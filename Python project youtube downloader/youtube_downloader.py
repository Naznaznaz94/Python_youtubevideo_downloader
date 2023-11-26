
from pytube import YouTube

def download_video(url, output_path='.'):
    try:
        # Create a YouTube object
        yt = YouTube(url)

        # Get the highest resolution stream available
        video_stream = yt.streams.get_highest_resolution()

        # Download the video to the specified output path
        video_stream.download(output_path)

        print("Download successful!")

    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    # Get the YouTube video URL from the user
    video_url = input("Enter the YouTube video URL: ")

    # Get the output path from the user (optional, defaults to current directory)
    output_path = input("Enter the output path (press Enter for current directory): ") or '.'

    # Call the download_video function
    download_video(video_url, output_path)