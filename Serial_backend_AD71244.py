import serial
import time

 
"""
VARIAVEIS GLOBAIS (NESTE EXEMPLO)
"""

DEVICE    = 'COM4'
BAUD_RATE =  9600
TIMEOUT   =  1
PARITY    = 'N'
STOPBITS  = '1'
BYTESIZE  = '8'

'''
def InfoComSerial():
    print( '\nObtendo informacoes sobre a comunicacao serial\n')
    # Iniciando conexao serial
    #comport = serial.Serial(DEVICE, 9600, timeout=1)
    comport = serial.Serial(DEVICE, int(BAUD_RATE), timeout=int(TIMEOUT), bytesize=int(BYTESIZE), stopbits=int(STOPBITS), parity=PARITY)
    # Alem das opcoes rtscts=BOOL, xonxoff=BOOL, e dsrdtr=BOOL
    # Link: http://pyserial.sourceforge.net/pyserial_api.html#constants
    time.sleep(1.8) # Entre 1.5s a 2s
    print ('\nStatus Porta: %s ' % (comport.isOpen()))
    print ('Device conectado: %s ' % (comport.name))
    print ('Dump da configuracao:\n %s ' % (comport))
 
    print ('\n###############################################\n')
 
    # Fechando conexao serial
    #comport.close()
""" main """
if __name__ == '__main__':
    InfoComSerial()

 
'''
'''
def ComSerial():
    DEVICE    = 'COM4'
    BAUD_RATE =  9600
    TIMEOUT   =  1
    PARITY    = 'N'
    STOPBITS  = '1'
    BYTESIZE  = '8'
    
    ser = serial.Serial(DEVICE , BAUD_RATE, timeout= TIMEOUT )
    # var = input("Enter something: ")
    # ser.write(str.encode(var))
    
    time.sleep(1)
    var1 = "S"                                      # Variavel que corresponde pela leitura de dados pelo AD
    ser.write(str.encode(var1))                     # Envia a solicitação para leitura de dados peço AD
    time.sleep(1)
    var2 = "C"                                      # Variavel que corresponde pela leitura de dados pelo AD de forma continua
    ser.write(str.encode(var2)) 
    
    return ser
    
    
    
'''
'''

def InfoComSerial():
    print( '\nObtendo informacoes sobre a comunicacao serial\n')
    # Iniciando conexao serial
    #comport = serial.Serial(DEVICE, 9600, timeout=1)
    comport = serial.Serial(DEVICE, int(BAUD_RATE), timeout=int(TIMEOUT), bytesize=int(BYTESIZE), stopbits=int(STOPBITS), parity=PARITY)
    # Alem das opcoes rtscts=BOOL, xonxoff=BOOL, e dsrdtr=BOOL
    # Link: http://pyserial.sourceforge.net/pyserial_api.html#constants
    time.sleep(1.8) # Entre 1.5s a 2s
    print ('\nStatus Porta: %s ' % (comport.isOpen()))
    print ('Device conectado: %s ' % (comport.name))
    print ('Dump da configuracao:\n %s ' % (comport))
 
    print ('\n###############################################\n')
 
'''
ser = serial.Serial(DEVICE , BAUD_RATE, timeout= TIMEOUT )
# var = input("Enter something: ")
# ser.write(str.encode(var))

time.sleep(1)

var1 = "S"                                      # Variavel que corresponde pela leitura de dados pelo AD
ser.write(str.encode(var1))                     # Envia a solicitação para leitura de dados peço AD

time.sleep(1)
var2 = "C"                                      # Variavel que corresponde pela leitura de dados pelo AD de forma continua
ser.write(str.encode(var2)) 
                    # Envia a solicitação para leitura de dados pelo AD de forma continua
#InfoComSerial()

#ComSerial()
    
while 1:
    try:
        print(ser.readline())
        #print(ser.read())
        #print(ser.read(5))
        print('\n')
        # time.sleep(1)
        # var = input("Enter something: ")
        # ser.write(str.encode(var))
    except ser.SerialTimeoutException:
        print('Data could not be read')

