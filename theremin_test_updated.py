import serial
import time
from Tone import Tone
from Note import Note

arduino_port = 'COM5'
baud_rate = 9600

# Initialize
ser = serial.Serial(arduino_port, baud_rate, timeout=3)
time.sleep(2)  # give some time for the connection to establish

ser.flushInput() #clear the buffer

notes = [
    ("C4", 5, 7.5),
    ("D4", 7.5, 10),
    ("E4", 10, 12.5),
    ("F4", 12.5, 15),
    ("G4", 15, 17.5),
    ("A4", 17.5, 20),
    ("B4", 20, 22.5),
    ("C5", 22.5, 25)
]

volumes = [
    (0.2, 5, 7.5),
    (0.3, 7.5, 10),
    (0.4, 10, 12.5),
    (0.5, 12.5, 15),
    (0.6, 15, 17.5),
    (0.7, 17.5, 20),
    (0.8, 20, 22.5),
    (0.9, 22.5, 25)
]


# function to map distance to a note
def map_distance_to_note(distance):
    for note, min_dist, max_dist in notes:
        if min_dist <= distance <= max_dist:
            return note
    return None  # Return None if the distance is outside the expected range

def map_distance_to_volume(distance):
    for amp, min_dist, max_dist in volumes:
        if min_dist <= distance <= max_dist:
            return amp
    return None

values_freq = [5]
values_amp = [1]
dist1 = 0
dist2 = 0
#reading data
try:
    while True:
        # Read a line from the serial port (decode from bytes to string)
        if ser.in_waiting > 0:
            data = ser.readline().decode('ISO-8859-1').strip()
            if data.split() == []:
                pass
            
            else:
                rawlist = data.split()
                print(len(rawlist), rawlist)
                try:
                    dist1 = int(rawlist[0])
                    dist2 = int(rawlist[1])
                except:
                    dist1 = 6
                    dist2 = 24
                    
                if 5 <= dist1 <=25:
                        values_freq.append(dist1)
                else:
                    values_freq.append(values_freq[-1])
                    
                if 5 <= dist2 <=25:
                        values_amp.append(dist2)
                else:
                    values_amp.append(values_amp[-1])
            
                
                note = map_distance_to_note(values_freq[-1])
                amp = map_distance_to_volume(values_amp[-1])
                Note(note,amp,duration=0.3).play()
                print((note, dist1), (amp, dist2))
        time.sleep(0.001)
                
except KeyboardInterrupt:
    print("Program stopped.")
    print(values_freq)
finally:
    ser.close()  
    