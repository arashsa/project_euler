import itertools


# problem 1 (solved)
def multiples_of_three_and_five(limit):
    limit -= 1
    multiple_sum = 0
    while limit > 2:
        if limit % 3 == 0 or limit % 5 == 0:
            multiple_sum += limit
        limit -= 1
    print multiple_sum


# multiples_of_three_and_five(1000)


# problem 2 (solved)
def even_numbered_fibonacci(limit):
    first = 2
    second = 3
    the_sum = 2
    limit -= 2

    while second < limit:
        # print second
        if second % 2 == 0:
            the_sum += second
            # print second
        hold_second = second
        second += first
        first = hold_second
    print the_sum


# even_numbered_fibonacci(4000000)


# problem 3 (solved)
def largest_prime_factor(num):
    case = 1
    numbers_list = []

    while case <= num:
        case += 1
        if num % case == 0:
            numbers_list.append(case)
            num /= case
            case = 1

    print numbers_list


# largest_prime_factor(23454245987)


# problem 4 (solved)
def check_palindrome(i, j):
    prod = str(i * j)
    if len(prod) % 2 == 0:
        prod1 = prod[0:len(prod) / 2]
        prod2 = prod[len(prod) / 2:len(prod)]
        prod2 = prod2[::-1]
        if prod1 == prod2:
            return True


def largest_palindrome_product(digits):
    digit1 = pow(10, digits)
    my_palindromes = []

    while digit1 > 0:
        digit2 = pow(10, digits)
        while digit2 > 0:
            if check_palindrome(digit1, digit2):
                my_palindromes.append(digit1 * digit2)
            digit2 -= 1
        digit1 -= 1
    return max(my_palindromes)


# print largest_palindrome_product(3)


# problem 5 (solved)
def smallest_multiple(start, end):
    check = 10

    while True:
        for i in range(start, end + 1):
            if check % i == 0:
                if i == end:
                    return check
            else:
                break
        check += 2


# print smallest_multiple(1, 20)


# problem 6 (solved)
def sum_square_difference(test_range):
    sum_of_squares = 0
    square_of_sums = 0

    for i in range(1, test_range + 1):
        sum_of_squares += pow(i, 2)

    for i in range(1, test_range + 1):
        square_of_sums += i

    square_of_sums = pow(square_of_sums, 2)

    return square_of_sums - sum_of_squares


# print sum_square_difference(100)


# problem 7 (solved)
def is_prime(num):
    if num <= 3:
        return num >= 2

    if num % 2 == 0 or num % 3 == 0:
        return False

    for i in range(5, int(num ** 0.5) + 1, 6):
        if num % i == 0 or num % (i + 2) == 0:
            return False
    return True


def find_prime(num):
    if num < 1:
        return 0
    if num == 1:
        return 2

    count = 0
    for i in itertools.count(1, 2):
        if is_prime(i):
            count += 1
            if count == num:
                return i


def get_all_primes(num):
    for i in range(1, num):
        print "{}: {}".format(i, find_prime(i))


#   print find_prime(100000)


# problem 8 (solved)
def largest_product_in_a_series(series, length):
    prods = []
    temp = 1
    # print "length of list: {}".format(len(series) - length)
    for i in range(len(series) - length):
        prods.append(temp)
        temp = 1
        for j in range(length):
            # print i + j
            temp *= int(series[i + j])
    print max(prods)


# largest_product_in_a_series("73167176531330624919225119674426574742355349194934"+
# "96983520312774506326239578318016984801869478851843" +
# "85861560789112949495459501737958331952853208805511" +
# "12540698747158523863050715693290963295227443043557" +
# "66896648950445244523161731856403098711121722383113" +
# "62229893423380308135336276614282806444486645238749" +
# "30358907296290491560440772390713810515859307960866" +
# "70172427121883998797908792274921901699720888093776" +
# "65727333001053367881220235421809751254540594752243" +
# "52584907711670556013604839586446706324415722155397" +
# "53697817977846174064955149290862569321978468622482" +
# "83972241375657056057490261407972968652414535100474" +
# "82166370484403199890008895243450658541227588666881" +
# "16427171479924442928230863465674813919123162824586" +
# "17866458359124566529476545682848912883142607690042" +
# "24219022671055626321111109370544217506941658960408" +
# "07198403850962455444362981230987879927244284909188" +
# "84580156166097919133875499200524063689912560717606" +
# "05886116467109405077541002256983155200055935729725" +
# "71636269561882670428252483600823257530420752963450", 13)


# problem 9 (solved)
def special_pythagorean_triplet(num):
    for i in range(num):
        for j in range(i, num):
            for k in range(j, num):
                if pow(i, 2) + pow(j, 2) == pow(k, 2):
                    if i + j + k == num:
                        print "{}^2 + {}^2 = {}^2".format(i, j, k)
                        print "Product {}".format(i*j*k)

# special_pythagorean_triplet(1000)


# problem 10 (solved)
def sum_of_all_primes(num):
    the_sum = 0
    for i in range(2, num - 1):
        current = is_prime(i)
        if current:
            # print i
            the_sum += i
    print the_sum

# sum_of_all_primes(2000000)