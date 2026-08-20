# FLUX 3 Video Edit API: Python Wrapper for Black Forest Labs' Instruction-Driven Video Editing

[![Powered by MuAPI](https://img.shields.io/badge/Powered%20by-MuAPI-6366f1?style=flat-square&logo=data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHZpZXdCb3g9IjAgMCAyNCAyNCI+PHBhdGggZmlsbD0id2hpdGUiIGQ9Ik0xMiAyQzYuNDggMiAyIDYuNDggMiAxMnM0LjQ4IDEwIDEwIDEwIDEwLTQuNDggMTAtMTBTMTcuNTIgMiAxMiAyem0tMSAxNHYtNGgtMnYtMmg0djZoLTJ6bTAtOFY2aDJ2MmgtMnoiLz48L3N2Zz4=)](https://muapi.ai?utm_source=github&utm_medium=badge&utm_campaign=flux-3-video-edit-api)

[![PyPI version](https://img.shields.io/pypi/v/flux-3-video-edit-api.svg)](https://pypi.org/project/flux-3-video-edit-api/)
[![GitHub stars](https://img.shields.io/github/stars/Anil-matcha/flux-3-video-edit.svg)](https://github.com/Anil-matcha/flux-3-video-edit/stargazers)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Python 3.7+](https://img.shields.io/badge/python-3.7+-blue.svg)](https://www.python.org/downloads/)

A Python wrapper for **FLUX 3 Video Edit** — Black Forest Labs' instruction-driven video editing mode within the **FLUX 3** family, delivered via [muapi.ai](https://muapi.ai/flux-3?utm_source=github&utm_medium=readme&utm_campaign=flux-3-video-edit-api). FLUX 3 Video Edit applies natural-language instructions directly to existing footage — re-grading color, restyling a scene, swapping an object, or extending a shot — using Black Forest Labs' unified image/video/audio architecture, so edits stay physically grounded and consistent with the source clip.

> **Status: Coming Soon.** Black Forest Labs lists video editing as coming soon for FLUX 3. This SDK targets the endpoint MuAPI is preparing for it (`flux-3-video-edit`); requests will 404 until Black Forest Labs opens general access and MuAPI activates the endpoint. [Reserve an API key](https://muapi.ai/flux-3?utm_source=github&utm_medium=readme&utm_campaign=flux-3-video-edit-api) now to get access the moment it goes live.

## Related Projects

- [Flux-3-Dev-API](https://github.com/Anil-matcha/Flux-3-Dev-API) — Python SDK for FLUX 3 Dev, plus the full FLUX 3 image/video family
- [flux-3-video-upscaler](https://github.com/Anil-matcha/flux-3-video-upscaler) — Python SDK for upscaling FLUX 3 (or any) video output
- [flux-3-omni](https://github.com/Anil-matcha/flux-3-omni) — Python SDK for FLUX 3's multi-reference Omni Reference mode
- [flux-3-video-api](https://github.com/SamurAIGPT/flux-3-video-api) — Python wrapper focused on FLUX 3 Text-to-Video and Image-to-Video
- [awesome-flux-3-api-prompts](https://github.com/Anil-matcha/awesome-flux-3-api-prompts) — FLUX 3 API guide, prompt engineering, and a curated prompt library
- [flux-3-comfyui](https://github.com/Anil-matcha/flux-3-comfyui) — ComfyUI custom nodes for the FLUX 3 API
- [Open-Generative-AI](https://github.com/Anil-matcha/Open-Generative-AI) — open-source, self-hosted AI image & video generation studio (200+ models)

## 🚀 Why FLUX 3 Video Edit?

FLUX 3 is Black Forest Labs' newest frontier model — a unified multimodal system jointly trained across image, video, and audio, extendable to action prediction for robotics. **FLUX 3 Video Edit** brings that same architecture to editing existing footage instead of generating new clips from scratch:

- **Instruction-Driven**: A single text prompt drives the edit — no masks, keyframes, or timeline tools required.
- **Physically Grounded**: Edits stay consistent with the clip's original lighting, motion, and geometry rather than warping the scene.
- **Shares FLUX 3's Architecture**: The same unified model that powers FLUX 3 Video and FLUX 3 Action, so quality and behavior track the flagship model.
- **Developer-First**: Simple Python SDK on top of MuAPI's unified infrastructure — no separate account or waitlist needed once you have a MuAPI key.

## 🌟 Key Features

- ✅ **FLUX 3 Video Edit**: Apply a text instruction to an existing video clip via `edit_video()`.
- ✅ **File Upload**: Upload local videos directly using `upload_file()`.
- ✅ **MCP Server**: Use FLUX 3 Video Edit as a Model Context Protocol server for Claude Desktop, Cursor, and other MCP clients.

---

## 🛠 Installation

### Via Pip (Recommended)
```bash
pip install flux-3-video-edit-api
```

### From Source
```bash
git clone https://github.com/Anil-matcha/flux-3-video-edit.git
cd flux-3-video-edit
pip install -r requirements.txt
```

### Configuration
Create a `.env` file in the root directory and add your [MuAPI](https://muapi.ai/flux-3?utm_source=github&utm_medium=readme&utm_campaign=flux-3-video-edit-api) API key:
```env
MUAPI_API_KEY=your_muapi_api_key_here
```

---

## 🤖 FLUX 3 Video Edit MCP Server

Use FLUX 3 Video Edit as an **MCP (Model Context Protocol)** server so AI clients (like Claude Desktop or Cursor) can directly invoke the video-editing tool.

### Running the MCP Server
1. Ensure `MUAPI_API_KEY` is set in your environment.
2. Run the server:
   ```bash
   python3 mcp_server.py
   ```
3. To test with the MCP Inspector:
   ```bash
   npx -y @modelcontextprotocol/inspector python3 mcp_server.py
   ```

---

## 💻 Quick Start (Python)

```python
from flux3_video_edit_api import Flux3VideoEditAPI

# Initialize the client
api = Flux3VideoEditAPI()

# Edit an existing video clip
print("Submitting FLUX 3 Video Edit task...")
submission = api.edit_video(
    prompt="Apply a cinematic teal-and-orange grade",
    video_url="https://example.com/clip.mp4",
    resolution="1080p"
)

# Wait for completion
result = api.wait_for_completion(submission["request_id"])
print(f"Success! Output: {result['outputs'][0]}")
```

---

## 📡 API Endpoint & Reference

### FLUX 3 Video Edit
**Endpoint**: `POST https://api.muapi.ai/api/v1/flux-3-video-edit`

```bash
curl --location --request POST "https://api.muapi.ai/api/v1/flux-3-video-edit" \
  --header "Content-Type: application/json" \
  --header "x-api-key: YOUR_API_KEY" \
  --data-raw '{
      "prompt": "Apply a cinematic teal-and-orange grade",
      "video_url": "https://example.com/clip.mp4",
      "resolution": "1080p"
  }'
```

**Python SDK:**
```python
submission = api.edit_video(
    prompt="Apply a cinematic teal-and-orange grade",
    video_url="https://example.com/clip.mp4",
    resolution="1080p",
)
result = api.wait_for_completion(submission["request_id"])
print(result["outputs"][0])
```

---

## 📖 Method Reference

| Method | Parameters | Description |
| :--- | :--- | :--- |
| `edit_video` | `prompt`, `video_url`, `resolution` | Apply a text-instruction edit to an existing video clip. |
| `upload_file` | `file_path` | Upload a local file (image or video) to MuAPI for use in generation tasks. |
| `get_result` | `request_id` | Check task status for a FLUX 3 Video Edit generation. |
| `wait_for_completion` | `request_id`, `poll_interval`, `timeout` | Blocking helper that polls until the task completes. |

---

## 🔗 Official Resources
- **FLUX 3 Announcement (Black Forest Labs)**: [bfl.ai/models/flux-3](https://bfl.ai/models/flux-3)
- **Playground — FLUX 3 (all variants)**: [muapi.ai/flux-3](https://muapi.ai/flux-3?utm_source=github&utm_medium=readme&utm_campaign=flux-3-video-edit-api)
- **Playground — FLUX Kontext (available today)**: [muapi.ai/flux-kontext](https://muapi.ai/flux-kontext?utm_source=github&utm_medium=readme&utm_campaign=flux-3-video-edit-api)
- **API Provider**: [MuAPI.ai](https://muapi.ai?utm_source=github&utm_medium=readme&utm_campaign=flux-3-video-edit-api)

## 📄 License
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

**Keywords**: FLUX 3 API, FLUX 3 Video Edit, FLUX 3 Video Edit API, Black Forest Labs FLUX 3, FLUX 3 Python SDK, FLUX 3 video editing, AI video editing API, AI video generation API, MuAPI, Python video editing SDK.
