from moviepy.editor import VideoFileClip
import imageio

def video_to_gif(video_path, gif_path, plugin='ffmpeg'):
    # Load the video file
    clip = VideoFileClip(video_path)
    # Write the video frames to a GIF file using imageio
    with imageio.get_writer(gif_path, mode='I', plugin='DICOM') as writer:
        for frame in clip.iter_frames():
            writer.append_data(frame)

def images_to_gif(image_folder, gif_path, duration=500):
    from PIL import Image
    import os
    # Load the images
    images = [Image.open(os.path.join(image_folder, file)) for file in sorted(os.listdir(image_folder)) if file.endswith(('png', 'jpg', 'jpeg'))]
    # Convert the images to a GIF
    images[0].save(gif_path, save_all=True, append_images=images[1:], duration=duration, loop=0)

def main():
    choice = input("Enter '1' to create GIF from video or '2' to create GIF from images: ")
    if choice == '1':
        video_path = input("Enter the path to the video file: ")
        gif_path = input("Enter the path to save the GIF file: ")
        plugin = input("Enter the plugin to use for imageio (default is 'ffmpeg'): ") or 'ffmpeg'
        video_to_gif(video_path, gif_path, plugin)
    elif choice == '2':
        image_folder = input("Enter the path to the folder containing images: ")
        gif_path = input("Enter the path to save the GIF file: ")
        duration = int(input("Enter the duration for each frame in milliseconds (default is 500): ") or 500)
        images_to_gif(image_folder, gif_path, duration)
    else:
        print("Invalid choice. Please enter '1' or '2'.")

if __name__ == "__main__":
    main()