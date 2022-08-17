import os
import sys
import time

print("creating stage")
print("#")
print("#")
print("#")
print("#")
print("#")
print("#")
print("#")
print("#")
print("#")
print("#")

## value to print to go back a line: \033[F

line = 0 # 0 is bottom line

def gotoline(y):
    global line
    if (y > line):
        for i in range(y-line):
            print(f"\033[F", end='\r', flush=True)
    elif (y < line):
        for i in range(line-y):
            print(f"\n", flush=True)
    line = y 
    


s = 0
while s < 10:
    gotoline(s)
    s += 1
    time.sleep(1)


while s > 5:
    gotoline(s)
    s -= 1
    time.sleep(0.3)

columns, lines = os.get_terminal_size() 
ncols = 2
def update(n):
    for i in range(n):
        print("i:",sep='',end="\r",flush=False)
        message = f'{i} hello!' + str(lines) + " _ " + str(columns) 
        print(f'{message:<{columns}}', sep='', end='\r', flush=True)
        print(f"\033[F\033[{ncols}G Space-lead appended text")
        time.sleep(0.1)

update(1000)

size = 200
progress = 0
copied = 0
while True:
    print ('Copy Source: ' + str(copied))
    print ('Copy Target: ' + str(copied + 10))
    print ('Progress:' + ("=" * progress))
    print (message)
    copied += 1 
    progress = round(copied * 100 / size)
    my_progress = str(progress).ljust(5)
    sys.stdout.write (my_progress + '%\b\b\b')
    sys.stdout.flush()
    time.sleep(0.2)


