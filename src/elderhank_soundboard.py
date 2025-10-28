import tkinter as tk
import customtkinter as ctk
from pygame import mixer

mixer.init()
mixer.set_num_channels(2)

class MusicTrack:
    """
    
    """
    def __init__(self):
        pass

    def play(self, sound_file):
        """Plays a specified sound file."""
        try:
            mixer.music.load(sound_file)
            mixer.music.play()
        except Exception as e:
            print(f"Error playing sound: {e}")

    def stop(self):
        """Stops the currently playing sound."""
        mixer.music.stop()

    def set_volume(self, new_volume):
        """

        """
        float_volume = float(new_volume)
        mixer.music.set_volume(float_volume)

music = MusicTrack()

#==========UI==========#
root = ctk.CTk()
root.title("ElderHank Soundboard")
root.geometry("400x200")

#~~~TRANSPORT BAR~~~#
transport_bar = ctk.CTkFrame(root)
transport_bar.pack(side=ctk.BOTTOM, fill=ctk.X, pady=10)

stop_button = ctk.CTkButton(transport_bar, text="Stop", command=lambda: music.stop())
stop_button.pack(side=ctk.RIGHT, padx=5, pady=5, expand=True)

play_frame = ctk.CTkFrame(transport_bar)
play_frame.pack(side=ctk.LEFT, padx=5, pady=5, expand=True)

play_button = ctk.CTkButton(play_frame, text="Play Ambience", command=lambda: music.play('./data/music/skyrim_awake.wav'))
play_button.pack(side=ctk.BOTTOM, padx=5, pady=5, expand=True)

#~~~MUSIC TRACK~~~#
music_track = ctk.CTkFrame(root)
music_track.pack(side=ctk.LEFT, padx=5, pady=5, expand=True)

music_volume_label = ctk.CTkLabel(music_track, text="100%")
music_volume_label.pack(side=ctk.BOTTOM, pady=5)

def set_music_volume(new_volume):
    """
    
    """
    numeric_volume = round(float(new_volume))
    music_volume_label.configure(text=f"{numeric_volume}%")
    music.set_volume(numeric_volume * 0.01)


music_volume = ctk.CTkSlider(music_track, from_=100, to=0, command=set_music_volume)
music_volume.set(100)
music_volume.pack(fill=ctk.Y, padx=5, pady=5)


root.mainloop()