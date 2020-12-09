import serial
import time

baudRate = 9600
serialPort = 'COM3'

ser = serial.Serial(serialPort, baudRate)
sensor_data = []
data_point = []

for itr in range(0, 10):
    data = float(ser.read(7).decode().strip())
    print('Data at {0} is {1}'.format(itr, data))
    sensor_data.append(data)
    data_point.append(itr)
    time.sleep(1)


print(sensor_data)