#!/usr/bin/env python3

import time

time_struct = time.localtime()

print("some processing log")
print(f"::notice::according to this python script, the time is {time_struct.tm_hour}:{time_struct.tm_min} !")
print("some more processing log")
