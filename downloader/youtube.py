from yt_dlp import YoutubeDL


def download_video(url: str, output_dir: str = 'downloads'):
    """Download a YouTube video or Twitch VOD locally."""
    ydl_opts = {
        'outtmpl': f'{output_dir}/%(title)s.%(ext)s',
        'format': 'bestvideo+bestaudio/best',
        'merge_output_format': 'mp4'
    }

    with YoutubeDL(ydl_opts) as ydl:
        info = ydl.extract_info(url, download=True)
        return ydl.prepare_filename(info)
