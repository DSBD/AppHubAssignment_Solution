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
    mRate = interestRate / 100 / 12;
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
    choice = int(input("\nPlease Choose a Conversion: "));

    if(choice == 1):
        value = float(input("Please Enter the Value in KG: "));
        converted = value * 2.205;
        output = "The Value of " + str(value) + " kg is " + str(round(converted, 2)) + "lbs.";
    elif(choice == 2):
        value = float(input("Please Enter the Value in LBS: "));
        converted = value / 2.205;
        output = "The Value of " + str(value) + " lbs is " + str(round(converted, 2)) + "kg.";
    elif(choice == 3):
        value = float(input("Please Enter the Value in CAD: "));
        converted = value * 0.76;
        output = "The Value of " + str(value) + " CAD is " + str(round(converted, 2)) + "USD.";
    elif(choice == 4):
        value = float(input("Please Enter the Value in USD: "));
        converted = value * 1.32;
        output = "The Value of " + str(value) + " USD is " + str(round(converted, 2)) + "CAD.";
    elif(choice == 5):
        value = float(input("Please Enter the Value in Miles: "));
        converted = value * 1.609;
        output = "The Value of " + str(value) + " miles is " + str(round(converted, 2)) + "km.";
    elif(choice == 6):
        value = float(input("Please Enter the Value in KM: "));
        converted = value / 1.609;
        output = "The Value of " + str(value) + " km is " + str(round(converted, 2)) + "miles.";
    elif(choice == 7):
        value = float(input("Please Enter the Value in Meters: "));
        converted = value * 3.281;
        output = "The Value of " + str(value) + " m is " + str(round(converted, 2)) + "ft.";
    elif(choice == 8):
        value = float(input("Please Enter the Value in FT: "));
        converted = value / 2.381;
        output = "The Value of " + str(value) + " ft is " + str(round(converted, 2)) + "m.";
    elif(choice == 9):
        value = float(input("Please Enter the Value in Celcius: "));
        converted = (value * (9 / 5) + 32);
        output = "The Value of " + str(value) + " °C is " + str(round(converted, 2)) + "°F.";
    elif(choice == 10):
        value = float(input("Please Enter the Value in Fahrenheit: "));
        converted = (value - 32) * (5 / 9);
        output = "The Value of " + str(value) + " °F is " + str(round(converted, 2)) + "°C.";
    else:
        output = "InValid Choice";

    return output;

def TaxCalculator(amount, taxRate):
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
        return "Heads";
    elif(result == 1):
        return "Tails";

def PrintMenu():
    print("\nA - Fibonacci Generator");
    print("B - Prime Factorization");
    print("C - Next Prime Number");
    print("D - Prime Checker");
    print("E - Mortgage Calculator");
    print("F - Change Return Program");
    print("G - Binary to Decimal Converter");
    print("H - Decimal to Binary Converter");
    print("I - Unit Converter");
    print("J - Tax Calulator");
    print("K - Factorial Calculator");
    print("L - Coin Flip Simulation");
    print("Z - Exit");

def main():
    #TODO Create Main Program
    loopControl = True;

    print("Welcome to the App Dashboard, Please Select an App to Continue\n");

    while(loopControl):
        PrintMenu();
        selectedApp = (input("\nPlease Enter a Choice: ")).upper();
        if(selectedApp == "A"):
            terms = int(input("\nWelcome to Fibonacci. Please Enter the Number of Terms you would like: "));
            termList = FibonacciGenerator(terms);

            print("The Terms Are: ", end="");
            for cTerm in termList:
                print(cTerm, end=" ")
            print();
        
        elif(selectedApp == "B"):
            number = int(input("\nWelcome to Prime Factorization. Please Enter the Number you would like to factor: "));
            factList = PrimeFactorization(number);

            print("The Factors Are: ", end="");
            for cTerm in factList:
                print(cTerm, end=" ")
            print();
        
        elif(selectedApp == "C"):
            number = int(input("\nWelcome to Next Prime. Please the Number to Start at: "));

            print("The Next Prime Number after", number, "is", NextPrime(number));

        elif(selectedApp == "D"):
            number = int(input("\nWelcome to Prime Checker. Please the Number to Check: "));

            if(IsPrime(number)):
                print("The Number", number, "is Prime");
            else:
                print("The Number", number, "is not Prime");
        
        elif(selectedApp == "E"):
            principle = float(input("\nWelcome to Mortgage Calculator. Please the Initial Loan Value: "));
            rate = float(input("Please Enter the Interest Rate: "));
            years = int(input("Please Enter the Length of the Loan: "))

            payment = MortgageCalculator(principle, rate, years);

            print("\nThe monthly loan payment is $" + str(payment));

        elif(selectedApp == "F"):
            cost = float(input("\nWelcome to Change Return Calculator. Please Enter the Cost of the Item: "));
            tender = float(input("Please Enter the Tender Amount: "))

            change = ChangeReturn(cost, tender)

            print("$100:", change["100"]);
            print("$50 :", change["50"]);
            print("$20 :", change["20"]);
            print("$10 :", change["10"]);
            print("$5  :", change["5"]);
            print("$2  :", change["2"]);
            print("$1  :", change["1"]);
            print("25₵ :", change["0.25"]);
            print("10₵ :", change["0.1"]);
            print("5₵  :", change["0.05"]);
        
        elif(selectedApp == "G"):
            bNum = input("\nWelcome to Binary to Decimal Converter. Please Enter a Binary Number: ");
            dNum = BinaryToDecimal(bNum);
            print("The Binary Number", bNum, "is", dNum);

        elif(selectedApp == "H"):
            dNum = int(input("\nWelcome to Decimal to Binary Converter. Please Enter a Number: "));
            bNum = DecimalToBinary(dNum);
            print("The Number", dNum, "is", bNum[2::]);

        elif(selectedApp == "I"):
            print(UnitConverter());
        
        elif(selectedApp == "J"):
            number = float(input("\nWelcome to Tax Calculator. Please Enter a Number: "));
            taxRate = int(input("Please Enter the Tax Rate: "))

            total = TaxCalculator(number, taxRate);

            print("The Total is", total);

        elif(selectedApp == "K"):
            number = int(input("\nWelcome to Factrial Calculator. Please Enter a Number: "));
            
            print("The Factorial of", number , "is", Factorial(number));
        
        elif(selectedApp == "L"):
            print("\nWelcome to Coin Flip Simulator. The Coin Says:", CoinFlip());

        elif(selectedApp == "Z"):
            loopControl = False;

    print("\nThank You for Using AppHub, Have a Nice Day!\n");

main();