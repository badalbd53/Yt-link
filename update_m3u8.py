import os

# চ্যানেল লিস্ট ফাইল
try:
    with open('youtube_channels.txt', 'r') as f:
        urls = [line.strip() for line in f if line.strip()]
except FileNotFoundError:
    urls = ["https://www.youtube.com/channel/UC2HXZuHFLddZib4gDl1m6cA/live"]

m3u8_content = "#EXTM3U\n"

for url in urls:
    if "channel/" in url:
        channel_id = url.split("channel/")[1].split("/")[0]
        name = "Somoy TV" # আপনি আপনার চ্যানেলের নাম এখানে লিখতে পারেন
        
        # আমরা একটি পাবলিক ইউটিউব প্রক্সি ব্যবহার করছি যা লিঙ্কটিকে OTT Navigator এর উপযোগী করবে
        # এই লিঙ্কটি সরাসরি .m3u8 হিসেবে কাজ করবে
        proxy_url = f"https://youtube-proxy.lib.codetabs.com/video/{channel_id}" 
        # অথবা নিচের ফরম্যাটটি ট্রাই করুন (সবচেয়ে জনপ্রিয়):
        final_link = f"https://www.youtube.com/channel/{channel_id}/live"
        
        # OTT Navigator এর জন্য সরাসরি কাজ করার মতো লিঙ্ক:
        stream_link = f"https://pwn.sh/tools/get_video_url.php?url={final_link}"
        
        m3u8_content += f'#EXTINF:-1 tvg-id="{channel_id}" tvg-logo="" group-title="YouTube Live", {name}\n'
        m3u8_content += f'{stream_link}\n'

with open('live_playlist.m3u8', 'w', encoding='utf-8') as f:
    f.write(m3u8_content)

print("OTT Navigator compatible playlist created!")
