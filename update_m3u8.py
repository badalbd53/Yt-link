import os
import subprocess

# চ্যানেল লিস্ট ফাইল ওপেন করা
try:
    with open('youtube_channels.txt', 'r') as f:
        urls = [line.strip() for line in f if line.strip()]
except FileNotFoundError:
    print("Error: youtube_channels.txt file not found!")
    urls = []

m3u8_content = "#EXTM3U\n"

for url in urls:
    print(f"Processing: {url}")
    try:
        # yt-dlp ব্যবহার করে মেনিফেস্ট লিঙ্ক বের করা
        # --get-url ব্যবহার করা হয়েছে সরাসরি লিঙ্ক পাওয়ার জন্য
        cmd = f'yt-dlp --get-url --format "best[ext=mp4]/best" "{url}"'
        stream_url = subprocess.check_output(cmd, shell=True).decode('utf-8').strip()
        
        if stream_url:
            # এখানে আমরা চ্যানেলের নামটাও অটোমেটিক নেওয়ার চেষ্টা করছি
            name_cmd = f'yt-dlp --get-filename -o "%(title)s" "{url}"'
            channel_name = subprocess.check_output(name_cmd, shell=True).decode('utf-8').strip()
            
            m3u8_content += f"#EXTINF:-1, {channel_name}\n{stream_url}\n"
            print(f"Success: Found link for {channel_name}")
        else:
            print(f"Failed: No link found for {url}")
            
    except Exception as e:
        print(f"Error processing {url}: {e}")

# প্লেলিস্ট ফাইল সেভ করা
with open('live_playlist.m3u8', 'w', encoding='utf-8') as f:
    f.write(m3u8_content)
print("Playlist updated successfully!")
