import time
import serial
import numpy as np
import pandas as pd

# init.
baudRate = 9600
serialPort = 'COM3'  # COM3

# creating serial obj
ser = serial.Serial(serialPort, baudRate)
sensor_data = []
data_point = []

# gather data
for itr in range(0, 10):
    data = float(ser.read(7).decode().strip())
    sensor_data.append(data)
    data_point.append(itr)
    print("The data at {sample} is {data_sen}".format(sample=itr, data_sen=data))
    time.sleep(1)  # get 1s delay

# calc. avg
avg = np.average(sensor_data)
print("The avg. of all data is: ", avg)

# write to CSV
values = {'Serial': data_point, 'Data': sensor_data}
df_w = pd.DataFrame(values, columns=['Serial', 'Data'])
df_w.to_csv("results.csv", index=None, header=True)



