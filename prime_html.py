
def mersenne_prime_display(merseene_prime_list):



    with \
    open("large-prime-number.html", "w") as f:

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
                f.write("<br><br>\n<a href=\"large-prime-number-page-"+str(file_count+1)+".html\">\n</body>\n</html>")
                line_count = 0
                file_count += 1
                break


        with \
        open("large-prime-number-page"\
        +str(file_count)+".html", "w") as f:

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

        for file_index in range(file_count):
            f.write(" of "+str(file_count)+"\n</body>\n</html>")




with open("largest_known_prime_number.txt", "r") as f:
    prime_string = f.read()


mersenne_prime_display(prime_string)
 
