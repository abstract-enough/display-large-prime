import os
import shutil

#O(n^2) test

def test_mersenne_n(
    n, mersenne_prime_list
):

    #note
    #(2^n)-1=2^0+2^1+...+2^(n-1)

    #write 1 (2^0) to temp_1_list
    temp_1_list = [1]

    binary_power_start=1
    binary_power_end=n-1
    for binary_power in range(binary_power_start, \
    binary_power_end+1):

        print(
            "test",
            binary_power,
            "of",
            binary_power_end)

        #write binary power to temp_2_list
        temp_2_list = write_2_to_the_m(
            m=binary_power
        )

        sum_list = add_lists(
            add_1=temp_1_list,
            add_2=temp_2_list
            )

        
        temp_1_list = sum_list

    verify_equality(
        temp_1.temp_1_list,
        merseene_prime_list)


def write_2_to_the_m(
    m,
    print_state
):

    #write 2 (2^1) to temp_4_list
    power_of_two_list = [1]

    for multiplication in range(m):
        if print_state:
            print(
                "step",
                multiplication,
                "of",
                m)
        power_of_two_list = times_2(power_of_two_list)

    return power_of_two_list

def add_lists(
            add_smaller_list,
            add_larger_list,
            ):

    small_count = len(add_smaller_list)
    large_count = len(add_larger_list)

  
    for difference in \
    range(large_count-small_count):
        add_smaller_list.append(0)

    
    sum_list = []
    
    r = 0

    for i in large_count:

        a = add_smaller_list[i]
        b = add_larger_list[i]
        c = a+b+r
        r=c//10
        c=c%10
        sum_list.append(c)

    sum_list.append(r)

    return sum_list

def times_2(in_list):

    

    out_list = add_files(
            add_smaller_list=in_file,
            add_larger_list=in_file,
            )

    return out_list


def verify_equality(
        test_list,
        merseene_prime_list):

    passed = True
    if len(test_list) != len(merseene_prime_list):
        passed = False

    if passed:

      for i in range(len(test_list)):
        if test_list[i] != mersenne_prime_list[i]:
            passed = False
            break

    print("Test result", passed_test)


#O(n) printer
def mersenne_prime_write(n):

    #using 1x2x2…
    write_2_to_the_m(n,True)

    merseene_prime_list = subtract_one(merseene_prime_list)

    return merseene_prime_list


def subtract_one(subtract_list):

    subtract_list[0] -= 1
    
    return subtract_list

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

test_mersenne_n(136279841,"merseene_prime_file.txt")
