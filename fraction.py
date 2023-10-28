'''
    Fractions!

    Messy right now... maybe combine the two classes

    problems:
        - converts 0.99999... to 1, okay, but also 0.9 to 1 :)
        -  0.666666666666... sorts of numbers don't snap to correct fraction (maybe round to nearest?)
        - messes up front part

'''
import math

class Fraction:
    def __init__(self, numerator, denominator):
        self.numerator = numerator
        self.denominator = denominator

        # simplify fraction upon creation
        self.__simplify()

    def __mul__(self, rhs):
        if isinstance(rhs, Fraction):
            return Fraction(self.numerator * rhs.numerator, self.denominator * rhs.denominator)
        elif isinstance(rhs, int):
            # this is actually silly since the factor will be removed during simplification
            # must do right hand multiplication: Fraction * int
            return Fraction(rhs * self.numerator, rhs * self.denominator)
        else:
            raise Exception(f"Invalid multiplication operation: {rhs} is type {type(rhs)}")

    # division (/) operator overload
    def __truediv__(self, rhs):
        if isinstance(rhs, Fraction):
            return self * rhs.reciprocal()
        else:
            raise Exception(f"Invalid division operation: {rhs} is type {type(rhs)}")

    def __add__(self, rhs):
        if isinstance(rhs, Fraction):
            if self.denominator == rhs.denominator:
            # e.g. 1/4 + 2/4 = 3/4
                return Fraction(self.numerator + rhs.numerator, self.denominator)
            
            # get the greatest common denominator
            gcd = self.__gcd(self.denominator, rhs.denominator)
            
            if gcd == 1:
                # e.g. 1/3 + 1/2 == 2/6 + 3/6
                newNumerator = self.numerator * rhs.denominator + rhs.numerator * self.denominator
                newDenominator = self.denominator * rhs.denominator
                return Fraction(newNumerator, newDenominator)
            else:   
                # e.g. 1/6 + 1/3 = 1/6 + 2/6
                # multiply the smallest denominator by the gcd
                if self.denominator < rhs.denominator:
                    newNumerator = gcd * self.numerator
                    return Fraction(newNumerator + rhs.numerator, rhs.denominator)
                else:
                    newNumerator = gcd * rhs.numerator
                    return Fraction(newNumerator + self.numerator, self.denominator)
        elif isinstance(rhs, int):
            # must be right side addition: Fraction + int
            return self + Fraction(rhs, 1)
        else:
            raise Exception(f"Invalid addition operation: {rhs} is type {type(rhs)}")

    def __eq__(self, rhs):
        if self.numerator == rhs.numerator and self.denominator == rhs.denominator:
            return True
        return False

    def __str__(self) -> str:
        return f"{self.numerator} / {self.denominator}"

    # euclidean algorithm to determine greatest common denominator
    def __gcd(self, a, b):
        if a == 0:
            return b
        return self.__gcd(b % a, a)

    # divide out the gcd of the numerator and denominator from the fraction 
    def __simplify(self):
        gcd = self.__gcd(self.numerator, self.denominator)
        # (could just as well divide 1 --> does nothing)
        if gcd != 1:
            self.numerator = int(self.numerator / gcd) 
            self.denominator = int(self.denominator / gcd) 

    # decimal value of Fraction
    def decimal(self):
        return self.numerator / self.denominator
    
    # convert Fraction to its reciprocal value
    def reciprocal(self):
        return Fraction(self.denominator, self.numerator)



class ContinuedFraction:
    def __init__(self, decimal):
        self.decimal = decimal
        self.terms = self.__create_fraction(decimal)
        # self.fraction = None or to_fraction() 

    def __str__(self):
        return f"{self.terms}"

    # divide b by a and return the result of integer division (floored) and remainder
    def __div(self, a, b):
        return (b // a, b % a)
    
    # return a list of terms in decimal's continued fraction
    def __create_fraction(self, decimal):
        terms = []

        # list[<start>:<stop>:<step>] - walk though whole thing backwards with step 1
        # so count the number of characters to the right of the decimal
        decimal_places = str(decimal)[::-1].find('.')
        power_of_10 = 10**decimal_places

        # add the first integer part
        integral_part = math.trunc(decimal)
        terms.append(math.trunc(decimal))  

        if integral_part > 0 and decimal - integral_part != 0:
            return terms

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
            quotient, remainder = self.__div(denominator, numerator)

            # the quotient is the next term
            terms.append(int(quotient))

            # and the remainder is the numerator
            numerator = remainder
        return terms

    def calculate_convergent(self, num):
        '''
            consider a continued fraction [0, 5, 3, 6, 7]
            then we can build a fraction by reading from right to left

            a = 6 + 1/7 
            b = 3 + 1/a
            c = 5 + 1/b
            d = 0 + 1/c

            return d
        '''

        # zero-based index, so from 0 to n-1
        if num < 0 or num > len(self.terms)-1:
            raise Exception(f"invalid input of {num}.. there are {len(self.terms)-1} terms")
        else:
            # 0th convergent has 1 term, nth convergent has n+1 terms
            terms_to_use = self.terms[:num+1]

            print(terms_to_use)

            if len(terms_to_use) == 1:
                return terms_to_use[0]
            else:
                # calculate first bit, then go
                frac = Fraction(1, terms_to_use[-1]) + terms_to_use[-2]
                
                # continue adding the next n-2 numbers in this manner
                for term in terms_to_use[-3::-1]:
                    frac = frac.reciprocal() + term
        return frac

    # convert ContinuedFraction into a simplified Fraction
    def to_fraction(self):
        # this is just calculate convergent with the size of the list
        return self.calculate_convergent(len(self.terms)-1)