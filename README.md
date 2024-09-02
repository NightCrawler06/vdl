# Simple Video Downloader

## Overview

The **Simple Video Downloader** is a Python script that allows you to easily download videos from various platforms. By leveraging `yt-dlp` and `FFmpeg`, this tool ensures you get the best available quality with minimal effort.

## Usage

1. **Run the Script**:
   - Execute the following command in your terminal:
     ```bash
     python3 vdl.py
     ```

2. **Enter the Video URL**:
   - You will be prompted to enter the URL of the video you want to download. Paste the link and press `ENTER`.

3. **Select Download Options**:
   - When prompted for a format, simply press `ENTER` to use the default settings, or specify a format code if needed.

4. **Download**:
   - The download process will start automatically. Please wait for the download to complete.

## Setup

### Requirements

- **Python 3.x**
- **FFmpeg**
- **yt-dlp**

### Installation

1. **Install FFmpeg**:
   - Ensure that `FFmpeg` is installed on your system. It is required for merging audio and video streams. You can download and install it from [FFmpeg's official website](https://ffmpeg.org/download.html).

2. **Install yt-dlp**:
   - Install `yt-dlp`, the tool used for downloading videos:
     ```bash
     pip install yt-dlp
     ```
