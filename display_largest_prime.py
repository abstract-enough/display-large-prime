import matplotlib.pyplot as plt
%matplotlib inline

import os
import shutil
import time

#O(n) printer
def mersenne_prime_write(n):

    #2^n

    #using 1x2x2…
    merseene_prime = 1
    power = 1

    start_time = time.time()
    indices = []
    times = []
    start_power = 1
    end_power = n
    for i in range(start_power,end_power+1):
        if i == power:
          print("multiplication", "{:e}".format(i), "of", "{:e}".format(n))
          indices.append(i)
          times.append(time.time()-start_time)
          plt.plot(indices,times)
          plt.show()
          power = power * 10
        merseene_prime = merseene_prime * 2
        
    #-1
    merseene_prime = merseene_prime - 1

    return merseene_prime




merseene_prime = mersenne_prime_write(136279841)

with open("large_prime_number.txt", "w") as f:
  f.write(str(merseene_prime))
