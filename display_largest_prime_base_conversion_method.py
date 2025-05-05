def mersenne_prime_write(n):

    if n%8 == 1:
        prime_string = "01"
    elif n%8 == 2:
        prime_string = "03"
    elif n%8 == 3:
        prime_string = "07"
    elif n%8 == 4:
        prime_string = "0F"
    elif n%8 == 5:
        prime_string = "1F"
    elif n%8 == 6:
        prime_string = "3F"
    elif n%8 == 7:
        prime_string = "7F"

    for i in range(n//8):
        prime_string += "FF"

    merseene_prime = int.from_bytes(bytearray.fromhex(prime_string),byteorder='big') 

    return merseene_prime


merseene_prime = mersenne_prime_write(136279841)

with open("large_prime_number_base_conversion_method.txt", "w") as f:
  f.write(str(merseene_prime))
