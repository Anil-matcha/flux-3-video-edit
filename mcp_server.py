import json
from mcp.server.fastmcp import FastMCP
from flux3_video_edit_api import Flux3VideoEditAPI

# Initialize FastMCP server
mcp = FastMCP("FLUX 3 Video Edit API Server")

# Helper to get API client
def get_api():
    return Flux3VideoEditAPI()

@mcp.tool()
def extend_video(prompt: str, video_url: str, resolution: str = "720p",
                  aspect_ratio: str = None, duration: int = 5,
                  generate_audio: bool = True) -> str:
    """
    Continue an existing video clip with new prompt-guided motion using FLUX 3 Video Extend.

    Note: this is a continuation API, not a general instruction-driven editor
    (no arbitrary re-grade/restyle/object-swap).

    :param prompt: Text describing how the video should continue.
    :param video_url: URL of the source video to extend (<50MB, <15s).
    :param resolution: Output resolution ('720p' or '1080p').
    :param aspect_ratio: Optional output aspect ratio, e.g. '16:9', '9:16'.
    :param duration: Length of the extension in seconds (5-20, default 5).
    :param generate_audio: Whether to generate synchronized native audio.
    """
    api = get_api()
    result = api.extend_video(prompt, video_url, resolution, aspect_ratio, duration, generate_audio)
    return json.dumps(result, indent=2)

@mcp.tool()
def extend_video_draft(prompt: str, video_url: str, aspect_ratio: str = None,
                        duration: int = 5, generate_audio: bool = True) -> str:
    """
    Fast, lower-cost draft mode of FLUX 3 Video Extend for testing continuity
    before a final-quality extension.

    :param prompt: Text describing how the video should continue.
    :param video_url: URL of the source video to extend (<50MB, <15s).
    :param aspect_ratio: Optional output aspect ratio.
    :param duration: Length of the draft extension in seconds (5-20, default 5).
    :param generate_audio: Whether to generate synchronized native audio.
    """
    api = get_api()
    result = api.extend_video_draft(prompt, video_url, aspect_ratio, duration, generate_audio)
    return json.dumps(result, indent=2)

@mcp.tool()
def upload_file(file_path: str) -> str:
    """
    Upload a local file (image or video) to MuAPI for use in generation tasks.

    :param file_path: Local path to the file.
    """
    api = get_api()
    result = api.upload_file(file_path)
    return json.dumps(result, indent=2)

@mcp.tool()
def get_task_status(request_id: str) -> str:
    """
    Check the status and get results of a generation task.

    :param request_id: The ID returned from a generation tool call.
    """
    api = get_api()
    result = api.get_result(request_id)
    return json.dumps(result, indent=2)

if __name__ == "__main__":
    mcp.run()
