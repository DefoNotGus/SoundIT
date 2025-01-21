# GUSTAVO R
# 01/01/2025

import os
from tkinter import Tk, filedialog, Button, Label, messagebox
from moviepy import VideoFileClip

# Function to select a video file and extract its audio
def select_file():
    # Open a file dialog to select the video file
    filepath = filedialog.askopenfilename(
        title="Select a video file",
        filetypes=[("Video files", "*.mp4 *.avi *.mov *.mkv *.flv *.wmv *.m4v")])  # Add more video formats if needed

    if filepath:
        try:
            # Try opening the file as a video using moviepy
            video = VideoFileClip(filepath)

            # Detach audio and save it as mp3
            audio = video.audio
            output_path = os.path.splitext(filepath)[0] + ".mp3"
            audio.write_audiofile(output_path)

            # Success message
            messagebox.showinfo("Success", f"Audio saved as: {output_path}")
        except Exception as e:
            # Error message for non-video files or other issues
            messagebox.showerror("Error", f"Failed to process file. Make sure it's a valid video.\n{str(e)}")
    else:
        messagebox.showwarning("No file selected", "Please select a video file.")

# Create the main GUI window
window = Tk()
window.title("Video to MP3 Converter")
window.geometry("300x150")  # Set window size

# Add a label
label = Label(window, text="Choose a video file to extract audio")
label.pack(pady=10)

# Add a button to open the file dialog
select_button = Button(window, text="Select Video", command=select_file)
select_button.pack(pady=20)

# Start the GUI event loop
window.mainloop()
