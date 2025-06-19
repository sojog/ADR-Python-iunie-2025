import time

start_timestamp = time.time()
print("inceput:", start_timestamp)

print("Buna dimineata")
time.sleep(3)
print("Buna ziua")
time.sleep(5)
print("Buna seara")

stop_timestamp = time.time()
print("final:", stop_timestamp)


print("Au trecut", stop_timestamp - start_timestamp)