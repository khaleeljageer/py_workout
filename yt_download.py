from pytube import YouTube
from moviepy.editor import *


def download_youtube_audio(video_url, out_path):
    try:
        # Step 1: Fetch the YouTube video using pytube
        yt = YouTube(video_url)

        # Step 2: Select the highest quality audio stream available
        audio_stream = yt.streams.filter(only_audio=True).first()

        # Step 3: Download the audio stream
        print("Downloading audio...")
        file_name = audio_stream.title
        audio_stream.download()

        # Step 4: Convert the downloaded video to audio
        video_path = audio_stream.default_filename
        audio_path = os.path.join(out_path, file_name + '.mp3')
        video_clip = VideoFileClip(video_path)

        # Explicitly set the fps to avoid the 'video_fps' error
        fps = video_clip.fps if video_clip.fps else 44100

        audio_clip = video_clip.audio
        audio_clip.write_audiofile(audio_path, fps=fps)

        # Step 5: Close the video clip and remove the temporary video file
        audio_clip.close()
        video_clip.close()
        os.remove(video_path)

        print("Audio downloaded and saved as:", audio_path)

    except Exception as e:
        print("Error:", str(e))


def get_urls():
    with open("unique_urls.txt", 'r') as f:
        lines = f.readlines()
        f.close()
    return lines


def main():
    youtube_video_urls = get_urls()
    output_path = 'videos/'
    for yt_url in youtube_video_urls:
        download_youtube_audio(yt_url, output_path)


if __name__ == "__main__":
    main()
