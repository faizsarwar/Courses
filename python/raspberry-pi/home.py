from gpiozero import LED
import time
light=LED(4)
light.on()

while True:
    light.on()
    time.sleep(2)
    light.off()
