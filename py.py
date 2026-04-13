#!/data/data/com.termux/files/usr/bin/python

import os
import sys
import subprocess
import shutil
import signal
import time
import glob

try:
    from rich.console import Console
    from rich.panel import Panel
    from rich.prompt import Prompt
    from rich import print as rprint
    rich_ok = True
except ImportError:
    print("📦 Installing rich for better interface...")
    subprocess.check_call([sys.executable, "-m", "pip", "install", "rich"])
    from rich.console import Console
    from rich.panel import Panel
    from rich.prompt import Prompt
    from rich import print as rprint
    rich_ok = True

console = Console()

# ---------- গ্লোবাল ভেরিয়েবল ----------
DOWNLOAD_DIR = os.path.expanduser("~/storage/downloads/NXALIMRANS")
TOOL_NAME = "2L YT Live"
DEV_NAME = "NX AL IMRAN S"
DEV_LINKS = {
    "YouTube": "https://youtube.com/@nx.al.imran.s",
    "Facebook": "https://www.facebook.com/nx.al.imran.s",
    "Telegram": "https://t.me/NXALIMRANS_bot",
    "Website": "https://nxalimranss.blogspot.com"
}

# ---------- সিগন্যাল হ্যান্ডলার ----------
def signal_handler(sig, frame):
    console.print("\n[red]⚠️  Tool stopped by user.[/red]")
    cleanup_temp_files()
    sys.exit(0)

signal.signal(signal.SIGINT, signal_handler)

# ---------- টেম্প ফাইল ক্লিনআপ ----------
def cleanup_temp_files():
    try:
        temp_pattern = os.path.join(DOWNLOAD_DIR, "temp_stream_*")
        for temp_file in glob.glob(temp_pattern):
            try:
                os.remove(temp_file)
                console.print(f"[dim]🧹 Cleaned up: {os.path.basename(temp_file)}[/dim]")
            except:
                pass
    except:
        pass

# ---------- হেল্পার: কমান্ড রান ----------
def run_cmd(cmd, capture_output=False):
    try:
        if capture_output:
            result = subprocess.run(cmd, shell=True, capture_output=True, text=True)
            return result.stdout.strip()
        else:
            subprocess.run(cmd, shell=True, check=True)
            return True
    except subprocess.CalledProcessError:
        return False

# ---------- প্যাকেজ চেক ও ইনস্টল ----------
def check_and_install_dependencies():
    console.print("[cyan]🔍 Checking required packages...[/cyan]")

    # yt-dlp
    try:
        import yt_dlp
        console.print("[green]✅ yt-dlp already installed.[/green]")
    except ImportError:
        console.print("[yellow]📦 Installing yt-dlp...[/yellow]")
        if run_cmd("pip install yt-dlp"):
            console.print("[green]✅ yt-dlp installed.[/green]")
        else:
            console.print("[red]❌ Failed to install yt-dlp. Please run: pip install yt-dlp[/red]")
            sys.exit(1)

    # ffmpeg
    if shutil.which("ffmpeg"):
        console.print("[green]✅ ffmpeg already installed.[/green]")
    else:
        console.print("[yellow]📦 Installing ffmpeg...[/yellow]")
        if run_cmd("pkg install ffmpeg -y"):
            console.print("[green]✅ ffmpeg installed.[/green]")
        else:
            console.print("[red]❌ Failed to install ffmpeg. Please run: pkg install ffmpeg[/red]")
            sys.exit(1)

# ---------- স্টোরেজ ও ফোল্ডার সেটআপ ----------
def setup_storage_and_folder():
    storage_path = os.path.expanduser("~/storage/downloads")
    if not os.path.exists(storage_path):
        console.print("[yellow]📁 Storage access not available. Please run: termux-setup-storage[/yellow]")
        Prompt.ask("Press Enter to try again")
        run_cmd("termux-setup-storage")
        time.sleep(3)  # পারমিশন সেট হওয়ার জন্য অপেক্ষা
        
    # আবার চেক করুন
    if not os.path.exists(storage_path):
        console.print("[red]❌ Storage setup failed. Please run 'termux-setup-storage' manually and restart the app.[/red]")
        sys.exit(1)

    os.makedirs(DOWNLOAD_DIR, exist_ok=True)
    console.print(f"[green]✅ Download folder: {DOWNLOAD_DIR}[/green]")

