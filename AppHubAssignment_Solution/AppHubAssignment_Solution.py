#Hatch Alpha AppHub Assignment Spring 2019 Solution
#Coded By: Dragos Baciu-David

import random

def FibonacciGenerator(terms):
    n1 = 0;
    n2 = 1;
    cTerms = 2;
    rList = [0, 1];
    
    while(cTerms <= terms):
        rList.append(n1 + n2);
        n1, n2 = n2, n1 + n2;
        cTerms += 1;

    return rList;

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

def MortgageCalculator(loanValue, interestRate, loanLength):
    mRate = interestRate / 100;
    months = loanLength * 12;

    payment = loanValue * ((mRate * (1 + mRate) ** months) / (((1 + mRate) ** months) - 1));

    return round(payment, 2);


def ChangeReturn(cost, tender):
    changeNeeded = tender - cost;

    change = {"100" : 0, "50" : 0, "20" : 0, "10" : 0, "5" : 0, "2" : 0, "1" : 0, "0.25" : 0, "0.1" : 0, "0.05" : 0};

    for value, quantity in change.items():
        while True:
            if(float(value) <= changeNeeded):
                change[value] += 1;
                changeNeeded -= float(value);
            else:
                break;

    return change;

def BinaryToDecimal(bNum):
    return int(bNum, 2);

def DecimalToBinary(dNum):
    return(bin(dNum));

def UnitConverter():
    print("Unit Conversion Program \n1) KG - LBS \n2) LBS - KG \n3) CAD - USD \n4) USD - CAD \n5) Miles - KM \n6) KM - Miles \n7) Meters - Ft \n8) Ft - Meters \n9) Celcius - Fahrenhiet \n10) Fahrenhiet - Celcius");
    choice = int(input("\nPlease Choose a Conversion: "))

    if(choice == 1):
        value = float(input("Please Enter the Value in KG: "));
        converted = value * 2.205;
        output = "The Value of " + str(value) + " kg is " + str(round(converted, 2)) + "lbs."
    elif(choice == 2):
        value = float(input("Please Enter the Value in LBS: "));
        converted = value / 2.205;
        output = "The Value of " + str(value) + " lbs is " + str(round(converted, 2)) + "kg."
    elif(choice == 3):
        value = float(input("Please Enter the Value in CAD: "));
        converted = value * 0.76;
        output = "The Value of " + str(value) + " CAD is " + str(round(converted, 2)) + "USD."
    elif(choice == 4):
        value = float(input("Please Enter the Value in USD: "));
        converted = value * 1.32;
        output = "The Value of " + str(value) + " USD is " + str(round(converted, 2)) + "CAD."
    elif(choice == 5):
        value = float(input("Please Enter the Value in Miles: "));
        converted = value * 1.609;
        output = "The Value of " + str(value) + " miles is " + str(round(converted, 2)) + "km."
    elif(choice == 6):
        value = float(input("Please Enter the Value in KM: "));
        converted = value / 1.609;
        output = "The Value of " + str(value) + " km is " + str(round(converted, 2)) + "miles."
    elif(choice == 7):
        value = float(input("Please Enter the Value in Meters: "));
        converted = value * 3.281;
        output = "The Value of " + str(value) + " m is " + str(round(converted, 2)) + "ft."
    elif(choice == 8):
        value = float(input("Please Enter the Value in FT: "));
        converted = value / 2.381;
        output = "The Value of " + str(value) + " ft is " + str(round(converted, 2)) + "m."
    elif(choice == 9):
        value = float(input("Please Enter the Value in Celcius: "));
        converted = (value * (9 / 5) + 32);
        output = "The Value of " + str(value) + " °C is " + str(round(converted, 2)) + "°F."
    elif(choice == 10):
        value = float(input("Please Enter the Value in Fahrenheit: "));
        converted = (value - 32) * (5 / 9);
        output = "The Value of " + str(value) + " °F is " + str(round(converted, 2)) + "°C."
    else:
        output = "InValid Choice";

    return output;

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
    #TODO Create Main Program
    pass;
main();