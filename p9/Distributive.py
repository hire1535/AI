a = 10
b = 20
c = 30

print("Distributive Law of Addition")

left = a * (b + c)
right = (a * b) + (a * c)

print("a * (b + c) =", left)
print("(a * b) + (a * c) =", right)

if left == right:
    print("Distributive Law is Verified")
else:
    print("Distributive Law is Not Verified")


print("\nDistributive Law of Subtraction")

left = a * (b - c)
right = (a * b) - (a * c)

print("a * (b - c) =", left)
print("(a * b) - (a * c) =", right)

if left == right:
    print("Distributive Law is Verified")
else:
    print("Distributive Law is Not Verified")