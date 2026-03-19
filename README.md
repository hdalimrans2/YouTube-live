<h1 align="center">🚀 2L YT Live - Ultimate YouTube Tool</h1>

<p align="center">
  <img src="https://img.shields.io/badge/Python-3.x-blue?style=for-the-badge&logo=python" alt="Python">
  <img src="https://img.shields.io/badge/Platform-Termux-orange?style=for-the-badge&logo=termux" alt="Termux">
  <img src="https://img.shields.io/badge/Developer-NX%20AL%20IMRAN%20S-green?style=for-the-badge" alt="Developer">
  <img src="https://img.shields.io/badge/License-MIT-red?style=for-the-badge" alt="License">
</p>

<p align="center">
  <b>2L YT Live</b> হলো Termux ব্যবহারকারীদের জন্য একটি শক্তিশালী টুল। এর মাধ্যমে আপনি সহজেই ইউটিউব ভিডিও ডাউনলোড করতে পারবেন এবং যেকোনো ভিডিও বা লাইভ স্ট্রিম আপনার চ্যানেলে রিলে (Relay) করতে পারবেন।
</p>

---

## 📺 How to Use & Tutorial (ভিডিও টিউটোরিয়াল)

টুলটি কিভাবে ইনস্টল করবেন এবং পাসওয়ার্ড দিয়ে ব্যবহার করবেন তা দেখতে নিচের ভিডিওতে ক্লিক করুন:

<p align="center">
  <a href="https://www.youtube.com/watch?v=YOUR_VIDEO_ID_HERE">
    <img src="https://img.youtube.com/vi/YOUR_VIDEO_ID_HERE/maxresdefault.jpg" alt="Watch Tutorial" width="600" style="border-radius: 10px;">
  </a>
</p>

> **নোট:** গিটহাব সরাসরি `iframe` সাপোর্ট করে না, তাই উপরের থাম্বনেইল ছবিতে ক্লিক করলে সরাসরি ইউটিউবে ভিডিওটি ওপেন হবে। (ভিডিও আইডি `YOUR_VIDEO_ID_HERE` এর জায়গায় আপনার ভিডিওর আইডিটি বসিয়ে দিন)

---

## 🔑 Password (পাসওয়ার্ড)

এই টুলটি সুরক্ষিত এবং এটি ব্যবহার করার জন্য একটি পাসওয়ার্ড প্রয়োজন। পাসওয়ার্ডটি পেতে আমাদের অফিসিয়াল সাইটে ভিজিট করুন:

👉 **[Get Password From Here](https://www.nxalimrans.site)**

---

## ✨ Features (টুলটির বৈশিষ্ট্যসমূহ)

- 📥 **Video Downloader:** সরাসরি ইউটিউব থেকে সেরা কোয়ালিটিতে ভিডিও ডাউনলোড।
- 📡 **Local Stream:** আপনার ফোনের যেকোনো ভিডিও ইউটিউবে লাইভ স্ট্রিম করুন (Loop অপশনসহ)।
- 🔄 **Relay Stream:** অন্য কোনো ইউটিউব লাইভকে নিজের চ্যানেলে সরাসরি রিলে করুন।
- ⚡ **Direct Stream:** ভিডিও ডাউনলোড না করেই সরাসরি লিঙ্ক থেকে স্ট্রিম করার সুবিধা।
- 🛠️ **Auto Setup:** সব প্রয়োজনীয় প্যাকেজ (FFmpeg, yt-dlp) টুলটি নিজে থেকেই ইনস্টল করে নেবে।

---

## 📥 Installation (ইনস্টলেশন পদ্ধতি)

আপনার Termux অ্যাপে নিচের কমান্ডগুলো কপি করে একে একে পেস্ট করুন:

```bash
apt update && apt upgrade -y
pkg install python git ffmpeg -y
git clone https://github.com/YOUR_GITHUB_USERNAME/YOUR_REPO_NAME.git
cd YOUR_REPO_NAME
python nx.py
