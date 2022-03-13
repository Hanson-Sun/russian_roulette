import os
from random import randint
import time
import platform

print("idk why you decided to run this program but okay")
time.sleep(0.5)
print("time to see if you die")
time.sleep(1)

if randint(1,6) == 1:
    print("uh oh")
    time.sleep(0.5)

    if platform.system() == "Windows":
        os.system("shutdown /s /t 1")
    else:
        os.system("shutdown -h now")

else:
    print("you're safe. For now . . .")
