import json
from mcp.server.fastmcp import FastMCP
from flux3_video_edit_api import Flux3VideoEditAPI

# Initialize FastMCP server
mcp = FastMCP("FLUX 3 Video Edit API Server")

# Helper to get API client
def get_api():
    return Flux3VideoEditAPI()

@mcp.tool()
def edit_video(prompt: str, video_url: str, resolution: str = "720p") -> str:
    """
    Edit an existing video clip with a text instruction using FLUX 3 Video Edit.

    :param prompt: Text instruction describing the edit to apply.
    :param video_url: URL of the source video to edit.
    :param resolution: Output resolution ('480p', '720p', or '1080p').
    """
    api = get_api()
    result = api.edit_video(prompt, video_url, resolution)
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
