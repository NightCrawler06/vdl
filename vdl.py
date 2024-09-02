#A Simple Video Downloader (°-°)

import yt_dlp

def download_video(url, output_path='downloads', format_code=None):
    ydl_opts = {
        'format': format_code if format_code else 'bestvideo+bestaudio/best',
        'outtmpl': f'{output_path}/%(title)s.%(ext)s',
        'merge_output_format': 'mp4',
    }
    
    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        ydl.download([url])

if __name__ == "__main__":
    video_url = input("Enter the video URL: ")
    format_code = input("Enter the format code (leave blank for best): ")
    download_video(video_url, format_code=format_code)
    print("Download complete.")
