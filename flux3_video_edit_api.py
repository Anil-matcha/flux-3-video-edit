import os
import requests
import time
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()


class Flux3VideoEditAPI:
    def __init__(self, api_key=None):
        """
        Initialize the FLUX 3 Video Edit API client.
        :param api_key: Your MuAPI.ai API key. Defaults to MUAPI_API_KEY environment variable.
        """
        self.api_key = api_key or os.getenv("MUAPI_API_KEY")
        if not self.api_key:
            raise ValueError("API Key is required. Set MUAPI_API_KEY in .env or pass it to the constructor.")

        self.base_url = "https://api.muapi.ai/api/v1"
        self.headers = {
            "x-api-key": self.api_key,
            "Content-Type": "application/json"
        }

    def edit_video(self, prompt, video_url, resolution="720p", aspect_ratio=None,
                   duration=5, generate_audio=True):
        """
        Submits a FLUX 3 Video Extend task.

        Note: FLUX 3 does not ship a general instruction-driven video editor
        (no arbitrary re-grade/restyle/object-swap). The live API is FLUX 3
        Video Extend: it CONTINUES an existing clip with new prompt-guided
        motion and scene development, with optional native synchronized
        audio, using Black Forest Labs' unified image/video/audio
        architecture. This method is kept under its original name for
        backwards compatibility with existing callers of this package, but
        it now calls the real flux-3-video-extend endpoint.

        :param prompt: Text describing how the video should continue (not a
            free-form edit instruction).
        :param video_url: URL of the source video to extend. Must be under
            50MB and under 15 seconds.
        :param resolution: Output resolution ('720p' or '1080p').
        :param aspect_ratio: Optional output aspect ratio, one of
            '21:9', '2:1', '16:9', '4:3', '1:1', '3:4', '9:16'.
        :param duration: Length of the extension in seconds (5-20, default 5).
        :param generate_audio: Whether to generate synchronized native audio.
        :return: JSON response with request_id.
        """
        endpoint = f"{self.base_url}/flux-3-video-extend"
        payload = {
            "prompt": prompt,
            "video_url": video_url,
            "resolution": resolution,
            "duration": duration,
            "generate_audio": generate_audio,
        }
        if aspect_ratio:
            payload["aspect_ratio"] = aspect_ratio
        return self._post_request(endpoint, payload)

    def extend_video(self, prompt, video_url, resolution="720p", aspect_ratio=None,
                      duration=5, generate_audio=True):
        """Alias for edit_video() with a name that matches what the API actually does."""
        return self.edit_video(prompt, video_url, resolution, aspect_ratio, duration, generate_audio)

    def extend_video_draft(self, prompt, video_url, aspect_ratio=None,
                            duration=5, generate_audio=True):
        """
        Submits a FLUX 3 Video Extend Draft task -- a fast, lower-cost draft
        mode for testing continuity and camera movement before extending a
        clip with extend_video(). Same fields as extend_video() but no
        resolution parameter (billed flat regardless of quality tier).

        :param prompt: Text describing how the video should continue.
        :param video_url: URL of the source video to extend (<50MB, <15s).
        :param aspect_ratio: Optional output aspect ratio.
        :param duration: Length of the draft extension in seconds (5-20, default 5).
        :param generate_audio: Whether to generate synchronized native audio.
        :return: JSON response with request_id.
        """
        endpoint = f"{self.base_url}/flux-3-video-extend-draft"
        payload = {
            "prompt": prompt,
            "video_url": video_url,
            "duration": duration,
            "generate_audio": generate_audio,
        }
        if aspect_ratio:
            payload["aspect_ratio"] = aspect_ratio
        return self._post_request(endpoint, payload)

    # ------------------------------------------------------------------
    # Shared helpers
    # ------------------------------------------------------------------

    def _post_request(self, endpoint, payload):
        response = requests.post(endpoint, json=payload, headers=self.headers)
        response.raise_for_status()
        return response.json()

    def upload_file(self, file_path):
        """
        Uploads a file (image or video) to MuAPI for use in generation tasks.

        :param file_path: Path to the local file to upload.
        :return: JSON response from MuAPI containing the URL of the uploaded file.
        """
        endpoint = f"{self.base_url}/upload_file"

        # Omit Content-Type to let requests set the multipart boundary automatically
        headers = {
            "x-api-key": self.api_key
        }

        with open(file_path, "rb") as file_data:
            files = {"file": file_data}
            response = requests.post(endpoint, headers=headers, files=files)

        response.raise_for_status()
        return response.json()

    def get_result(self, request_id):
        """
        Polls for the result of a generation task.
        """
        endpoint = f"{self.base_url}/predictions/{request_id}/result"
        response = requests.get(endpoint, headers=self.headers)
        response.raise_for_status()
        return response.json()

    def wait_for_completion(self, request_id, poll_interval=5, timeout=300):
        """
        Waits for the generation task to complete and returns the result.
        """
        start_time = time.time()
        while time.time() - start_time < timeout:
            result = self.get_result(request_id)
            status = result.get("status")

            if status == "completed":
                return result
            elif status == "failed":
                raise Exception(f"Generation failed: {result.get('error')}")

            print(f"Status: {status}. Waiting {poll_interval} seconds...")
            time.sleep(poll_interval)

        raise TimeoutError("Timed out waiting for generation to complete.")


if __name__ == "__main__":
    # Example usage for FLUX 3 Video Edit
    try:
        api = Flux3VideoEditAPI()
        prompt = "Apply a cinematic teal-and-orange grade"
        video_url = "https://example.com/clip.mp4"

        print(f"Submitting FLUX 3 Video Extend task with prompt: {prompt}")
        submission = api.extend_video(prompt=prompt, video_url=video_url, resolution="1080p")
        request_id = submission.get("request_id")
        print(f"Task submitted. Request ID: {request_id}")

        print("Waiting for completion...")
        result = api.wait_for_completion(request_id)
        print(f"Generation completed! Output: {result.get('outputs', [result.get('url')])}")

    except Exception as e:
        print(f"Error: {e}")
