from Tone import Tone
from Note import Note
import numpy as np
# Tone.sine(440, duration = 1, amp=0.2)
# Tone.sine(440, duration = 1, amp=0.8)
# # Tone.sine(200, duration= 0.5)

# # #C major scale
# notes_list = [
#     "C4",
#     "D4",
#     "E4",
#     "F4",
#     "G4",
#     "A4",
#     "B4",
#     "C5"
# ]

# volume = [1,0.8,0.3,0.5,0.6,0.7,1,0.3]

# # #twinkle twinkle little star
notes_list = [
    "C4", "C4", "G4", "G4", "A4", "A4", "G4",
    "F4", "F4", "E4", "E4", "D4", "D4", "C4",
    "G4", "G4", "F4", "F4", "E4", "E4", "D4",
    "G4", "G4", "F4", "F4", "E4", "E4", "D4",
    "C4", "C4", "G4", "G4", "A4", "A4", "G4",
    "F4", "F4", "E4", "E4", "D4", "D4", "C4"
]

volume = np.linspace(0.1, 1, 42)
#volume = np.ones(42)

for note,volume in zip(notes_list, volume):
    Note(note, volume,duration=0.5).play()