import os

# চ্যানেল লিস্ট ফাইল ওপেন করা
try:
    with open('youtube_channels.txt', 'r') as f:
        urls = [line.strip() for line in f if line.strip()]
except FileNotFoundError:
    urls = ["https://www.youtube.com/channel/UC2HXZuHFLddZib4gDl1m6cA/live"]

m3u8_content = "#EXTM3U\n"

for url in urls:
    # চ্যানেল আইডি বের করা
    if "channel/" in url:
        channel_id = url.split("channel/")[1].split("/")[0]
        name = f"YouTube Live ({channel_id[:5]})"
        
        # আমরা সরাসরি YouTube এর 'live' এন্ডপয়েন্ট ব্যবহার করছি যা আধুনিক প্লেয়ার সাপোর্ট করে
        m3u8_content += f'#EXTINF:-1 tvg-id="{channel_id}" group-title="YouTube Live", {name}\n'
        m3u8_content += f'https://www.youtube.com/channel/{channel_id}/live\n'
    
    elif "watch?v=" in url:
        video_id = url.split("watch?v=")[1].split("&")[0]
        m3u8_content += f'#EXTINF:-1, YouTube Video {video_id}\n'
        m3u8_content += f'https://www.youtube.com/watch?v={video_id}\n'

# প্লেলিস্ট ফাইল সেভ করা
with open('live_playlist.m3u8', 'w', encoding='utf-8') as f:
    f.write(m3u8_content)

print("live_playlist.m3u8 file created successfully!")
