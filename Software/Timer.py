import time

print("Timer")
timer_sec = int(input("Write time in seconds: "))
for i in reversed(range(timer_sec)):
    print(i, end="\r")
    time.sleep(1)
