import math
from itertools import product # cartesian product

# break apart a string of ints into a list
def parse(str):
    return [int(c) for c in str]

# combine a list of ints into a string
def combine(lst):
    string = ""
    for c in lst:
        string += str(c)
    return string

def dot(a, b):
    sum = 0
    # convert to list of ints if str
    if type(a) is str:
        a = parse(a)
        b = parse(b)
    for i in range(len(a)):
        sum += (a[i] * b[i])
    return sum

def solutions(zs):
    
    # all bit strings that when dotted into z_i, yield 0
    temps = []
    
    # intersection of values in temps
    sols = []

    # all zs will have same length, so use length of first z to
    # generate a list of n bits: 0 or 1    
    bits = [[1,0] for i in range(len(zs[0]))]
    states = []
    
    # combine these n bits into 2^n possible states
    for state in product(*bits):
        # product returns a tuple, could use list(x) to convert to list
        states.append(state) 

    # try to find every combination s.t. z_i * s = 0
    for i, z in enumerate(zs):
        # add set for current z_i --> nice for finding intersection later
        temps.append(set())
        zi = parse(z)

        for state in states:
            if dot(zi, state) % 2 == 0:
                temps[i].add(state)

    # combine all temp lists into one list
    big = []
    for temp in temps:
        # print(temp)
        big.append(temp)
    
    # the solution is contained in the intersection between all possible answers
    sols = set.intersection(*big)

    return sols

def hidden_dot():
    # find all the possible bit strings such that
    # the dot product with each value of z is 0 mod 2

    # zs = ["011", "110", "010"]
    zs = ["001", "111"]

    sols = solutions(zs)

    print("\nz values:")
    for i, z in enumerate(zs):
         print(f" {i+1}) {z}")
    print("possible values of s:")
    for i, sol in enumerate(sols):
        sol = combine(sol)
        print(f" {i+1}) {sol}")






def binary_to_decimal(bin):
    dec = 0 
    split = ["0", "0"]

    # check if binary value contains a fraction
    # if not, then just leave the fraction element as 0
    if "." in bin:
        split = bin.split(".")
    else:
        split[0] = bin

    # reverse order of the integer string to make summation easier 
    # 2^n + ... + 2^1 + 2^0 "." + 2^-1 + ... + 2^-n
    # 2^0 + 2^1 + ... + 2^n "." + 2^-1 + ... + 2^-n
    # split = [val[::-1] for val in split]

    # list[<start>:<stop>:<step>] - walk though whole thing backwards with step 1
    split[0] = split[0][::-1]

    # calculate integer part
    for i, val in enumerate(split[0]):
        dec += (int(val) * 2**i)

    # calculate fraction part
    for i, val in enumerate(split[1]):
        i += 1 # start with 1/2 after decimal

        # print()
        # print(i, val)
        # print(val, " * ", 2**(-i))
        dec += (int(val) * 2**(-i))

    return dec

def binary_fractions():
    bins = ["0.0001101", "0.00011101", "10", "1.1", "1.01"]
    decs = [[bin, binary_to_decimal(bin)] for bin in bins]

    print("\nresults:")
    for [bin, dec] in decs:
        print("base-2:", bin)
        print("base-10:", dec)
        print()






# this could easily be a class where we store the terms a_0,...,a_n in a list
def continued_fractions():

    def div(a, b):
        # divide b by a and return the result of integer division (floored) and remainder
        return (b // a, b % a)


    def create_fraction(decimal):
        # return a list of terms in decimal's continued fraction
        terms = []

        # list[<start>:<stop>:<step>] - walk though whole thing backwards with step 1
        # so count the number of characters to the right of the decimal
        decimal_places = str(decimal)[::-1].find('.')
        power_of_10 = 10**decimal_places

        # add the first integer part
        terms.append(math.trunc(decimal))  
        
        # begin expressing 
        denominator = power_of_10
        numerator = decimal * power_of_10

        while True:
            # swap the numerator and denominator
            numerator, denominator = denominator, numerator

            if denominator == 0 or denominator == 1:  
                break

            # divide and add the integer to the list of continued fraction terms
            # basically, create a mixed fraction with the given items
            quotient, remainder = div(denominator, numerator)

            # the quotient is the next term
            terms.append(int(quotient))

            # and the remainder is the numerator
            numerator = remainder
        return terms

        
    def calculate_convergents(decimal, fraction):
        # calculate the convergents of a given continued fraction
        print(f"{decimal} convergents: ")
        for i in range(len(fraction)):
            convergent = 0
            for j in range(0, i):
                convergent += fraction[j]

            print(f" convergent {i}: {convergent}")

            # wrong, not a sum -- need to place terms into continued fraction



    # simple continued fraction expansion of pi: http://oeis.org/A001203
    # decimals = [0.3438, 0.5, 0.6562, 0.8438, 1.61, math.pi, 0.1562]
    decimals = [0.3438, 0.5, 0.6562, 0.8438]
    fractions = []

    for decimal in decimals:
        fractions.append(create_fraction(decimal))

    for decimal, fraction in zip(decimals, fractions):
        print(decimal, fraction)

    # for decimal, fraction in zip(decimals, fractions):
    #     print()
    #     calculate_convergents(decimal, fraction)
    

def modular_expansion():
    
    strings = []
    # convert it to binary fraction

    # create a continued fraction

    # approximate s/r

if __name__ == '__main__':
    hidden_dot()
    # binary_fractions()
    # continued_fractions()
    # modular_expansion()


    print(5 * 0.125 / 2.0)