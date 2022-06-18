import time

f = open("totaltime.txt", "r")
cur_total_time = f.read()
f.close

start_time = time.time()
print('counting time. Enjoy your gym session')

input('Press any key to stop: ')
stop_time = time.time()

time_in_s = int(stop_time - start_time)
time_in_m = int(time_in_s / 60)
time_in_h = int(time_in_m / 60)

print("Total Time Spent: ", time_in_h, " Hours")
new_time = int(cur_total_time) + int(time_in_s)
new_time = str(new_time)

f = open("totaltime.txt", "w")
f.write(new_time)
print("works")
f.close
