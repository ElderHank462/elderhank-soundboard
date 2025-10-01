import tkinter
from pygame import mixer

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

root = tkinter.Tk()
root.title("ElderHank Soundboard")
root.geometry("400x200")
root.configure(bg="#1f2f16")

transport_bar = tkinter.Frame(root)
transport_bar.pack(side=tkinter.BOTTOM, fill=tkinter.X, pady=10)

play_frame = tkinter.Frame(transport_bar)
play_frame.pack(side=tkinter.LEFT, padx=5, pady=5, expand=True)

# label creation
test_label = tkinter.Label(play_frame, text="Active")
test_label.pack(side=tkinter.TOP, pady=5)

play_button = tkinter.Button(play_frame, text="Play Ambience", command=lambda: play_sound('../data/music/skyrim_awake.wav'))
play_button.pack(side=tkinter.BOTTOM, padx=5, pady=5, expand=True)

stop_button = tkinter.Button(transport_bar, text="Stop", command=stop_sound)
stop_button.pack(side=tkinter.RIGHT, padx=5, pady=5, expand=True)

root.mainloop()
