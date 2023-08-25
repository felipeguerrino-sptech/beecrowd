alphabet = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"

n_lines = int(input())

text_lines = []

for i in range(n_lines):
    line = input()
    text_lines.append(line)

for i in range(0, len(text_lines)):
    line = list(text_lines[i])
    for j in range(0, len(line)):
        if(alphabet.find(line[j]) > -1):
            char = ord(line[j])
            line[j] = chr(char+3)        

    line = line[::-1]
    
    half = int(len(line)/2)
    
    for k in range(half, len(line)):
        char = ord(line[k])
        line[k] = chr(char-1)

    line = "".join(line)            
    text_lines[i] = line

text = "\n".join(text_lines)

print(text)