import time
import datetime

second = time.time()
decimal4 = round(second, 4)
print("Seconds since January 1, 1970: ", end="")
print(f"{decimal4:,} or {decimal4:.2e} in scientific notation")

now = datetime.datetime.now()
print(now.strftime("%b"), now.strftime("%d"), now.strftime("%Y"))
