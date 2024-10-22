def thisisnotafunction():
    print("what")
    print("it is though")

def adder(x, y):
    return x + y

thisisnotafunction()
thisisnotafunction()
thisisnotafunction()
thisisnotafunction()

print(adder(1,2))
print(adder(0,2))
print(adder(10,2))
print(adder(-2,2))
print(adder(1,-2))
print(adder(1,42))
print(adder(21,2))
print(adder(0,0))
print(adder(1,-1))
print(adder(-1,-1))

result = adder(1111111, -1111110)
print(result)