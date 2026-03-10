import os
import subprocess

# চ্যানেল লিস্ট ফাইল ওপেন করা
with open('youtube_channels.txt', 'r') as f:
    urls = f.readlines()

m3u8_content = "#EXTM3U\n"

for url in urls:
    url = url.strip()
    if not url: continue
    
    try:
        # yt-dlp ব্যবহার করে মেনিফেস্ট লিঙ্ক বের করা
        cmd = f'yt-dlp -g -f "best[ext=mp4]" {url}'
        stream_url = subprocess.check_output(cmd, shell=True).decode('utf-8').strip()
        
        # চ্যানেলের নাম বা আইডি যোগ করা
        m3u8_content += f"#EXTINF:-1, YouTube Live\n{stream_url}\n"
    except:
        print(f"Error getting link for {url}")

# প্লেলিস্ট ফাইল সেভ করা
with open('live_playlist.m3u8', 'w') as f:
    f.write(m3u8_content)