# ---------- ওয়েবসাইট ওপেন ----------
def open_website():
    try:
        subprocess.run(["termux-open-url", "https://nxalimranss.blogspot.com"])
    except:
        pass

# ---------- ডাউনলোড ----------
def download_video():
    url = Prompt.ask("[cyan]🎬 Enter YouTube video URL[/cyan]")
    if not url:
        console.print("[red]❌ No URL provided.[/red]")
        return

    console.print("[yellow]⏳ Downloading video...[/yellow]")
    try:
        # mp4 ফরম্যাটে ডাউনলোড নিশ্চিত করুন
        cmd = f'yt-dlp -f "best[ext=mp4]/best" --merge-output-format mp4 -o "{DOWNLOAD_DIR}/%(title)s.%(ext)s" "{url}"'
        subprocess.run(cmd, shell=True, check=True)
        console.print(f"[green]✅ Download complete! File saved in: {DOWNLOAD_DIR}[/green]")
    except subprocess.CalledProcessError as e:
        console.print(f"[red]❌ Download failed: {e}[/red]")

# ---------- লোকাল ফাইল পাথ যাচাই ----------
def get_valid_local_file():
    while True:
        file_path = Prompt.ask("[cyan]📁 Enter full path to video file[/cyan]")
        if os.path.isfile(file_path):
            return file_path
        else:
            console.print("[red]❌ File does not exist. Try again.[/red]")

# ---------- স্ট্রিমিং ফাংশন (অটো-রিকানেক্ট সহ) ----------
def stream_with_reconnect(ffmpeg_cmd, max_retries=5):
    """নেটওয়ার্ক ড্রপ হলে অটো-রিকানেক্ট সহ স্ট্রিমিং"""
    retry_count = 0
    while retry_count < max_retries:
        try:
            process = subprocess.Popen(ffmpeg_cmd, stdout=subprocess.DEVNULL, stderr=subprocess.PIPE)
            
            # স্ট্রিমিং মনিটরিং
            while True:
                time.sleep(1)
                if process.poll() is not None:
                    # প্রসেস শেষ হয়ে গেছে
                    break
                    
        except KeyboardInterrupt:
            console.print("\n[yellow]⏹️ Stream stopped by user.[/yellow]")
            process.terminate()
            return True
        except Exception as e:
            retry_count += 1
            if retry_count < max_retries:
                console.print(f"[yellow]⚠️ Connection lost. Reconnecting in 5 seconds... (Attempt {retry_count}/{max_retries})[/yellow]")
                time.sleep(5)
            else:
                console.print(f"[red]❌ Max retries reached. Streaming failed: {e}[/red]")
                return False
        
        if process.returncode == 0:
            console.print("[green]✅ Stream completed successfully.[/green]")
            return True
        else:
            retry_count += 1
            if retry_count < max_retries:
                console.print(f"[yellow]⚠️ Stream interrupted. Reconnecting... (Attempt {retry_count}/{max_retries})[/yellow]")
                time.sleep(5)
            else:
                console.print("[red]❌ Max retries reached.[/red]")
                return False
    
    return False

# ---------- লোকাল ফাইল স্ট্রিম (লুপ সহ) ----------
def stream_local_file(video_file, stream_key, loop_choice):
    # RTMPS ব্যবহার করুন (আরও নিরাপদ)
    rtmp_url = f"rtmps://a.rtmps.youtube.com:443/live2/{stream_key}"
    
    if not os.path.exists(video_file):
        console.print("[red]❌ Video file not found![/red]")
        return

    console.print(f"[green]✅ Video ready: {video_file}[/green]")
    console.print("[yellow]🚀 Starting stream... Press CTRL+C to stop.[/yellow]")

    # উন্নত এনকোডিং প্যারামিটার
    ffmpeg_cmd = ["ffmpeg", "-re"]
    
    # লুপ অপশন
    if loop_choice.lower() == 'y':
        ffmpeg_cmd.extend(["-stream_loop", "-1"])
    
    ffmpeg_cmd.extend([
        "-i", video_file,
        # ভিডিও সেটিংস - মোবাইলের জন্য অপ্টিমাইজড
        "-c:v", "libx264", "-preset", "ultrafast", "-tune", "zerolatency",
        "-b:v", "2000k", "-maxrate", "2000k", "-bufsize", "6000k",
        "-pix_fmt", "yuv420p", "-g", "60",  # Keyframe interval
        # অডিও সেটিংস
        "-c:a", "aac", "-b:a", "128k", "-ar", "44100",
        "-f", "flv", rtmp_url
    ])

    stream_with_reconnect(ffmpeg_cmd)

