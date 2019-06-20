#Hatch Alpha AppHub Assignment Spring 2019 Solution
#Coded By: Dragos Baciu-David

import random

def FibonacciGenerator(terms):
    pass

def PrimeFactorization(number):
    pass

def NextPrime(number):
    pass

def IsPrime(number):
    i = number - 1;

    while(i > 1):
        if(number % i == 0):
            return False;
        i -= 1;
    return True

def MortgageCalculator(loanValue, loanLength, interestRate):
    pass

def ChangeReturn(cost, tender):
    pass

def BinaryToDecimal(bNum):
    pass

def DecimalToBinary(dNum):
    pass

def UnitConverter():
    pass

def TaxCalulator(amount, taxRate):
    return round(amount * (1 + (taxRate / 100)), 2);

def Factorial(number):
    pass

def CoinFlip():
    result = random.randint(0, 1);
    if(result == 0):
        return "Heads"
    elif(result == 1):
        return "Tails"

def main():
    pass;

if __name__ == "__main__": #The following two lines of code run the main method apon program start as python does no do this by default
    main()