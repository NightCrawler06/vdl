#A Simple Video Downloader (°-°)

import yt_dlp

def download_video(url, output_path='downloads', file_name=None, format_code=None):
    ydl_opts = {
        'format': format_code if format_code else 'bestvideo+bestaudio/best',
        'outtmpl': f'{output_path}/{file_name}.%(ext)s' if file_name else f'{output_path}/%(title)s.%(ext)s',
        'merge_output_format': 'mp4',
    }
    
    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        ydl.download([url])

if __name__ == "__main__":
    video_url = input("Enter the video URL: ")
    file_name = input("Enter the name to save the file as: ") or None
    download_video(video_url, file_name=file_name)
    print("Download complete.")
