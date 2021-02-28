# THIS IS TERRIBLE CODE, DO NOT COPY ANY ASPECT OF THIS!!!
# Read README.md before tackling this code.

n = 600851475143
pn = []
c = 2

while True:
    if n==c:
        n = 0
        pn.append(c)
        break

    if (n/c).is_integer():
        pn.append(c)
        n = int(n/c)

    while True:
        c += 1

        pri = True

        for i in range(2, c):
            if (c/i).is_integer():
                pri=False
                break
        
        if pri == True:
            break


print(max(pn))
        