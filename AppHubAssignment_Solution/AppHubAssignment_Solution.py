#Hatch Alpha AppHub Assignment Spring 2019 Solution
#Coded By: Dragos Baciu-David

import random

def FibonacciGenerator(terms):
    pass

def PrimeFactorization(number):
    factList = [];
    curFactor = 1;

    while(curFactor < number):
        if(number % curFactor == 0 and IsPrime(curFactor)):
            factList.append(curFactor);
        curFactor += 1;

    return factList;

def NextPrime(number):
    nPrime = number + 1;

    while(IsPrime(nPrime) == False):
        nPrime += 1;

    return nPrime;

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
    return int(bNum, 2);

def DecimalToBinary(dNum):
    return(bin(dNum));

def UnitConverter():
    pass

def TaxCalulator(amount, taxRate):
    return round(amount * (1 + (taxRate / 100)), 2);

def Factorial(number):
    result = 1;

    while(number > 1):
        result *= number;
        number -= 1;

    return result;

def CoinFlip():
    result = random.randint(0, 1);
    if(result == 0):
        return "Heads"
    elif(result == 1):
        return "Tails"

def main():
    #print(BinaryToDecimal("1010010"));
    #print(DecimalToBinary(82)[2::]);

    pass;

main();