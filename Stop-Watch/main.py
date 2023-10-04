import os
import time

co = int(input('Enter a number: '))
print('Timer starts')
while co >= 0:
    print(co)
    co = co - 1
    time.sleep(1)
    os.system('clear')

os.system('say done')
