import time

while True :
    # localTime = time.localtime()
    result = time.strftime('%H:%M:%S')
    print(result)
    time.sleep(1)
