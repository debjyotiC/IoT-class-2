import time
import serial
import numpy as np

baudRate = 9600
serialPort = '/dev/cu.usbmodem14201' # COM3

ser = serial.Serial(serialPort, baudRate)
sensor_data = []
data_point = []

for itr in range(0, 10):
    data = float(ser.read(7).decode().strip())
    sensor_data.append(data)
    data_point.append(itr)
    print("The data at {sample} is {data_sen}".format(sample=itr, data_sen=data))
    time.sleep(1)    # get 1s delay

avg = np.average(sensor_data)
print("The avg. of all data is: ", avg)
