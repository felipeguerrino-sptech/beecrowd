def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)

while(True):
    try:
        inp = input()
        inp = inp.split()
        n = int(inp[0])
        m = int(inp[1])
    
        print(factorial(n) + factorial(m))
    except:
        break

    