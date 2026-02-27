def title():
    """Prints the Title"""
    print("Feet and Meters Converter\n");
def menu():
    """Prints the Menu"""
    print("Conversions Menu:\na.   Feet to Meters\nb.   Meters to Feet");
def feetmeters(x):
    """Converts feet to meters"""
    return (x*0.3048)
def metersfeet(x):
    """Converts meeters to feet"""
    return (x/0.3048)
def salestaxrate():
    """Returns the Sales Tax Rate"""
    return 6
def CalcSalesTax(taxrate: int,amount: float):
    """Calculates the amount of tax given the tax rate and amount"""
    return round((taxrate/100)*amount,2)
def evenorodd(int):
    """Checks if a number is even or odd"""
    if (int % 2) == 0:
        print("Your number is even");
    else:
        print("Your number is odd");
def GetInt():
    """Gets a Integer from user"""
    return int(float(input("\nPlease enter an integer between 1 and 5000:")))
def IsPrime(x):
    """Checks if number is prime"""
    for i in range(2,x-1):
        if (x%i) == 0:
            return 0
        i+=1
    return 1

def NumberOfFactors(x):
    """Checks the number of factors"""
    factors = 0
    for i in range(2,x-1):
        if (x%i) == 0:
            factors += 1
    return factors
    