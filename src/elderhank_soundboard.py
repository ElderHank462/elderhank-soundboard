import tkinter as tk
from pygame import mixer


class Track:
    # FIELDS
    #
    test_var = "test"


mixer.init()

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

root = tk.Tk()
root.title("ElderHank Soundboard")
root.geometry("400x200")

transport_bar = tk.Frame(root)
transport_bar.pack(side=tk.BOTTOM, fill=tk.X, pady=10)

play_frame = tk.Frame(transport_bar)
play_frame.pack(side=tk.LEFT, padx=5, pady=5, expand=True)

# label creation
test_label = tk.Label(play_frame, text="Active")
test_label.pack(side=tk.TOP, pady=5)

play_button = tk.Button(play_frame, text="Play Ambience", command=lambda: play_sound('../data/music/skyrim_awake.wav'))
play_button.pack(side=tk.BOTTOM, padx=5, pady=5, expand=True)

stop_button = tk.Button(transport_bar, text="Stop", command=stop_sound)
stop_button.pack(side=tk.RIGHT, padx=5, pady=5, expand=True)

root.mainloop()
