text = input("Insert text here: ")
chars = list(text)
caratteri_modificati = []
key = int(input("Insert here the key (number): "))

for char in chars:
    if char.isalpha():
        shift = key % 26
        
        if char.islower():
            nuovo_carattere = chr(((ord(char) - ord('a') + shift) % 26) + ord('a'))
        elif char.isupper():
            nuovo_carattere = chr(((ord(char) - ord('A') + shift) % 26) + ord('A'))
        
        caratteri_modificati.append(nuovo_carattere)
    else:
        caratteri_modificati.append(char)

crypted = ''.join(caratteri_modificati)
print("Encrypted text:", crypted)
