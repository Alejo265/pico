# codigo 3
from machine import Pin as pin
import utime
leda=pin(2,pin.OUT)
ledb=pin(15,pin.OUT)
ledc=pin(4,pin.OUT)
ledd=pin(16,pin.OUT)
lede=pin(17,pin.OUT)
ledf=pin(18,pin.OUT)
ledg=pin(21,pin.OUT)
ledh=pin(22,pin.OUT)
ledi=pin(5,pin.OUT)
ledj=pin(23,pin.OUT) 
ledall = [leda,ledb,ledc,ledd,lede,ledf,ledg,ledh,ledi,ledj]
def derecha():
  for elemento in ledall:
    elemento.value(1)
    utime.sleep_ms(50)
    elemento.value(0)
    utime.sleep(0.15)
def izquierda():
  for elemento in reversed(ledall):
    elemento.value(1)
    utime.sleep(0.15)
    elemento.value(0)
    utime.sleep(0.05)
while True:
  derecha()
  izquierda()