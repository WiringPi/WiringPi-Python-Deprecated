HIGH = 1
LOW = 0
MSBFIRST = 1
LSBFIRST = 0
WPI_MODE_PINS = 0
WPI_MODE_GPIO = 1
WPI_MODE_SYS = 2
MODE_PINS = 0
MODE_GPIO = 1
MODE_SYS = 2
INPUT = 0
OUTPUT = 1
PWM_OUTPUT = 2
PUD_OFF = 0
PUD_DOWN = 1
PUD_UP = 2

class nes(object):
    def setupNesJoystick(self,*args):
        return setupNesJoystick(*args)
    def readNesJoystick(self,*args):
        return readNesJoystick(*args)

class Serial(object):
    device = '/dev/ttyAMA0'
    baud = 9600
    serial_id = 0
    def printf(self,*args):
        return serialPrintf(self.serial_id,*args)
    def dataAvail(self,*args):
        return serialDataAvail(self.serial_id,*args)
    def getchar(self,*args):
        return serialGetchar(self.serial_id,*args)
    def putchar(self,*args):
        return serialPutchar(self.serial_id,*args)
    def puts(self,*args):
        return serialPuts(self.serial_id,*args)
    def __init__(self,device,baud):
        self.device = device
        self.baud = baud
        self.serial_id = serialOpen(self.device,self.baud)
    def __del__(self):
        serialClose(self.serial_id)

class GPIO(object):
    HIGH = 1
    LOW = 0
    MSBFIRST = 1
    LSBFIRST = 0
    WPI_MODE_PINS = 0
    WPI_MODE_GPIO = 1
    WPI_MODE_SYS = 2
    MODE_PINS = 0
    MODE_GPIO = 1
    MODE_SYS = 2
    INPUT = 0
    OUTPUT = 1
    PWM_OUTPUT = 2
    PUD_OFF = 0
    PUD_DOWN = 1
    PUD_UP = 2
    MODE = 0
    def __init__(self,pinmode=0):
        self.MODE=pinmode
        if pinmode==0:
            wiringPiSetup()
        elif pinmode==1:
            wiringPiSetupGpio()
        elif pinmode==2:
            wiringPiSetupSys()
    def delay(self,*args):
        delay(*args)
    def delayMicroseconds(self,*args):
        delayMicroseconds(*args)
    def millis(self):
        return millis()
    def pinMode(self,*args):
        pinMode(*args)
    def digitalWrite(self,*args):
        digitalWrite(*args)
    def pwmWrite(self,*args):
        pwmWrite(*args)
    def digitalRead(self,*args):
        return digitalRead(*args)
    def shiftOut(self,*args):
        shiftOut(*args)
    def shiftOutWithDelay(self,*args):
        shiftOutWithDelay(*args)
    def shiftIn(self,*args):
        return shiftIn(*args)
    def pullUpDnControl(self,*args):
        return pullUpDnControl(*args)
    def softPwmCreate(*args):
        return softPwmCrate(*args)
    def softPwmWrite(*args):
        return sofPwmWrite(*args)
