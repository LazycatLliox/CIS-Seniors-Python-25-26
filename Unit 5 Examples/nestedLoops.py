'''
Program to print all two letter domain names.

ord('a') --> It will take the ASCII Number
chr(97) --> Takes an ASCII number and gives you it's charcter
'''

print("\n\nTwo-letter domain name:")

letter1 = "a"
letter2 = "?"

while letter1 <= "z":   #outer loop
    letter2 = "a"
    
    while letter2 <= "z":   #inner loop
        print(f"{letter1}{letter2}.com")
        letter2 = chr(ord(letter2) + 1)

    letter1 = chr(ord(letter1) + 1) # protects from infinite loop

