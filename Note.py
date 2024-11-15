from utils import NOTE_MAP
from Tone import Tone

class Note:
    def __init__(self, note_str, volume, duration = 1):
        main_note = note_str[0].upper() #convert first letter to uppercase
        self.note_str = main_note + note_str[1:]
        self.duration = duration
        self.freq = NOTE_MAP[self.note_str]
        self.volume = volume
        
        
    def play(self, speaker = None):
        Tone.sine(self.freq, duration=self.duration, amp=self.volume, speaker=speaker)