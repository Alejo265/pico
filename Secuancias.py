from machine import Pin
from utime import sleep, sleep_ms
import random
dato1=random.randint(1,5)
dato2=random.randint(1,4)
led1= Pin(15,Pin.OUT)
led2= Pin(2,Pin.OUT)
led3= Pin(4,Pin.OUT)
led4= Pin(16,Pin.OUT)
led5= Pin(17,Pin.OUT)
led6= Pin(5,Pin.OUT)
led7= Pin(18,Pin.OUT)
led8= Pin(19,Pin.OUT)
led9= Pin(22,Pin.OUT)
led10= Pin(23,Pin.OUT)
leds = [led1,led2,led3,led4,led5,led6,led7,led8,led9,led10]
lisall = [led9,led3,led2,led10,led1,led8,led5,led4,led6,led7]
ledsall2 = [led1, led2, led3, led4, led5] and [led10, led9, led8, led7, led6]
ledsall3 = [led6, led7, led8, led9, led10] and [led5, led4, led3, led2, led1]
ledsall4 = [led5, led9, led1, led4, led10] and [led6, led7, led8, led3, led2]
ledsall5 = [led2, led4, led6, led8, led10]
ledsall6 = [led1, led3, led5, led7, led9]
ledsall7 = [led2, led1, led4, led3, led6, led5, led8, led7, led10, led9]
boton1= Pin(13,Pin.IN, Pin.PULL_UP)
boton2= Pin(12,Pin.IN, Pin.PULL_UP)
boton3= Pin(32,Pin.IN, Pin.PULL_UP)
boton4= Pin(27,Pin.IN, Pin.PULL_UP)


print("primer dato:",dato1)
print("Segundo dato:",dato2)

suma=dato1+dato2
if suma==7:
  print(lisall)
else:
  print(leds)

def ida():
  for i in leds:
    i.value(1)
    sleep_ms(50)
    i.value(0)
    sleep(0.05)
def regreso():
  for i in reversed(leds):
    i.value(1)
    sleep(0.05)
    i.value(0)
    sleep(0.05)

def azar():
  for i in lisall:
    i.value(0)
    sleep(0.5)
    i.value(3)
    sleep(0.05)
def azarregreso():
  for i in reversed(lisall):
    i.value(1)
    sleep(0.05)
    i.value(0)
    sleep(0.05)
def doblesec():
  for i in ledsall2:
    i.value(0)
    sleep(0.5)
    i.value(3)
    sleep(0.05)
def doblesecregreso():
  for i in reversed(ledsall2):
    i.value(1)
    sleep(0.05)
    i.value(0)
    sleep(0.05)
def tercerasec():
  for i in ledsall3:
    i.value(0)
    sleep(0.5)
    i.value(3)
    sleep(0.05)
def tercerasecregreso():
  for i in reversed(ledsall3):
    i.value(1)
    sleep(0.05)
    i.value(0)
    sleep(0.05)
def cuatrosec():
  for i in ledsall4:
    i.value(0)
    sleep(0.5)
    i.value(3)
    sleep(0.05)
def cuatrosecregreso():
  for i in reversed(ledsall4):
    i.value(1)
    sleep(0.05)
    i.value(0)
    sleep(0.05)
def quintosec():
  for i in ledsall5:
    i.value(0)
    sleep(0.5)
    i.value(3)
    sleep(0.05)
def quintosecregreso():
  for i in reversed(ledsall5):
    i.value(1)
    sleep(0.05)
    i.value(0)
    sleep(0.05)
def sextosec():
  for i in ledsall6:
    i.value(0)
    sleep(0.5)
    i.value(3)
    sleep(0.05)
def sextosecregreso():
  for i in reversed(ledsall6):
    i.value(1)
    sleep(0.05)
    i.value(0)
    sleep(0.05)
def septimosec():
  for i in ledsall7:
    i.value(0)
    sleep(0.5)
    i.value(3)
    sleep(0.05)
def septimosecregreso():
  for i in reversed(ledsall7):
    i.value(1)
    sleep(0.05)
    i.value(0)
    sleep(0.05)

while True:
    if (boton1.value()==0 and boton1.value()==1):
      print ("boton1")
      ida()

    if (boton2.value()==0):
      print ("boton2")
      regreso()

    if (boton3.value()==0):
      print ("boton3")
      azar()

    if (boton4.value()==0):
      print ("boton4")
      azarregreso()

    if (boton1.value and boton2.value()==0):
      print ("boton1+boton2")
      doblesec()

    if (boton3.value and boton4.value()==0):
      print ("boton3+boton4")
      doblesecregreso()

    if (boton1.value and boton3.value()==0):
      print ("boton1+boton3")
      tercerasec()

    if (boton2.value and boton4.value()==0):
      print ("boton2+boton4")
      tercerasecregreso()

    if (boton1.value and boton4.value()==0):
      print ("boton1+boton4")
      cuatrosec()

    if (boton2.value and boton3.value()==0):
      print ("boton2+boton3")
      cuatrosecregreso()
    
    if (boton1.value and boton2.value and boton3.value()==0):
      print ("boton1+boton2+boton3")
      quintosec()

    if (boton3.value and boton2.value and boton1.value()==0):
      print ("boton3+boton2+boton1")
      quintosecregreso()

    if (boton2.value and boton3.value and boton4.value()==0):
      print ("boton2+boton3+boton4")
      sextosec()

    if (boton4.value and boton3.value and boton2.value()==0):
      print ("boton4+boton3+boton2")
      sextosecregreso()

    if (boton1.value and boton2.value and boton3.value and boton4.value()==0):
      print ("boton1+boton2+boton3+boton4")
      septimosec()

    if (boton4.value and boton3.value and boton2.value and boton1.value()==0):
      print ("boton4+boton3+boton2+boton1")
      septimosecregreso()