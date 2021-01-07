import time
import serial
import numpy as np
import pandas as pd


class ArduinoComm:
    sensor_data = []
    data_point = []

    def __init__(self, serialPort, baudRate):
        self.serialPort = serialPort
        self.baudRate = baudRate

    def connectWith(self, number, delay, verbose=False):
        # creating serial obj
        ser = serial.Serial(self.serialPort, self.baudRate)
        # gather data
        for itr in range(0, number):
            data = float(ser.read(7).decode().strip())
            self.sensor_data.append(data)
            self.data_point.append(itr)
            if verbose:
                print("The data at {sample} is {data_sen}".format(sample=itr, data_sen=data))
            else:
                print('.', end='')
            time.sleep(delay)  # get 1s delay
        print('')

    def calculateAverage(self):
        # calc. avg
        return np.average(self.sensor_data)

    def writeCSV(self, filename):
        # write to CSV
        values = {'Serial': self.data_point, 'Data': self.sensor_data}
        df_w = pd.DataFrame(values, columns=['Serial', 'Data'])
        df_w.to_csv(filename, index=None, header=True)



