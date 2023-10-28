'''
    It turns out that calculating the period of a modular exponentiation by hand
    is quite tedious.

    here are some python operators: https://www.geeksforgeeks.org/operator-overloading-in-python/

    Input: 
        most likely binary outputs from the quantum period finder
    Output:
        the correct period (will also show each attempt)
'''
from fraction import Fraction, ContinuedFraction

def period_of_modular_expansion(data, N):
    periods = find_periods(data, N)

def find_periods(data, N):
    for datum in data:
        s_over_r_approx = find_period(datum, N)

def find_period(binary_decimal_thing, N):
    # calculate all convergents and return the most precise one
    # (highest convergent) such that the denominator is less than N
    pass

def verify_period(a, r, m):
    # power mod: a^r mod m
    if pow(a, r, m) == 1:
        return True
    return False

if __name__ == '__main__':

    # frac = Fraction(2, 3)
    # frac2 = Fraction(17, 51) # 1/3

    # con_frac = ContinuedFraction(0.1562)
    # print(con_frac.decimal)
    # print(con_frac)
    # # print(con_frac.calculate_convergent(5))
    # print(con_frac.to_fraction())

    # data = []

    # period_of_modular_expansion(data)




    # print(ContinuedFraction(0.9).to_fraction())
    # print(ContinuedFraction(0.9).to_fraction().decimal())

    while True:
        opt = input("number: ")
        
        if opt == "q":
            break
        else:
            print(ContinuedFraction(float(opt)).to_fraction())



