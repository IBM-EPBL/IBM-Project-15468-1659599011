import random
import winsound
temp=random.randint(0,100)
hum=random.randint(0,100)
while True:
    if temp>100:
        if hum>50:
            print("NORMAL")
        else:
            winsound.Beep(440,1200)
            print("TEMPERATURE ALERT!!!!!!!!")
    else:
        winsound.Beep(2000,100)
        print("HIGH TEMPERATURE ALERT!!!!!!!!!")
