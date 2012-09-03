%module wiringpi

%apply unsigned char { uint8_t };

extern int  wiringPiSetup     (void) ;
extern int  wiringPiSetupSys  (void) ;
extern int  wiringPiSetupGpio (void) ;

extern void pullUpDnControl   (int pin, int pud) ;
extern void pinMode           (int pin, int mode) ;
extern void digitalWrite      (int pin, int value) ;
extern void pwmWrite          (int pin, int value) ;
extern int  digitalRead       (int pin) ;
extern void shiftOut          (uint8_t dPin, uint8_t cPin, uint8_t order, uint8_t val);
extern uint8_t shiftIn        (uint8_t dPin, uint8_t cPin, uint8_t order);

extern void         delay             (unsigned int howLong) ;
extern void         delayMicroseconds (unsigned int howLong) ;
extern unsigned int millis            (void) ;

extern int   serialOpen      (char *device, int baud) ;
extern void  serialClose     (int fd) ;
extern void  serialPutchar   (int fd, uint8_t c) ;
extern void  serialPuts      (int fd, char *s) ;
extern int   serialDataAvail (int fd) ;
extern int   serialGetchar   (int fd) ;
extern void  serialPrintf    (int fd, char *message, ...) ;

extern int wiringPiSPIGetFd  (int channel) ;
extern int wiringPiSPIDataRW (int channel, unsigned char *data, int len) ;
extern int wiringPiSPISetup  (int channel, int speed) ;

extern void gertboardAnalogWrite (int chan, int value) ;
extern int  gertboardAnalogRead  (int chan) ;
extern int  gertboardSPISetup    (void) ;

extern int          setupNesJoystick (int dPin, int cPin, int lPin) ;
extern unsigned int  readNesJoystick (int joystick) ;

extern int  softPwmCreate (int pin, int value, int range) ;
extern void softPwmWrite  (int pin, int value) ;

%{
#include "WiringPi/wiringPi/wiringPi.h"
#include "WiringPi/wiringPi/wiringShift.h"
#include "WiringPi/wiringPi/wiringSerial.h"
#include "WiringPi/wiringPi/gertboard.h"
#include "WiringPi/wiringPi/wiringPiSPI.h"
#include "WiringPi/wiringPi/softPwm.h"
#include "WiringPi/wiringPi/piNes.h"
#include "WiringPi/wiringPi/lcd.h"
%}
