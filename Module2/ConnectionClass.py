import serial
import time
import numpy as np
import pandas as pd


class ArduinoComm:
    sensor_data = []
    data_point = []

    def __init__(self, serialPort, baudRate):
        self.serialPort = serialPort
        self.baudRate = baudRate

    def connectWith(self, number):
        ser = serial.Serial(self.serialPort, self.baudRate)
        for itr in range(0, number):
            data = float(ser.read(7).decode().strip())
            self.sensor_data.append(data)
            self.data_point.append(itr)
            print("The data at {sample} is {data_sen}".format(sample=itr, data_sen=data))
            time.sleep(1)

    def calculateAverage(self):
        return np.average(self.sensor_data)

    def writeCSV(self, filename):
        values = {'Serial': self.data_point, 'Data': self.sensor_data}
        df_w = pd.DataFrame(values, columns=['Serial', 'Data'])
        df_w.to_csv(filename, index=None, header=True)



