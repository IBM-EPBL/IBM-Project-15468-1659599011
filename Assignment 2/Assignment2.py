import random
import winsound
temp = random.randint(0,100)
hum = random.randint(0,100)
while True:
    if temp>0:
         if hum >100:
                print("Normal")
         else:
                winsound.Beep(4400,120)
                print("Alert!!!! high temperature detected")
    else:
        winsound.Beep(5000,450)
        print("Alert!!! stop")