# ---------- ইউআরএল থেকে ডাউনলোড করে স্ট্রিম (লুপ সহ) ----------
def stream_from_url_download(url, stream_key, loop_choice):
    rtmp_url = f"rtmps://a.rtmps.youtube.com:443/live2/{stream_key}"
    console.print("[yellow]⏳ Downloading video from URL...[/yellow]")
    
    try:
        # mp4 ফরম্যাটে ডাউনলোড নিশ্চিত করুন
        temp_pattern = f"{DOWNLOAD_DIR}/temp_stream_%(title)s.%(ext)s"
        cmd_dl = f'yt-dlp -f "best[ext=mp4]/best" --merge-output-format mp4 -o "{temp_pattern}" "{url}"'
        subprocess.run(cmd_dl, shell=True, check=True)

        # ডাউনলোড করা ফাইলের নাম বের করুন
        info_cmd = f'yt-dlp --get-filename -f "best[ext=mp4]/best" --merge-output-format mp4 -o "{temp_pattern}" "{url}"'
        result = subprocess.run(info_cmd, shell=True, capture_output=True, text=True)
        filename = result.stdout.strip()
        
        if not filename:
            console.print("[red]❌ Could not determine downloaded filename.[/red]")
            return
        
        # ফাইল এক্সিস্ট করে কিনা চেক করুন
        if os.path.exists(filename):
            video_file = filename
        else:
            # সম্ভাব্য এক্সটেনশন খুঁজুন
            base_name = os.path.splitext(filename)[0]
            for ext in ['.mp4', '.webm', '.mkv', '.flv']:
                test_file = base_name + ext
                if os.path.exists(test_file):
                    video_file = test_file
                    break
            else:
                console.print("[red]❌ Downloaded file not found.[/red]")
                return
                
    except Exception as e:
        console.print(f"[red]❌ Download error: {e}[/red]")
        return

    console.print(f"[green]✅ Video ready: {video_file}[/green]")
    console.print("[yellow]🚀 Starting stream... Press CTRL+C to stop.[/yellow]")

    ffmpeg_cmd = ["ffmpeg", "-re"]
    
    # লুপ অপশন
    if loop_choice.lower() == 'y':
        ffmpeg_cmd.extend(["-stream_loop", "-1"])
    
    ffmpeg_cmd.extend([
        "-i", video_file,
        # ভিডিও সেটিংস - মোবাইলের জন্য অপ্টিমাইজড
        "-c:v", "libx264", "-preset", "ultrafast", "-tune", "zerolatency",
        "-b:v", "2000k", "-maxrate", "2000k", "-bufsize", "6000k",
        "-pix_fmt", "yuv420p", "-g", "60",
        # অডিও সেটিংস
        "-c:a", "aac", "-b:a", "128k", "-ar", "44100",
        "-f", "flv", rtmp_url
    ])

    stream_with_reconnect(ffmpeg_cmd)

    # টেম্প ফাইল মুছুন
    try:
        os.remove(video_file)
        console.print("[green]🧹 Temporary file deleted.[/green]")
    except:
        pass

# ---------- ডাইরেক্ট স্ট্রিম (নো ফাইল, নো লুপ) ----------
def stream_from_url_direct(url, stream_key):
    rtmp_url = f"rtmps://a.rtmps.youtube.com:443/live2/{stream_key}"
    console.print("[yellow]⏳ Starting direct streaming (no file saved)... Press CTRL+C to stop.[/yellow]")

    yt_cmd = ["yt-dlp", "-f", "best", "-o", "-", url]
    ffmpeg_cmd = [
        "ffmpeg", "-f", "matroska", "-i", "pipe:0",  # ফরম্যাট স্পেসিফাই করা
        "-c:v", "libx264", "-preset", "ultrafast", "-tune", "zerolatency",
        "-b:v", "2000k", "-maxrate", "2000k", "-bufsize", "6000k",
        "-pix_fmt", "yuv420p", "-g", "60",
        "-c:a", "aac", "-b:a", "128k",
        "-f", "flv", rtmp_url
    ]

    try:
        yt_process = subprocess.Popen(yt_cmd, stdout=subprocess.PIPE, stderr=subprocess.DEVNULL)
        ffmpeg_process = subprocess.Popen(ffmpeg_cmd, stdin=yt_process.stdout,
                                          stdout=subprocess.DEVNULL, stderr=subprocess.PIPE)
        yt_process.stdout.close()
        
        # স্ট্রিমিং মনিটরিং
        while True:
            time.sleep(1)
            if ffmpeg_process.poll() is not None:
                break
                
        yt_process.wait()
        
    except KeyboardInterrupt:
        console.print("\n[yellow]⏹️ Direct stream stopped by user.[/yellow]")
        yt_process.terminate()
        ffmpeg_process.terminate()
    except Exception as e:
        console.print(f"[red]❌ Streaming error: {e}[/red]")
    else:
        if ffmpeg_process.returncode == 0:
            console.print("[green]✅ Direct stream finished successfully.[/green]")
        else:
            console.print("[red]❌ Stream ended with errors.[/red]")

