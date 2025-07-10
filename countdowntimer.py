import time



tot_time = int(input("enter no. of seconds : "))


for x in reversed(range(0, tot_time)):
    minutes = int(x/60)%60
    hours = int(x/3600)
    seconds = x % 60
    print(f"{hours:02}:{minutes:02}:{seconds:02}")
    time.sleep(1)
 
print("TIME IS UP!")
