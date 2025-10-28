import tkinter as tk
import customtkinter as ctk
from pygame import mixer
import math

mixer.init()
mixer.set_num_channels(2)

#========== STYLES ==========#
DEFAULT_FONT = ("CTkFont", 24, "normal")


BACKGROUND_COLOR = "#30342E"
FRAME_COLOR = "#424640"
PLAY_BUTTON_COLOR = "#395B50"
PLAY_BUTTON_HOVER_COLOR = "#2a443c"
STOP_BUTTON_COLOR = "#5A7684"
STOP_BUTTON_HOVER_COLOR = "#40545F"
TEXT_COLOR = "#dcdacd"


#========== PYTHON COMPONENTS ==========#
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


#========== UI FACTORY FUNCTIONS ==========#
def create_transport_button(parent, text, command, color, hover_color, scale_factor=1):
    """
    Factory method for creating a transport control.

    Args:
        parent: the parent tkinter widget
        text: the text to display on the button
        command: the function to call when the button is pressed
        color: the color of the button when it is not being hovered over
        hover_color: the color of the button when it is being hovered over
        scale_factor: the factor to scale the button by (defaults to 1)

    Returns:
        CTkButton: A complete button instance
    """
    font_tuple = (DEFAULT_FONT[0], DEFAULT_FONT[1] * scale_factor, DEFAULT_FONT[2])
    
    button = ctk.CTkButton(
        parent, 
        width=scale_factor * 100, 
        height=scale_factor * 80, 
        text=text, 
        command=command, 
        fg_color=color, 
        text_color=TEXT_COLOR, 
        hover_color=hover_color,
        font=font_tuple
    )
    return button


#========== UI CONSTRUCTION ==========#
root = ctk.CTk(fg_color=BACKGROUND_COLOR)
root.title("ElderHank Soundboard")
root.geometry("800x400")

#~~~GLOBAL TRANSPORT BAR~~~#
transport_bar = ctk.CTkFrame(root, width=400, fg_color=FRAME_COLOR)
transport_bar.pack(side=ctk.BOTTOM, expand=True)

transport_bar_label = ctk.CTkLabel(transport_bar, text="Global Controls")
transport_bar_label.pack(side=ctk.TOP, pady=5)

stop_button = create_transport_button(transport_bar, "Stop", lambda: mixer.stop(), STOP_BUTTON_COLOR, STOP_BUTTON_HOVER_COLOR)
stop_button.pack(side=ctk.RIGHT, padx=5, pady=5, expand=True)

# TODO: Make global play button start both music and ambience channels
play_button = create_transport_button(transport_bar, "Play", lambda: music.play('./data/music/skyrim_awake.wav'), PLAY_BUTTON_COLOR, PLAY_BUTTON_HOVER_COLOR)
play_button.pack(side=ctk.LEFT, padx=5, pady=5, expand=True)

#~~~MUSIC TRACK~~~#
music_track = ctk.CTkFrame(root, fg_color=FRAME_COLOR)
music_track.pack(side=ctk.LEFT, padx=5, pady=5, expand=True)

music_transport_bar = ctk.CTkFrame(music_track, fg_color=FRAME_COLOR)
music_transport_bar.pack(side=ctk.BOTTOM, fill=ctk.X)

music_stop_button = create_transport_button(music_transport_bar, "Stop", lambda: music.stop(), STOP_BUTTON_COLOR, STOP_BUTTON_HOVER_COLOR, 0.6)
music_stop_button.pack(side=ctk.RIGHT, padx=5, pady=5, expand=True)

music_play_button = create_transport_button(music_transport_bar, "Play", lambda: music.play('./data/music/skyrim_awake.wav'), PLAY_BUTTON_COLOR, PLAY_BUTTON_HOVER_COLOR, 0.6)
music_play_button.pack(side=ctk.BOTTOM, padx=5, pady=5, expand=True)


music_volume_label = ctk.CTkLabel(music_track, text="100%")
music_volume_label.pack(side=ctk.BOTTOM, pady=5)

def set_music_volume(new_volume):
    """
    
    """
    numeric_volume = round(float(new_volume))
    music_volume_label.configure(text=f"{numeric_volume}%")
    music.set_volume(numeric_volume * 0.01)

music_volume = ctk.CTkSlider(music_track, from_=0, to=100, command=set_music_volume, orientation=ctk.VERTICAL)
music_volume.set(100)
music_volume.pack(fill=ctk.Y, padx=5, pady=5)


root.mainloop()