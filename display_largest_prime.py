import os
import shutil

#O(n^2) test

def test_mersenne_n(
    n, mersenne_prime_file
):

    #note
    #(2^n)-1=2^0+2^1+...+2^(n-1)

    #write 1 (2^0) to temp_1.txt
    with open("temp_1.txt", "w") as f:
        f.write("1")

    binary_power_start=1
    binary_power_end=n-1
    for binary_power in range(binary_power_start, \
    binary_power_end+1):

        print(
            "test",
            binary_power,
            "of",
            binary_power_end)

        #write binary power to temp_2.txt
        write_2_to_the_m(
            temp_2.txt,
            m=binary_power
        )

        add_files(
            add_1=temp_1.txt,
            add_2=temp_2.txt,
            sum=temp_3.txt)

        os.remove("temp_1.txt")
        os.remove("temp_2.txt")
        os.rename("temp_3.txt", "temp_1.txt")

    verify_equality(
        temp_1.txt,
        merseene_prime_file)


def write_2_to_the_m(
    result_file,
    m,
    print_state
):

    #write 2 (2^1) to temp_4.txt
    with open("temp_4.txt", "w") as f:
        f.write("1")

    for multiplication in range(m):
        if print_state:
            print(
                "step",
                multiplication,
                "of",
                m)
        times_2(
            in_file="temp_4.txt",
            out_file=result_file
        )

        os.remove("temp_4.txt")
        os.rename(result_file, "temp_4.txt")


def add_files(
            add_smaller_file,
            add_larger_file,
            sum_file):

    with open(add_smaller_file, "r") as f:
        digit=f.read()
        small_count = 1
        while digit >= '0' and digit <= '9':
            digit = f.read(1)
            small_count += 1

    with open(add_larger_file, "r") as f:
        digit=f.read()
        large_count = 1
        while digit >= '0' and digit <= '9':
            digit = f.read(1)
            large_count += 1

    with open(add_smaller_file, "a") as f:
        for difference in \
        range(large_count-small_count):

            f.write("0")

    with \
        open(add_smaller_file, "r") as f, \
        open(add_larger_file, "r") as g, \
        open(sum_file, "w") as h:

        a = f.read(1)
        b = g.read(1)
        r = 0

        while a >= '0' and a <= '9':

            c = int(a)+int(b)+r
            r=c//10
            c=c%10
            h.write(str(c))

            a = f.read(1)
            b = g.read(1)

        h.write(str(r))


def times_2(in_file, out_file):

    shutil.copy(in_file, "temp_6.txt")

    add_files(
            add_smaller_file=in_file,
            add_larger_file="temp_6.txt",
            sum_file=out_file)

    os.remove("temp_6.txt")


def verify_equality(
        test_file,
        merseene_prime_file):

    with \
        open(test_file, "r") as f, \
        open(mersenne_prime_file, "r") as g:

        a = f.read(1)
        b = g.read(1)

        passed = True

        while a >= '0' and a <= '9':

            if a!=b:
                passed = False
                break

        print("Test result", passed_test)



#O(n) printer
def mersenne_prime_write(n):

    #using 1x2x2…
    write_2_to_the_m(
        "merseene_prime_file.txt",n,True)

    subtract_one("merseene_prime_file.txt")


def subtract_one(subtract_file):

    with \
    open(subtract_file, "r") as f, \
    open("temp_file_7.txt", "w") as g:

        digit=f.read()
        g.write(str(int(digit)-1))
        while digit >= '0' and digit <= '9':
            digit = f.read(1)
            g.write(digit)

def mersenne_prime_display():

    with open("mersenne_prime_file.txt", "r") as g:

        with \
        open("large-prime-number.html", "r") as f:

            f.write("<html>\n<head><title>Large Prime Number<\title>\n<\head><body>\ndecimal digits of largest known prime number:<br><br>\n"
)

            digit_count = 0
            line_count = 0
            file_count = 1
            file.seek(0, 2)  # Go to the end of the file
            position = file.tell()  # end of file

            while position > 0:
                position -= 1
                file.seek(position)
                digit = file.read(1)
                g.write(digit)
                digit_count += 1
                if digit_count == 100:
                    g.write("<br>\n")
                    digit_count = 0
                    line_count += 1
                if line_count == 10000:
                    f.write("<br><br>\n<a href=\"large-prime-page-"+str(file_count+1)+".html\">\n<\body>\n<\html>")
                    line_count = 0
                    file_count += 1
                    break

        while position > 0:
            with \
            open("large-prime-number-page"\
            +str(file_count)+".html", "r") as f:

                f.write("<html>\n<head><title>Large Prime Number - Page "+str(file_count)+"<\title>\n<\head><body>\ndecimal digits of largest known prime number:<br><br>\n"
)

                while position > 0:

                    position -= 1
                    file.seek(position)
                    digit = file.read(1)
                    g.write(digit)
                    digit_count += 1
                    if digit_count == 100:
                       g.write("<br>\n")
                       digit_count = 0
                       line_count += 1
                       if line_count == 10000:
                            f.write("<br><br>\n<a href=\"large-prime-page-"+str(file_count+1)+".html\">")
                            line_count = 0
                            file_count += 1
                            break

        for file_index in range(file_count):
            f.write("of "+str(file_count)+"\n<\body>\n<\html>")



mersenne_prime_write(136279841)

test_mersenne_n(136279841,"merseene_prime_file.txt")
