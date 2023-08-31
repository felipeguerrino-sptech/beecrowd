digits = '0123456789'

while(True):
    digit_counts = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    list_digits = []
    rg = input()
    rg = rg.split()
    
    if(rg[0] == '0' and rg[1] == '0'):
        break
    
    for i in range(int(rg[0]), int(rg[1])+1):
        list_digits.extend(list(str(i)))
    for j in list_digits:
            idx = digits.find(j)
            digit_counts[idx] += 1
    print(digit_counts)