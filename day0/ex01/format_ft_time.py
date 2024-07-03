import time
import datetime

second = time.time()
decimal4 = round(second, 4)
thousand_sep = f"{decimal4:,}"
print("Seconds since January 1, 1970:", thousand_sep, "or", "%.2e"%decimal4, "in scientific notation")

now = datetime.datetime.now()
print(now.strftime("%b"), now.strftime("%d"), now.strftime("%Y"))