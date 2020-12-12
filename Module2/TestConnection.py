from Module2.ConnectionClass import ArduinoComm

myConn = ArduinoComm(serialPort='/dev/cu.usbmodem14101', baudRate=9600)
myConn.connectWith(number=10, delay=2)
print(f"The average is: {myConn.calculateAverage()}")
myConn.writeCSV(filename='results2.csv')
