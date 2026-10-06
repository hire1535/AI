a = 10
b = 20
c = 30

print("Associative Law of Addition")
print("(a + b) + c =", (a + b) + c)
print("a + (b + c) =", a + (b + c))

if (a + b) + c == a + (b + c):
    print("Addition is Associative")
else:
    print("Addition is not Associative")


print("\nAssociative Law of Multiplication")
print("(a * b) * c =", (a * b) * c)
print("a * (b * c) =", a * (b * c))

if (a * b) * c == a * (b * c):
    print("Multiplication is Associative")
else:
    print("Multiplication is not Associative")


print("\nSubtraction")
print("(a - b) - c =", (a - b) - c)
print("a - (b - c) =", a - (b - c))

if (a - b) - c == a - (b - c):
    print("Subtraction is Associative")
else:
    print("Subtraction is not Associative")


print("\nDivision")
print("(a / b) / c =", (a / b) / c)
print("a / (b / c) =", a / (b / c))

if (a / b) / c == a / (b / c):
    print("Division is Associative")
else:
    print("Division is not Associative")