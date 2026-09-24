def positive_or_negative(given_number):
    if given_number > 0:
        print("positive")
    elif given_number < 0:
        print("negative")
    else:
        print("zero")
    return given_number

def sum_num():
    i = 1
    sum = 0
    while i <= 100:
        sum += i
        i += 1
    print("The sum of the first 100 positive integers is:", sum)
    return sum

def prime_num():
    n = 0
    prime_numbers = []

    prime_number_counter = 0
    while prime_number_counter < 10:
        if n < 2:
            n += 1
        elif n == 2:
            prime_number_counter += 1
            prime_numbers.append(n)
            n += 1
        else:
            dividor = 2
            while dividor != n:
                if prime_number_counter == 10:
                    break
                elif n % dividor == 0:
                    n += 1
                    dividor = 2
                    continue
                else:
                    dividor += 1
                    if dividor == n:
                        prime_number_counter +=1
                        prime_numbers.append(n)
                        n += 1
                        dividor = 2
    print(prime_numbers)
    return prime_numbers

