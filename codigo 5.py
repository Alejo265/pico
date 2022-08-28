# codigo 5

from machine import Pin as pin
from utime import sleep as pausa, sleep_ms as pausam, sleep_us as pausau
puerto=[2,15,4,16,17,5,18,21,22,23]
ledall=[]
for i in puerto:
  ledall.append  (pin(i,pin.OUT))
print (ledall)
def derecha():
  for i in ledall:
    for j in range (5):
      i.value(not i.value())
    pausam(250) 
def izquierda():
  for i in reversed (ledall):
    for j in range (5):
      i.value(not i.value())
    pausam(100) 
while True:
  derecha()
  izquierda()
 