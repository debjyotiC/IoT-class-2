from Module2.ClassPython import ArduinoComm

myObj = ArduinoComm(serialPort='COM3', baudRate=9600)
myObj.connectWith(number=10, delay=1)
print("The avg. of all data is: {avg:.2f}".format(avg=myObj.calculateAverage()))
myObj.writeCSV('results3.csv')


