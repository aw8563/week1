s = "(1+3)*5"

check = 0
for i in range(0, len(s)):
    check = 0
    if (s[i] == '+' or s[i] == '-' or s[i] == '*' or s[i] == '/' or s[i] == '(' or s[i] == '(' or s[i].isdigit() == True):
        check = 1
        print (s[i])

    if check == 0:
        print ("HERE") 
        print (s[i])
        break

print (check)

