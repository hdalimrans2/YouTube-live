# 🎥 2L YT Live - Termux YouTube Tool

![Version](https://img.shields.io/badge/version-1.0-blue)
![Termux](https://img.shields.io/badge/Termux-Required-green)
![Python](https://img.shields.io/badge/Python-3.x-yellow)

**2L YT Live** is a powerful YouTube tool for Termux that allows you to download videos, stream local files, relay live streams, and more — all from your Android terminal.

<p align="center">
  <img src="https://raw.githubusercontent.com/hdalimrans2/YouTube-live/main/assets/demo.gif" alt="Demo" width="600">
</p>

---

## 🔒 Access Password

This tool is protected. You need a valid password to use it.

👉 **Get your password from:** [https://www.nxalimrans.site](https://www.nxalimrans.site)

After obtaining the password, you will be prompted to enter it when you run the tool.

---

## 📺 Watch Installation & Usage Guide

[![Watch the video](https://img.youtube.com/vi/YOUR_VIDEO_ID/0.jpg)](https://www.youtube.com/watch?v=YOUR_VIDEO_ID)

> ⚠️ **Replace `YOUR_VIDEO_ID` with your actual YouTube video ID** (e.g., `dQw4w9WgXcQ`).  
> The video should show how to install and use the tool step-by-step.

<details>
<summary>📹 Click to watch video directly on GitHub</summary>
<br>
<!-- Replace with your actual YouTube iframe -->
<iframe width="560" height="315" src="https://www.youtube.com/embed/YOUR_VIDEO_ID" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>
</details>

---

## ✨ Features

- 📥 **Download YouTube videos** (best quality)
- 📡 **Stream to YouTube Live** from:
  - Local video files (with loop option)
  - YouTube URLs (download & stream, auto-delete temp file)
  - Direct streaming (no file saved, no loop)
- 🔁 **Relay an existing YouTube live stream**
- 🛡️ **Password protected** – access via [nxalimrans.site](https://www.nxalimrans.site)
- 🧹 **Auto-cleanup** of temporary files
- 🎨 Beautiful CLI interface with `rich` library
- 📱 Optimized for **Termux** on Android

---

## 🚀 Installation in Termux

Open Termux and run the following commands one by one:

```bash
# Update packages
pkg update && pkg upgrade -y

# Install required packages
pkg install python ffmpeg git -y

# Clone the repository
git clone https://github.com/hdalimrans2/YouTube-live.git

# Enter directory
cd YouTube-live

# Install Python dependencies
pip install rich yt-dlp

# Make the script executable
chmod +x nx.py

# Run the tool
python nx.py
