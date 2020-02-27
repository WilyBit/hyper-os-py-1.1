import time

print ("Hyper OS 1.1 Starting Setup")
time.sleep(8)
print ("hyper os setup")
print ("We Need To Setup Before Running")
print ("We need to know whats your Name")
Name = input("name ")
print ("Hello " + Name)
time.sleep(3)
now = time.asctime()
print(now)
print("right time isnt it")
time.sleep(4)
print("...")
time.sleep(1)
print("lets go back to setup installing now")
time.sleep(1)
for prcnt in range(1,101):
  print(prcnt)
print("booting hyper os")
time.sleep(3)
print("What would you like to do : ")
option = int(input("1. Clock, 2. Change Username, 3. Restart OS, 4. Exit"))
while option!=4:
  if option == 1:
    print(now)
    print("What would you like to do :  ")
    option = int(input("1. Clock, 2. Change Username, 3. Restart OS, 4. Exit"))
  if option == 2:
    print ("Ok Wanna Change Username")
    Name = input("name ")
    print ("Ok New Username Is " + Name)
    print("What would you like to do :  ")
    option = int(input("1. Clock, 2. Change Username, 3. Restart OS, 4. Exit"))
  if option == 3:
    for prcnt in range(1,101):
      print(prcnt)
    print("booting hyper os")
    print("What would you like to do :  ")
    option = int(input("1. Clock, 2. Change Username,3. Restart OS 4. Exit"))
    