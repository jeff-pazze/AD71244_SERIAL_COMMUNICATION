import serial
import time

ser = serial.Serial('COM4', 9600, timeout=1)
# var = input("Enter something: ")
# ser.write(str.encode(var))

time.sleep(2)
'''

#ser.write(str.encode('A'))
ser.write("A".encode())
time.sleep(2)
#ser.close()

# ser = serial.Serial('COM4', 9600, timeout=0)
#ser.write(str.encode('S'))
ser.write("s".encode())
time.sleep(2)
# ser.close()
# time.sleep(1)

# ser = serial.Serial('COM4', 9600, timeout=0)

#ser.write(str.encode("S"))
ser.write("c".encode())
time.sleep(2)
# ser.close()
# time.sleep(1)
# ser.write("s")
# time.sleep(1)
# ser.write("s")
'''
# var = "A"
# ser.write(str.encode(var))

# time.sleep(2)
var1 = "S"
ser.write(str.encode(var1))

time.sleep(2)
var2 = "C"
ser.write(str.encode(var2))


while 1:
    try:
        print(ser.readline())
        #print('')
        # time.sleep(1)
        # var = input("Enter something: ")
        # ser.write(str.encode(var))
    except ser.SerialTimeoutException:
        print('Data could not be read')
 


# ser = serial.Serial( "COM3", 9600, timeout=0.05)
# print(ser.name)         # check which port was really used
# ser.write(b'hello')     # write a string
# ser.close()             # close port

#python -m serial.tools.list_ports

# import serial

# ser = serial.Serial()
# ser.port = "COM4"               # serial port
# ser.baudrate = 9600           # set baudrate 115200
# ser.timeout = 60                # timeout 60 second
# ser.open()                      # open serial port

# while True:
#     ser.write('l')              # send '1' to port to get light
#     light = ser.read(4) 
#     print( "light", light)


# import time
# ser = serial.Serial('COM4', 9600, timeout=0)

# while 1:
#  try:
#   print( ser.readline())
#   time.sleep(1)
#  except ser.SerialTimeoutException:
#   print('Data could not be read')
#   time.sleep(1)
#   ser.close()             # close port
        
        