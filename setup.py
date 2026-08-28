from setuptools import setup

setup(
    name="flux-3-video-edit-api",
    version="0.2.0",
    author="Anil Matcha",
    description="Python wrapper for FLUX 3 Video Extend -- continues an existing video clip with new prompt-guided motion and scene development, via muapi.ai.",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    py_modules=["flux3_video_edit_api", "mcp_server"],
    install_requires=[
        "requests",
        "python-dotenv",
        "mcp[cli]"
    ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.7',
)
