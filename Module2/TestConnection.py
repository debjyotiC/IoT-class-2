from Module2.ConnectionClass import ArduinoComm

myConn = ArduinoComm('/dev/cu.usbmodem14101', 9600)
myConn.connectWith(10)
print(f"The average is: {myConn.calculateAverage()}")
# myConn.writeCSV('results2.csv')
