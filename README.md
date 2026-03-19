

![Version](https://img.shields.io/badge/version-1.0-blue)
![Termux](https://img.shields.io/badge/Termux-green)
![Python](https://img.shields.io/badge/Python-3.x-yellow)

**2L YT Live**是一个 শক্তিশালী Termux টুল যা আপনাকে Android টার্মিনাল থেকে YouTube ভিডিও ডাউনলোড, লোকাল ফাইল স্ট্রিম, লাইভ স্ট্রিম রিলে এবং আরও অনেক কিছু করতে দেয়।

---

## 🔒 অ্যাক্সেস পাসওয়ার্ড

এই টুল ব্যবহারের জন্য বৈধ পাসওয়ার্ড প্রয়োজন।

👉 **আপনার পাসওয়ার্ড নিন:** [https://www.nxalimrans.site](https://www.nxalimrans.site)

টুল রান করালে এটি আপনাকে পাসওয়ার্ড চাইবে। উপরের ওয়েবসাইট থেকে পাসওয়ার্ড সংগ্রহ করে সঠিকভাবে প্রবেশ করান।

---

## 📺 ইনস্টলেশন ও ব্যবহার গাইড (ভিডিও)

টুলটি কিভাবে ইনস্টল ও ব্যবহার করতে হয় তার সম্পূর্ণ ভিডিও নির্দেশিকা দেখুন:

[![ভিডিও দেখুন](https://img.youtube.com/vi/YOUR_VIDEO_ID/0.jpg)](https://www.youtube.com/watch?v=YOUR_VIDEO_ID)



<details>
<summary>📹 সরাসরি GitHub-এ ভিডিও দেখতে ক্লিক করুন</summary>
<br>
<!-- আপনার ইউটিউব ভিডিওর iframe কোড এখানে বসান -->
<iframe width="560" height="315" src="https://www.youtube.com/embed/YOUR_VIDEO_ID" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>
</details>

---

## ⚡ এক লাইনে ইনস্টলেশন

নিচের কমান্ডটি কপি করে Termux-এ পেস্ট করুন। এটি সবকিছু নিজে নিজেই ইনস্টল করবে এবং টুল রান করাবে:

```bash
pkg update -y && pkg upgrade -y && pkg install python ffmpeg git -y && git clone https://github.com/hdalimrans2/YouTube-live.git && cd YouTube-live && pip install rich yt-dlp && chmod +x nx.py && python nx.py
```

---

## 📝 ধাপে ধাপে ইনস্টলেশন (বিস্তারিত)

নিচের ধাপগুলো অনুসরণ করুন (এক লাইনের কমান্ড কাজ না করলে):


# 1. প্যাকেজ আপডেট করুন
```bash
pkg update && pkg upgrade -y
```
# 2. প্রয়োজনীয় প্যাকেজ ইনস্টল করুন
```bash
pkg install python ffmpeg git -y
```
# 3. রিপোজিটরি ক্লোন করুন
```bash
git clone https://github.com/hdalimrans2/YouTube-live.git
```
# 4. ডিরেক্টরিতে প্রবেশ করুন
```bash
cd YouTube-live
```
# 5. Python ডিপেন্ডেন্সি ইনস্টল করুন
```bash
pip install rich yt-dlp
```
# 6. স্ক্রিপ্ট এক্সিকিউটেবল করুন
```bash
chmod +x nx.py
```
# 7. টুল রান করুন
```bash
python nx.py
```

> **নোট:** প্রথমবার টুল রান করালে এটি স্টোরেজ পারমিশন দিন 
```bash
termux-setup-storage
```

## ✨ বৈশিষ্ট্যসমূহ

- 📥 **YouTube ভিডিও ডাউনলোড** (সেরা কোয়ালিটিতে)
- 📡 **YouTube Live-এ স্ট্রিম** করুন:
  - লোকাল ভিডিও ফাইল থেকে (লুপ অপশন সহ)
  - YouTube URL থেকে (ডাউনলোড করে স্ট্রিম, পরে অটো-ডিলিট)
  - ডাইরেক্ট স্ট্রিমিং (কোনো ফাইল সেভ হয় না, লুপ নেই)
- 🔁 **অন্য YouTube লাইভ স্ট্রিম রিলে** করুন
- 🛡️ **পাসওয়ার্ড প্রটেক্টেড** – এক্সেস নিতে হবে [nxalimrans.site](https://www.nxalimrans.site) থেকে
- 🧹 **অটো-ক্লিনআপ** – টেম্পোরারি ফাইল নিজে নিজেই মুছে যায়
- 🎨 সুন্দর CLI ইন্টারফেস (`rich` লাইব্রেরি ব্যবহার করে)
- 📱 **Termux-এর জন্য অপ্টিমাইজড** (Android)

---

## 🛠️ ব্যবহার বিধি

টুল রান করালে নিচের মেনু দেখতে পাবেন:

```
মেনু:
  1. 📥 YouTube ভিডিও ডাউনলোড
  2. 📡 YouTube Live-এ স্ট্রিম
  3. 🔁 YouTube লাইভ স্ট্রিম রিলে
  4. ℹ️  পরিচিতি
  5. 🚪 প্রস্থান
```

### 📥 অপশন ১: ডাউনলোড
- YouTube ভিডিওর URL দিন
- ভিডিও সেভ হবে `~/storage/downloads/NXALIMRANS/` ফোল্ডারে

### 📡 অপশন ২: স্ট্রিম
নিচের অপশন থেকে বাছাই করুন:
- **লোকাল ফাইল** – আপনার ডিভাইসের ভিডিও স্ট্রিম করুন
- **YouTube URL** – ডাউনলোড করে স্ট্রিম করুন (অটো-ডিলিট)
- **ডাইরেক্ট স্ট্রিমিং** – কোনো ফাইল সেভ না করে সরাসরি স্ট্রিম, স্টোরেজ বাঁচাতে ভালো
- **রিলে লাইভ** – অন্য কোনো লাইভ স্ট্রিম রি-ব্রডকাস্ট করুন

প্রত্যেকটি অপশনে **YouTube Stream Key** চাওয়া হবে (YouTube Studio > Go Live থেকে নিন)।

### 🔁 অপশন ৩: রিলে
একটি লাইভ YouTube URL এবং আপনার Stream Key দিন। টুলটি সেই লাইভ রি-ব্রডকাস্ট করবে।

### ℹ️ অপশন ৪: পরিচিতি
ডেভেলপার ও টুলের বিস্তারিত তথ্য দেখতে পাবেন।

---

## 👨‍💻 ডেভেলপার ও মালিক

**একমাত্র ডেভেলপার ও মালিক:**  
**NX AL IMRAN S**  
YouTube Content Creator & Termux ডেভেলপার

### 📱 সোশ্যাল মিডিয়া ও যোগাযোগ:

[![YouTube](https://img.shields.io/badge/YouTube-FF0000?style=for-the-badge&logo=youtube&logoColor=white)](https://youtube.com/@nx.al.imran.s)
[![Facebook](https://img.shields.io/badge/Facebook-1877F2?style=for-the-badge&logo=facebook&logoColor=white)](https://www.facebook.com/nx.al.imran.s)
[![Telegram](https://img.shields.io/badge/Telegram-2CA5E0?style=for-the-badge&logo=telegram&logoColor=white)](https://t.me/NXALIMRANS_bot)
[![Website](https://img.shields.io/badge/Website-4285F4?style=for-the-badge&logo=google-chrome&logoColor=white)](https://nxalimranss.blogspot.com)

> **কপিরাইট:** এই টুলের সম্পূর্ণ মালিকানা ও উন্নয়ন NX AL IMRAN S-এর। অনুমতি ছাড়া বাণিজ্যিক ব্যবহার বা পুনর্বিতরণ নিষিদ্ধ।

---

## 📂 রিপোজিটরি লিংক

**GitHub:** [https://github.com/hdalimrans2/YouTube-live.git](https://github.com/hdalimrans2/YouTube-live.git)

---

## 📌 প্রয়োজনীয় উপকরণ

- Termux (F-Droid বা GitHub থেকে ইনস্টল করুন, **Play Store-এর ভার্সন কাজ করবে না**)
- Android 7+
- ইন্টারনেট সংযোগ
- YouTube Stream Key (স্ট্রিমিংয়ের জন্য)

---

## 🤝 অবদান

এই টুলটি সম্পূর্ণরূপে **NX AL IMRAN S**-এর একক প্রচেষ্টায় তৈরি।  
যদি কোনো বাগ খুঁজে পান বা পরামর্শ থাকে, তবে GitHub-এ Issue খুলুন।

---

## ⚖️ লাইসেন্স

এই প্রোজেক্টটি **মালিকানাধীন (Proprietary)** – সর্বস্বত্ব সংরক্ষিত। অনুমোদন ছাড়া কোড কপি, বিতরণ বা বাণিজ্যিক ব্যবহার নিষিদ্ধ।

---

<p align="center">
  ❤️ তৈরি করেছেন <a href="https://youtube.com/@nx.al.imran.s">NX AL IMRAN S</a>
</p>
<p align="center">
  © ২০২৬ - সর্বস্বত্ব সংরক্ষিত
</p>
