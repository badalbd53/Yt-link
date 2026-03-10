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
        # --get-url এর সাথে --no-playlist এবং -g ব্যবহার করা হয়েছে
        # এটি লাইভ স্ট্রিমের m3u8 লিঙ্ক সরাসরি বের করবে
        cmd = f'yt-dlp -g -f "best" --no-playlist "{url}"'
        stream_url = subprocess.check_output(cmd, shell=True).decode('utf-8').strip()
        
        if "googlevideo.com" in stream_url:
            # ভিডিওর টাইটেল নেওয়া
            name_cmd = f'yt-dlp --get-title --no-playlist "{url}"'
            channel_name = subprocess.check_output(name_cmd, shell=True).decode('utf-8').strip()
            
            m3u8_content += f"#EXTINF:-1, {channel_name}\n{stream_url}\n"
            print(f"Success: Found link for {channel_name}")
        else:
            print(f"Wait: Stream URL doesn't look like a direct link for {url}")
            
    except Exception as e:
        print(f"Error processing {url}: {e}")

# প্লেলিস্ট ফাইল সেভ করা
with open('live_playlist.m3u8', 'w', encoding='utf-8') as f:
    f.write(m3u8_content)

print("\n--- Final Playlist Content ---")
print(m3u8_content)
