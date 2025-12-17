import time

interval = 1
countSecs = 0

startMs = int(time.time() * 1000)
print(f"{startMs=}")

for _ in range(1, 11):
    time.sleep(interval)
    countSecs += interval
    print(f"{countSecs=}")

endMs = int(time.time() * 1000)
diff = endMs - startMs
print(f"{diff}")

start = time.gmtime()
print(f"{start=}")
print(f"{start.tm_year}")
print(f"{start.tm_mon}")
print(f"{start.tm_mday}")
print(f"{start.tm_hour}")
