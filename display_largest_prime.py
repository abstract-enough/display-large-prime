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
    for i in range(1,n):
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


def mersenne_prime_display(merseene_prime_list):



    with \
    open("large-prime-number.html", "r") as f:

        f.write("<html>\n<head><title>Large Prime Number<\title>\n<\head><body>\ndecimal digits of largest known prime number:<br><br>\n"
)

        digit_count = 0
        line_count = 0

        i = len(merseene_prime_list)-1
        while i >= 0:


            digit = merseene_prime_list[i]
            i -= 1
            f.write(digit)
            digit_count += 1
            if digit_count == 100:
                f.write("<br>\n")
                digit_count = 0
                line_count += 1
            if line_count == 10000:
                f.write("<br><br>\n<a href=\"large-prime-page-"+str(file_count+1)+".html\">\n<\body>\n<\html>")
                line_count = 0
                file_count += 1
                break


        with \
        open("large-prime-number-page"\
        +str(file_count)+".html", "r") as f:

            f.write("<html>\n<head><title>Large Prime Number - Page "+str(file_count)+"<\title>\n<\head><body>\ndecimal digits of largest known prime number:<br><br>\n"
            )

            while i >= 0:

                digit = merseene_prime_list[i]
                i -= 1

                f.write(digit)
                digit_count += 1
                if digit_count == 100:
                    f.write("<br>\n")
                    digit_count = 0
                    line_count += 1
                    if line_count == 10000:
                        f.write("<br><br>\n<a href=\"large-prime-page-"+str(file_count+1)+".html\">")
                        line_count = 0
                        file_count += 1
                        break

        for file_index in range(file_count):
            f.write("of "+str(file_count)+"\n<\body>\n<\html>")



merseene_prime_list = mersenne_prime_write(136279841)

with open("large_prime_number.txt", "w") as f:
  f.write(str(merseene_prime))
