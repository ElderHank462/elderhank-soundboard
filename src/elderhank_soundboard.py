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


#========== GLOBAL FUNCTIONS ==========#
def stop_all():
    mixer.stop()
    mixer.music.stop()


#========== PYTHON COMPONENTS ==========#
class TransportBar:
    """
    
    """
    def __init__(self, master_widget, label_text, play_command, stop_command, scale_factor=1):
        self.master_widget = master_widget
        
        self.transport_bar = ctk.CTkFrame(self.master_widget, width=400, fg_color=FRAME_COLOR)
        self.transport_bar.pack(side=ctk.BOTTOM, expand=True)

        self.transport_bar_label = ctk.CTkLabel(self.transport_bar, text=label_text, text_color=TEXT_COLOR)
        self.transport_bar_label.pack(side=ctk.TOP, pady=5)

        self.stop_button = create_transport_button(self.transport_bar, "Stop", stop_command, STOP_BUTTON_COLOR, STOP_BUTTON_HOVER_COLOR, scale_factor)
        self.stop_button.pack(side=ctk.RIGHT, padx=5, pady=5, expand=True)

        # TODO: Make global play button start both music and ambience channels
        self.play_button = create_transport_button(self.transport_bar, "Play", play_command, PLAY_BUTTON_COLOR, PLAY_BUTTON_HOVER_COLOR, scale_factor)
        self.play_button.pack(side=ctk.LEFT, padx=5, pady=5, expand=True)

class MusicTrack:
    """
    The music track for the soundboard, containing the track UI and methods to control playback.
    """
    def __init__(self, master_widget):
        self.master_widget = master_widget
        self.music_track = ctk.CTkFrame(self.master_widget, fg_color=FRAME_COLOR)
        self.music_track.pack(side=ctk.LEFT, padx=5, pady=5, expand=True)

        self.music_transport_bar = TransportBar(self.music_track, "Music", lambda: self.play('./data/music/skyrim_awake.wav'), lambda: self.stop(), 0.6)
        self.music_transport_bar.transport_bar.pack(side=ctk.BOTTOM, fill=ctk.X)


        self.music_volume_label = ctk.CTkLabel(self.music_track, text="100%", text_color=TEXT_COLOR)
        self.music_volume_label.pack(side=ctk.BOTTOM, pady=5)

        self.music_volume = ctk.CTkSlider(self.music_track, from_=0, to=100, command=self.set_volume, orientation=ctk.VERTICAL)
        self.music_volume.set(100)
        self.music_volume.pack(fill=ctk.Y, padx=5, pady=5)


    def play(self, sound_file):
        """
        Plays a specified sound file.
        
        Args:
            sound_file: the path to a sound file
        """
        try:
            mixer.music.load(sound_file)
            mixer.music.play()
        except Exception as e:
            print(f"Error playing sound: {e}")

    def stop(self):
        """Stops the music that is playing currently."""
        mixer.music.stop()

    def set_volume(self, new_volume):
        """
        Set the volume of the music in the mixer and update the UI.

        Args:
            new_volume: the new volume to set
        """
        numeric_volume = round(float(new_volume))
        self.music_volume_label.configure(text=f"{numeric_volume}%")
        mixer.music.set_volume(numeric_volume * 0.01)


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
global_transport = TransportBar(root, "Global Controls", lambda: music_track.play('./data/music/skyrim_awake.wav'), lambda: stop_all())

# transport_bar = ctk.CTkFrame(root, width=400, fg_color=FRAME_COLOR)
# transport_bar.pack(side=ctk.BOTTOM, expand=True)

# transport_bar_label = ctk.CTkLabel(transport_bar, text="Global Controls", text_color=TEXT_COLOR)
# transport_bar_label.pack(side=ctk.TOP, pady=5)

# stop_button = create_transport_button(transport_bar, "Stop", lambda: mixer.stop(), STOP_BUTTON_COLOR, STOP_BUTTON_HOVER_COLOR)
# stop_button.pack(side=ctk.RIGHT, padx=5, pady=5, expand=True)

# # TODO: Make global play button start both music and ambience channels
# play_button = create_transport_button(transport_bar, "Play", lambda: music.play('./data/music/skyrim_awake.wav'), PLAY_BUTTON_COLOR, PLAY_BUTTON_HOVER_COLOR)
# play_button.pack(side=ctk.LEFT, padx=5, pady=5, expand=True)

#~~~MUSIC TRACK~~~#
music_track = MusicTrack(root)



root.mainloop()