# ---------- রিলে লাইভ স্ট্রিম ----------
def relay_live_stream(stream_url, stream_key):
    rtmp_url = f"rtmps://a.rtmps.youtube.com:443/live2/{stream_key}"
    console.print("[yellow]⏳ Starting relay... Press CTRL+C to stop.[/yellow]")

    yt_cmd = ["yt-dlp", "-f", "best", "-o", "-", stream_url]
    ffmpeg_cmd = [
        "ffmpeg", "-f", "matroska", "-i", "pipe:0",  # ফরম্যাট স্পেসিফাই করা
        "-c:v", "libx264", "-preset", "ultrafast", "-tune", "zerolatency",
        "-b:v", "2000k", "-maxrate", "2000k", "-bufsize", "6000k",
        "-pix_fmt", "yuv420p", "-g", "60",
        "-c:a", "aac", "-b:a", "128k",
        "-f", "flv", rtmp_url
    ]

    try:
        yt_process = subprocess.Popen(yt_cmd, stdout=subprocess.PIPE, stderr=subprocess.DEVNULL)
        ffmpeg_process = subprocess.Popen(ffmpeg_cmd, stdin=yt_process.stdout,
                                          stdout=subprocess.DEVNULL, stderr=subprocess.PIPE)
        yt_process.stdout.close()
        
        # স্ট্রিমিং মনিটরিং
        while True:
            time.sleep(1)
            if ffmpeg_process.poll() is not None:
                break
                
        yt_process.wait()
        
    except KeyboardInterrupt:
        console.print("\n[yellow]⏹️ Relay stopped by user.[/yellow]")
        yt_process.terminate()
        ffmpeg_process.terminate()
    except Exception as e:
        console.print(f"[red]❌ Relay error: {e}[/red]")
    else:
        if ffmpeg_process.returncode == 0:
            console.print("[green]✅ Relay finished successfully.[/green]")
        else:
            console.print("[red]❌ Relay ended with errors.[/red]")

# ---------- স্ট্রিমিং মেনু ----------
def stream_menu():
    console.print("\n[bold cyan]📡 Streaming Options[/bold cyan]")
    console.print("1. Stream from a local video file (with loop option)")
    console.print("2. Stream from YouTube URL (download then stream, with loop, auto-delete)")
    console.print("3. Stream from YouTube URL (direct streaming, no file saved, no loop)")
    console.print("4. Relay an existing YouTube live stream")
    choice = Prompt.ask("[cyan]Your choice[/cyan]", choices=["1","2","3","4"])

    if choice == '1':
        source = get_valid_local_file()
        stream_key = Prompt.ask("[cyan]🔑 Enter your YouTube Stream Key[/cyan]")
        if not stream_key:
            console.print("[red]❌ Stream key missing.[/red]")
            return
        loop_choice = Prompt.ask("[cyan]🔁 Loop video? (y/n, default n)[/cyan]", default="n")
        stream_local_file(source, stream_key, loop_choice)

    elif choice == '2':
        url = Prompt.ask("[cyan]🎬 Enter YouTube video URL[/cyan]")
        if not url:
            console.print("[red]❌ No URL provided.[/red]")
            return
        stream_key = Prompt.ask("[cyan]🔑 Enter your YouTube Stream Key[/cyan]")
        if not stream_key:
            console.print("[red]❌ Stream key missing.[/red]")
            return
        loop_choice = Prompt.ask("[cyan]🔁 Loop video? (y/n, default n)[/cyan]", default="n")
        stream_from_url_download(url, stream_key, loop_choice)

    elif choice == '3':
        url = Prompt.ask("[cyan]🎬 Enter YouTube video URL[/cyan]")
        if not url:
            console.print("[red]❌ No URL provided.[/red]")
            return
        stream_key = Prompt.ask("[cyan]🔑 Enter your YouTube Stream Key[/cyan]")
        if not stream_key:
            console.print("[red]❌ Stream key missing.[/red]")
            return
        stream_from_url_direct(url, stream_key)

    elif choice == '4':
        live_url = Prompt.ask("[cyan]🎥 Enter the YouTube LIVE stream URL to relay[/cyan]")
        if not live_url:
            console.print("[red]❌ No URL provided.[/red]")
            return
        stream_key = Prompt.ask("[cyan]🔑 Enter your YouTube Stream Key[/cyan]")
        if not stream_key:
            console.print("[red]❌ Stream key missing.[/red]")
            return
        relay_live_stream(live_url, stream_key)

