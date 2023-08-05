for i in range(1, 11):
    if i % 2 != 0:
        print(i, end="")
print("\n-------------------------")
x = 1
while x < 11:
    if x % 2 != 0:
       print(x, end="")
    x += 1
print("\n-------------------------")
for ch in "john.smith@pythoninstitute.org":
    if ch == "@":
        break
    print(ch, end="")
print("\n-------------------------")
for digit in "0165031806510":
    if digit == "0":
        print("x", end="")
        continue
    print(digit, end="")