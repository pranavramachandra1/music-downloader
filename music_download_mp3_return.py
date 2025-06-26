import os
import tempfile
import yt_dlp as youtube_dl
from zipfile import ZipFile

def download_audio_with_mp3(youtube_link):
    # Create a temporary directory for processing
    with tempfile.TemporaryDirectory() as temp_dir:
        ydl_opts = {
            'format': 'bestaudio/best',
            'outtmpl': os.path.join(temp_dir, '%(title)s.%(ext)s'),
            'postprocessors': [{
                'key': 'FFmpegExtractAudio',
                'preferredcodec': 'mp3',
                'preferredquality': '192',
                'nopostoverwrites': False
            }],
        }
        
        try:
            with youtube_dl.YoutubeDL(ydl_opts) as ydl:
                # Extract info to get the filename that will be created
                info = ydl.extract_info(youtube_link, download=False)
                
                # Download the file to temp directory
                ydl.download([youtube_link])

                # Check if 'entries' key exists (playlist detection)
                if info.get('entries', None):
                    # Create zip file path
                    zip_filename = 'playlist_archive.zip'
                    zip_path = os.path.join(temp_dir, zip_filename)
                    
                    # Create zip archive of all MP3 files
                    with ZipFile(zip_path, 'w') as zipf:
                        for root, _, files in os.walk(temp_dir):
                            for file in files:
                                if file.endswith('.mp3'):
                                    file_path = os.path.join(root, file)
                                    zipf.write(file_path, file)
                    
                    # Read zip file content
                    with open(zip_path, 'rb') as f:
                        zip_data = f.read()
                    
                    return {
                        'data': zip_data,
                        'title': info.get('title', 'Unknown'),
                        'filename': zip_filename
                    }
                
                else:
                    # Single video processing
                    filename = ydl.prepare_filename(info)
                    mp3_filename = os.path.splitext(filename)[0] + '.mp3'
                    
                    # Read MP3 file content
                    with open(mp3_filename, 'rb') as f:
                        mp3_data = f.read()
                    
                    return {
                        'data': mp3_data,
                        'title': info.get('title', 'Unknown'),
                        'filename': os.path.basename(mp3_filename)
                    }
                
        except Exception as e:
            return {'error': f"An error occurred: {e}"}