# ---------- অ্যাবাউট সেকশন ----------
def show_about():
    console.print(f"\n[bold magenta]📌 About {TOOL_NAME}[/bold magenta]")
    console.print(f"[cyan]Developer:[/cyan] {DEV_NAME}")
    console.print("[cyan]Links:[/cyan]")
    for platform, link in DEV_LINKS.items():
        console.print(f"  {platform}: [green]{link}[/green]")
    console.print("\n[yellow]This tool allows you to download YouTube videos, stream local files, stream YouTube videos directly (without saving), and relay live streams to your YouTube channel.[/yellow]")
    console.print("\n[cyan]Features:[/cyan]")
    console.print("  • Auto-reconnect on network drop")
    console.print("  • Mobile-optimized encoding")
    console.print("  • RTMPS secure streaming")
    console.print("  • Loop streaming support")
    console.print("\n[cyan]Thank you for using! 😊[/cyan]")

# ---------- ব্যানার ও মেইন মেনু ----------
def show_banner():
    os.system('clear')
    console.rule("[bold green]2L YT Live[/bold green]")
    console.print(Panel.fit(
        "[cyan]Developer: NX AL IMRAN S[/cyan]\n[yellow]Powerful YouTube Tool for Termux[/yellow]",
        border_style="blue"
    ))
    console.print(f"[green]✅ Download folder: {DOWNLOAD_DIR}[/green]\n")

def main_menu():
    open_website()
    cleanup_temp_files()  # পুরনো টেম্প ফাইল ক্লিনআপ
    
    while True:
        show_banner()
        console.print("[bold]Main Menu:[/bold]")
        console.print("  [cyan]1.[/cyan] 📥 Download YouTube video")
        console.print("  [cyan]2.[/cyan] 📡 Stream to YouTube Live")
        console.print("  [cyan]3.[/cyan] 🔁 Relay a YouTube Live stream")
        console.print("  [cyan]4.[/cyan] ℹ️  About")
        console.print("  [cyan]5.[/cyan] 🚪 Exit")
        choice = Prompt.ask("\n[yellow]Enter your choice[/yellow]", choices=["1","2","3","4","5"])

        if choice == '1':
            download_video()
            Prompt.ask("[cyan]Press Enter to continue...[/cyan]")
        elif choice == '2':
            stream_menu()
            Prompt.ask("[cyan]Press Enter to continue...[/cyan]")
        elif choice == '3':
            live_url = Prompt.ask("[cyan]🎥 Enter the YouTube LIVE stream URL to relay[/cyan]")
            if not live_url:
                console.print("[red]❌ No URL provided.[/red]")
                Prompt.ask("[cyan]Press Enter...[/cyan]")
                continue
            stream_key = Prompt.ask("[cyan]🔑 Enter your YouTube Stream Key[/cyan]")
            if not stream_key:
                console.print("[red]❌ Stream key missing.[/red]")
                Prompt.ask("[cyan]Press Enter...[/cyan]")
                continue
            relay_live_stream(live_url, stream_key)
            Prompt.ask("[cyan]Press Enter to continue...[/cyan]")
        elif choice == '4':
            show_about()
            Prompt.ask("[cyan]Press Enter to continue...[/cyan]")
        elif choice == '5':
            cleanup_temp_files()
            console.print("[green]👋 Goodbye![/green]")
            sys.exit(0)

# ---------- মূল প্রোগ্রাম ----------
if __name__ == "__main__":
    check_and_install_dependencies()
    setup_storage_and_folder()
    main_menu()
