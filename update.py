import subprocess

channels = open("channels.txt").read().splitlines()

playlist = "#EXTM3U\n"

for ch in channels:
    try:
        link = subprocess.check_output(
            ["yt-dlp", "-g", ch]
        ).decode().strip()

        playlist += f"#EXTINF:-1,{ch}\n{link}\n"

    except:
        pass

open("playlist.m3u8","w").write(playlist)
