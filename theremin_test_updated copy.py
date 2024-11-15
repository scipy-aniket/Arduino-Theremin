import serial
import time
from Tone import Tone
from Note import Note

arduino_port = 'COM5'
baud_rate = 9600

# Initialize
ser = serial.Serial(arduino_port, baud_rate, timeout=3)

time.sleep(2)  # give some time for the connection to establish

ser.flushInput()  # clear the buffer

min_distance = 5
max_distance = 25
interval = (max_distance - min_distance) / 8


notes = [
    ("C4", min_distance + 0 * interval, min_distance + 1 * interval),
    ("D4", min_distance + 1 * interval, min_distance + 2 * interval),
    ("E4", min_distance + 2 * interval, min_distance + 3 * interval),
    ("F4", min_distance + 3 * interval, min_distance + 4 * interval),
    ("G4", min_distance + 4 * interval, min_distance + 5 * interval),
    ("A4", min_distance + 5 * interval, min_distance + 6 * interval),
    ("B4", min_distance + 6 * interval, min_distance + 7 * interval),
    ("C5", min_distance + 7 * interval, min_distance + 8 * interval)
]

volumes = [
    (0.2, min_distance + 0 * interval, min_distance + 1 * interval),
    (0.2, min_distance + 1 * interval, min_distance + 2 * interval),
    (0.4, min_distance + 2 * interval, min_distance + 3 * interval),
    (0.4, min_distance + 3 * interval, min_distance + 4 * interval),
    (0.6, min_distance + 4 * interval, min_distance + 5 * interval),
    (0.6, min_distance + 5 * interval, min_distance + 6 * interval),
    (0.8, min_distance + 6 * interval, min_distance + 7 * interval),
    (0.8, min_distance + 7 * interval, min_distance + 8 * interval)
]


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

# Reading data
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
                    dist2 = 17

                if min_distance <= dist1 <= max_distance:
                    values_freq.append(dist1)
                else:
                    values_freq.append(values_freq[-1])

                if min_distance <= dist2 <= max_distance:
                    values_amp.append(dist2)
                else:
                    values_amp.append(values_amp[-1])

                note = map_distance_to_note(values_freq[-1])
                amp = map_distance_to_volume(values_amp[-1])
                Note(note, amp, duration=0.3).play()
                print((note, dist1), (amp, dist2))
        time.sleep(0.0001)

except KeyboardInterrupt:
    print("Program stopped.")
    print(values_freq)
finally:
    ser.close()
