
def mersenne_prime_display(merseene_prime_list):



    with open("large-prime-number.html", "w") as f:

        f.write("<html>\n<head><title>Large Prime Number</title>\n</head><body>\ndecimal digits of largest known prime number:<br><br>\n")

        digit_count = 0
        line_count = 0
        file_count = 1

        i = 0
        while i < len(merseene_prime_list) :


            digit = merseene_prime_list[i]
            i = i + 1
            f.write(digit)
            digit_count += 1
            if digit_count == 100:
                f.write("<br>\n")
                digit_count = 0
                line_count += 1
            if line_count == 100000:
                f.write("<br><br>\n<a href=\"large-prime-number-page-"+str(file_count+1)+".html\">page "+str(file_count+1))
                line_count = 0
                file_count += 1
                break

        
        while True:

            with open("large-prime-number-page-"+str(file_count)+".html", "w") as f:

                f.write("<html>\n<head><title>Large Prime Number - Page "+str(file_count)+"</title>\n</head><body>\ndecimal digits of largest known prime number:<br><br>\n")

                while i < len(merseene_prime_list):

                    digit = merseene_prime_list[i]
                    i = i + 1

                    f.write(digit)
                    digit_count += 1
                    if digit_count == 100:
                        f.write("<br>\n")
                        digit_count = 0
                        line_count += 1
                    if line_count == 100000:
                        f.write("<br><br>\n<a href=\"large-prime-number-page-"+str(file_count+1)+".html\">page "+str(file_count+1))
                        line_count = 0
                        file_count += 1
                        break

                if i == len(merseene_prime_list):
                    break

    with open("large-prime-number.html", "a") as f:
        f.write(" of "+str(file_count)+"</a>\n</body>\n</html>")

    for file_index in range(2,file_count):
        with open("large-prime-number-page-"+str(file_index)+".html", "a") as f:
            f.write(" of "+str(file_count)+"</a>\n</body>\n</html>")


    with open("large-prime-number-page-"+str(file_count)+".html", "a") as f:
        f.write("<br><br>end</body>\n</html>")


with open("large_prime_number_base_conversion_method.txt", "r") as f:
    prime_string = f.read()


mersenne_prime_display(prime_string)
 
