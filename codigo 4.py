
# codigo 4
from machine import Pin as pin
from utime import sleep as pausa, sleep_ms as pausam, sleep_us as pausau
ledb=pin(15,pin.OUT)
ledc=pin(4,pin.OUT)
leda=pin(2,pin.OUT)
ledd=pin(16,pin.OUT)
lede=pin(5,pin.OUT)
ledf=pin(17,pin.OUT)
ledg=pin(18,pin.OUT)
ledh=pin(21,pin.OUT)
ledi=pin(22,pin.OUT)
ledj=pin(23,pin.OUT) 
ledall=[leda,ledb,ledc,ledd,lede,ledf,ledg,ledh,ledi,ledj]
def derecha():
  for i in ledall:
    for j in range (2):
      i.value(not i.value())
      pausam(150)
def izquierda():       
  for i in reversed(ledall):
    for j in range (2):
      i.value(not i.value())
      pausam(150)
while True:
  derecha()
  izquierda()