# FLUX 3 Video Edit API: Python Wrapper for Black Forest Labs' Video Continuation (FLUX 3 Video Extend)

[![Powered by MuAPI](https://img.shields.io/badge/Powered%20by-MuAPI-6366f1?style=flat-square&logo=data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHZpZXdCb3g9IjAgMCAyNCAyNCI+PHBhdGggZmlsbD0id2hpdGUiIGQ9Ik0xMiAyQzYuNDggMiAyIDYuNDggMiAxMnM0LjQ4IDEwIDEwIDEwIDEwLTQuNDggMTAtMTBTMTcuNTIgMiAxMiAyem0tMSAxNHYtNGgtMnYtMmg0djZoLTJ6bTAtOFY2aDJ2MmgtMnoiLz48L3N2Zz4=)](https://muapi.ai?utm_source=github&utm_medium=badge&utm_campaign=flux-3-video-edit-api)

[![PyPI version](https://img.shields.io/pypi/v/flux-3-video-edit-api.svg)](https://pypi.org/project/flux-3-video-edit-api/)
[![GitHub stars](https://img.shields.io/github/stars/Anil-matcha/flux-3-video-edit.svg)](https://github.com/Anil-matcha/flux-3-video-edit/stargazers)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Python 3.7+](https://img.shields.io/badge/python-3.7+-blue.svg)](https://www.python.org/downloads/)

A Python wrapper for **FLUX 3 Video Extend** — Black Forest Labs' video-continuation mode within the **FLUX 3** family, delivered via [muapi.ai](https://muapi.ai/flux-3?utm_source=github&utm_medium=readme&utm_campaign=flux-3-video-edit-api). FLUX 3 Video Extend continues an existing clip with new prompt-guided motion, scene development, and camera movement — with optional native synchronized audio — using Black Forest Labs' unified image/video/audio architecture, so the continuation stays physically grounded and consistent with the source clip.

> **Important:** FLUX 3 does not ship a general instruction-driven video editor (no arbitrary re-grade, restyle, or object-swap on an existing clip). The live API is a **continuation** model — it extends a clip forward in time based on your prompt, it does not modify the clip's existing frames. This package's method names (`edit_video`, etc.) are kept for backwards compatibility, but they call the real `flux-3-video-extend` endpoint. Prefer the new `extend_video()` alias in new code.

> **Status: Live.** `flux-3-video-extend` and its fast/cheap draft sibling `flux-3-video-extend-draft` are both live on MuAPI today.

## Related Projects

- [Flux-3-Dev-API](https://github.com/Anil-matcha/Flux-3-Dev-API) — Python SDK for FLUX 3 Dev, plus the full FLUX 3 image/video family
- [flux-3-video-upscaler](https://github.com/Anil-matcha/flux-3-video-upscaler) — Python SDK for upscaling FLUX 3 (or any) video output
- [flux-3-omni](https://github.com/Anil-matcha/flux-3-omni) — Python SDK for FLUX 3's multi-reference Omni Reference mode
- [flux-3-video-api](https://github.com/SamurAIGPT/flux-3-video-api) — Python wrapper focused on FLUX 3 Text-to-Video and Image-to-Video
- [awesome-flux-3-api-prompts](https://github.com/Anil-matcha/awesome-flux-3-api-prompts) — FLUX 3 API guide, prompt engineering, and a curated prompt library
- [flux-3-comfyui](https://github.com/Anil-matcha/flux-3-comfyui) — ComfyUI custom nodes for the FLUX 3 API
- [Open-Generative-AI](https://github.com/Anil-matcha/Open-Generative-AI) — open-source, self-hosted AI image & video generation studio (200+ models)

## 🚀 Why FLUX 3 Video Extend?

FLUX 3 is Black Forest Labs' newest frontier model — a unified multimodal system jointly trained across image, video, and audio, extendable to action prediction for robotics. **FLUX 3 Video Extend** brings that same architecture to continuing existing footage instead of only generating new clips from scratch:

- **Prompt-Guided Continuation**: A single text prompt drives what happens next in the clip — no masks, keyframes, or timeline tools required.
- **Physically Grounded**: The continuation stays consistent with the clip's original lighting, motion, and geometry rather than warping the scene.
- **Native Synchronized Audio**: Optional audio generation for the extended portion, at no extra charge.
- **Shares FLUX 3's Architecture**: The same unified model that powers FLUX 3 Video and FLUX 3 Action, so quality and behavior track the flagship model.
- **Developer-First**: Simple Python SDK on top of MuAPI's unified infrastructure — no separate account or waitlist needed once you have a MuAPI key.

## 🌟 Key Features

- ✅ **FLUX 3 Video Extend**: Continue an existing video clip with new prompt-guided motion via `extend_video()`.
- ✅ **FLUX 3 Video Extend Draft**: Fast, lower-cost draft mode for testing continuity before a final-quality extension via `extend_video_draft()`.
- ✅ **File Upload**: Upload local videos directly using `upload_file()`.
- ✅ **MCP Server**: Use FLUX 3 Video Extend as a Model Context Protocol server for Claude Desktop, Cursor, and other MCP clients.

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

## 🤖 FLUX 3 Video Extend MCP Server

Use FLUX 3 Video Extend as an **MCP (Model Context Protocol)** server so AI clients (like Claude Desktop or Cursor) can directly invoke the video-continuation tool.

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

# Continue an existing video clip
print("Submitting FLUX 3 Video Extend task...")
submission = api.extend_video(
    prompt="The camera pulls back to reveal a sunrise breaking over the skyline",
    video_url="https://example.com/clip.mp4",
    resolution="1080p",
    duration=5,
)

# Wait for completion
result = api.wait_for_completion(submission["request_id"])
print(f"Success! Output: {result['outputs'][0]}")
```

---

## 📡 API Endpoint & Reference

### FLUX 3 Video Extend
**Endpoint**: `POST https://api.muapi.ai/api/v1/flux-3-video-extend`

```bash
curl --location --request POST "https://api.muapi.ai/api/v1/flux-3-video-extend" \
  --header "Content-Type: application/json" \
  --header "x-api-key: YOUR_API_KEY" \
  --data-raw '{
      "prompt": "The camera pulls back to reveal a sunrise breaking over the skyline",
      "video_url": "https://example.com/clip.mp4",
      "resolution": "1080p",
      "duration": 5,
      "generate_audio": true
  }'
```

**Python SDK:**
```python
submission = api.extend_video(
    prompt="The camera pulls back to reveal a sunrise breaking over the skyline",
    video_url="https://example.com/clip.mp4",
    resolution="1080p",
    duration=5,
)
result = api.wait_for_completion(submission["request_id"])
print(result["outputs"][0])
```

### FLUX 3 Video Extend Draft (fast, lower-cost)
**Endpoint**: `POST https://api.muapi.ai/api/v1/flux-3-video-extend-draft`

```python
submission = api.extend_video_draft(
    prompt="The camera pulls back to reveal a sunrise breaking over the skyline",
    video_url="https://example.com/clip.mp4",
    duration=5,
)
```

The draft endpoint has no `resolution` parameter — it's tuned purely for speed and cost during iteration.

---

## 📖 Method Reference

| Method | Parameters | Description |
| :--- | :--- | :--- |
| `extend_video` (alias: `edit_video`) | `prompt`, `video_url`, `resolution`, `aspect_ratio`, `duration`, `generate_audio` | Continue an existing video clip with new prompt-guided motion. |
| `extend_video_draft` | `prompt`, `video_url`, `aspect_ratio`, `duration`, `generate_audio` | Fast, lower-cost draft mode of the same continuation. |
| `upload_file` | `file_path` | Upload a local file (image or video) to MuAPI for use in generation tasks. |
| `get_result` | `request_id` | Check task status for a FLUX 3 Video Extend generation. |
| `wait_for_completion` | `request_id`, `poll_interval`, `timeout` | Blocking helper that polls until the task completes. |

---

## 💰 Pricing

| Variant | Price |
| :--- | :--- |
| Video Extend, 720p | $0.25/second |
| Video Extend, 1080p | $0.42/second |
| Video Extend Draft | $0.09/second (flat) |

Billed duration rounds up to the next whole second, capped at 20 seconds. Native audio generation is included at no extra charge.

---

## 🔗 Official Resources
- **FLUX 3 Announcement (Black Forest Labs)**: [bfl.ai/models/flux-3](https://bfl.ai/models/flux-3)
- **Playground — FLUX 3 Video Extend**: [muapi.ai/playground/flux-3-video-extend](https://muapi.ai/playground/flux-3-video-extend?utm_source=github&utm_medium=readme&utm_campaign=flux-3-video-edit-api)
- **Playground — FLUX 3 (all variants)**: [muapi.ai/flux-3](https://muapi.ai/flux-3?utm_source=github&utm_medium=readme&utm_campaign=flux-3-video-edit-api)
- **Playground — FLUX Kontext (available today)**: [muapi.ai/flux-kontext](https://muapi.ai/flux-kontext?utm_source=github&utm_medium=readme&utm_campaign=flux-3-video-edit-api)
- **API Provider**: [MuAPI.ai](https://muapi.ai?utm_source=github&utm_medium=readme&utm_campaign=flux-3-video-edit-api)

## 📄 License
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

**Keywords**: FLUX 3 API, FLUX 3 Video Extend, FLUX 3 Video Extend API, Black Forest Labs FLUX 3, FLUX 3 Python SDK, FLUX 3 video continuation, AI video generation API, MuAPI, Python video generation SDK.
