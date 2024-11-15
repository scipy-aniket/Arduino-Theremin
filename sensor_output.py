import serial
import time

arduino_port = 'COM5'
baud_rate = 9600

# Initialize
ser = serial.Serial(arduino_port, baud_rate, timeout=1)
time.sleep(2)  # Give some time for the connection to establish

print("Reading distance values from Arduino...")

# values = []

values_1 = []
values_2 = []

# Continuously read data from Arduino
try:
    while True:
        # Read a line from the serial port (decode from bytes to string)
        if ser.in_waiting > 0:
            data = ser.readline().decode('utf-8').strip()
            print(data.split())
            # if data.split() == []:
            #     pass
            # else:
            #     rawlist = data.split()
            #     if rawlist[3] == '1:':
            #         values_1.append(int(rawlist[4]))
            #         print(rawlist[4])
            #     elif rawlist[3] == '2:':
            #         values_2.append(int(rawlist[4]))
            #         print(rawlist[4])

        #time.sleep(0.1)  # Small delay for stability
except KeyboardInterrupt:
    print("Program stopped.")
    print(values_1)
    print(values_2)
    print(len(values_1), len(values_2))
finally:
    ser.close()  # Close the serial connection when done
