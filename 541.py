a = input()
b = input()

maxA = a
for i in range(0, len(a)):
    a = a[1:] + a[0]
    maxA = max(maxA, a)

minB = ""
for i in range(0, len(b)):
    b= b[1:] + b[0]
    if b[0] != '0':
        if minB == '':
            minB = b
        else:
            minB = min(minB, b)

print (int(maxA) - int(minB))