import sys
import time
i = 0

while True:
    
    sys.stdout.write("\r\rDoing thing1 %i" % i)
    sys.stdout.write("\rDoing thing2 %i" % i*100)
    sys.stdout.flush()
    i = i + 1
    time.sleep(1)
