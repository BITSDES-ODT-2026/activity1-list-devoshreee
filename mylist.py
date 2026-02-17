from machine import Pin
import time

l1=Pin(12,Pin.OUT)
l2=Pin(26,Pin.OUT)
l3=Pin(18,Pin.OUT)
l4=Pin(5,Pin.OUT)

l=[[1,0,0,0],[0,1,0,0],[0,0,1,0],[0,0,0,1]]

while True:
    for i in l:
        l1.value(i[0])
        l2.value(i[1])
        l3.value(i[2])
        l4.value(i[3])
        time.sleep(0.5)
