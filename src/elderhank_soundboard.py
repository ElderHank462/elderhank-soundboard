import tkinter
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
root = tkinter.Tk()
root.title("ElderHank Soundboard")
root.geometry("400x200")

transport_bar = tkinter.Frame(root)
transport_bar.pack(side=tkinter.BOTTOM, fill=tkinter.X, pady=10)

# Create a button to play a sound
# Replace 'path/to/your/soundfile.mp3' with the actual path to your sound file
play_button = tkinter.Button(transport_bar, text="Play Ambience", command=lambda: play_sound('../data/music/skyrim_awake.wav'))
play_button.pack(side=tkinter.LEFT, padx=5, pady=5, expand=True)

# Create a button to stop the sound
stop_button = tkinter.Button(transport_bar, text="Stop", command=stop_sound)
stop_button.pack(side=tkinter.RIGHT, padx=5, pady=5, expand=True)

# Run the application
root.mainloop()
