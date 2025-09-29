import tkinter as tk
from pygame import mixer

# Initialize the pygame mixer
mixer.init()

# Define functions for sound playback
def play_sound(sound_file):
    """Plays a specified sound file."""
    try:
        mixer.music.load(sound_file)
        mixer.music.play()
    except Exception as e:
        print(f"Error playing sound: {e}")

def stop_sound():
    """Stops the currently playing sound."""
    mixer.music.stop()

# Set up the Tkinter GUI
root = tk.Tk()
root.title("Simple Soundboard")
root.geometry("300x150")

# Create a button to play a sound
# Replace 'path/to/your/soundfile.mp3' with the actual path to your sound file
play_button = tk.Button(root, text="Play Ambience", command=lambda: play_sound('/Users/henryallen/Music/Logic/Wynatia/Sketches'))
play_button.pack(pady=10)

# Create a button to stop the sound
stop_button = tk.Button(root, text="Stop", command=stop_sound)
stop_button.pack(pady=10)

# Run the application
root.mainloop()
