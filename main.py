from moviepy.editor import ImageClip, AudioFileClip, CompositeVideoClip, TextClip
import pandas as pd
import os

def create_video_with_subtitles(image_path, audio_path, subtitle_path, output_path):
    # Load the audio file
    audio_clip = AudioFileClip(audio_path)
    
    # Calculate the resolution for 9:16 aspect ratio
    # Setting width to 1080 pixels for HD video
    width = 1080
    height = int(width * 16 / 9)
    
    # Load the image, resize it to maintain 9:16 aspect ratio, and set duration
    video_clip = ImageClip(image_path).resize(newsize=(width, height)).set_duration(audio_clip.duration + 2)

    # Set the audio of the video clip
    video_clip = video_clip.set_audio(audio_clip)
    
    # Read subtitles from the Excel file
    df = pd.read_excel(subtitle_path)
    # Assuming the Excel file has columns 'start', 'end', and 'text' for subtitles
    subtitles = []
    for index, row in df.iterrows():
        # Create a TextClip for each subtitle
        subtitle_clip = TextClip(row['text'], fontsize=24, color='white', size=video_clip.size)
        subtitle_clip = subtitle_clip.set_position('bottom').set_duration(row['end'] - row['start']).set_start(row['start'])
        subtitles.append(subtitle_clip)
    
    # Overlay the subtitles on the video
    video_with_subs = CompositeVideoClip([video_clip] + subtitles)
    
    # Create a composite video clip (useful if you need to layer more clips)
    final_clip = CompositeVideoClip([video_with_subs])
    
    # Write the final video file to disk
    final_clip.write_videofile(output_path, codec='libx264', fps=24)

# Example usage:
create_video_with_subtitles(
    f"{os.getcwd()}\use_image_here.jpg",
    f"{os.getcwd()}\use_audio_here.mp3",
    f"{os.getcwd()}\paste_subtitle_here.xlsx",
    f"{os.getcwd()}\output.mp4"
)
