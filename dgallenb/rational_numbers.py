import math;

class Rational:
    def __init__(self, numer, denom):
        self.numer = numer
        self.denom = denom
        self.sanify()

    def __eq__(self, other):
        return self.numer == other.numer and self.denom == other.denom

    def __repr__(self):
        return f'{self.numer}/{self.denom}'

    def __add__(self, other):
        self.numer = self.numer * other.denom + other.numer * self.denom
        self.denom = other.denom * self.denom
        self.sanify()
        return self
        

    def __sub__(self, other):
        self.numer = self.numer * other.denom - other.numer * self.denom
        self.denom = other.denom * self.denom
        self.sanify()
        return self

    def __mul__(self, other):
        self.numer = self.numer * other.numer
        self.denom = other.denom * self.denom
        self.sanify()
        return self

    def __truediv__(self, other):
        self.numer = self.numer * other.denom
        self.denom = other.numer * self.denom
        self.sanify()
        return self

    def __abs__(self):
        self.numer *= -1 if self.numer < 0 else 1
        self.denom *= -1 if self.denom < 0 else 1
        self.sanify()
        return self

    def __pow__(self, power):
        
        if(power > 0):
            self.numer = int(math.pow(self.numer, power))
            self.denom = int(math.pow(self.denom, power))

        elif(power < 0):
            temp = self.numer
            self.numer = int(math.pow(self.denom, -1 * power))
            self.denom = int(math.pow(temp, -1 * power))
        else:
            self.numer = 1
            self.denom = 1
        self.sanify()
        return self

    def __rpow__(self, base):
        temp = base ^ self.numer
        temp2 = 1.0 / self.denom
        return temp ** temp2

    def sanify(self):
        self.fixNegative();
        self.reduce();
        

    def reduce(self):
        gcd = int(math.gcd(self.numer, self.denom))
        self.numer = int(self.numer / gcd);
        self.denom = int(self.denom / gcd);
        pass

    def fixNegative(self):
        if(self.denom < 0):
            self.denom = self.denom * -1;
            self.numer = self.numer * -1;
