import subprocess

youtube_url = "https://www.youtube.com/watch?v=VIDEO_ID"

cmd = ["yt-dlp", "-g", youtube_url]

result = subprocess.run(cmd, capture_output=True, text=True)

m3u8_link = result.stdout.strip()

with open("stream.m3u8", "w") as f:
    f.write("#EXTM3U\n")
    f.write("#EXTINF:-1,YouTube Live\n")
    f.write(m3u8_link)
