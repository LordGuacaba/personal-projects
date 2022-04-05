"""
This program encrypts/decrypts a message that is input and output to the terminal or
a file using a special cypher.
@author Will Hoover
"""

def setup(keyword:str) -> tuple:
    """
    Sets up two lists for translating characters and for shifting the translation.
    """
    keylist = []
    shiftlist = []
    for lett in keyword:
        shiftlist.append(lett)
    if lett not in keylist:
        keylist.append(lett)
    conveyor = []
    for num in range(32, 127):
        conveyor.append(chr(num))
    for letter in conveyor:
        if letter not in keylist:
            keylist.append(letter)
    return keylist, shiftlist

def encrypt(msg:str, keylist:list, shiftlist:list) -> str:
    """
    Uses the setup lists to encrypt the message.
    """
    out = ""
    shift_count = 1
    for char in msg:
        tp = ord(char)
        tp += (ord(shiftlist[shift_count - 1]) - 31)
        shift_count += 1
        if shift_count > len(shiftlist):
            shift_count -= len(shiftlist)
        if tp > 126:
            tp -= 94
        new_letter = keylist[(tp - 32)]
        out += new_letter
    return out

def decrypt(msg:str, keylist:list, shiftlist:list) -> str:
    """
    Uses the setup lists to decrypt a message encrypted using the chosen keyword.
    """
    out = ""
    shift_count = 1
    for char in msg:
        tp = (keylist.index(char) + 32)
        tp -= (ord(shiftlist[shift_count - 1]) - 31)
        shift_count += 1
        if shift_count > len(shiftlist):
            shift_count -= len(shiftlist)
        if tp < 32:
            tp += 94
        new_letter = chr(tp)
        out += new_letter
    return out

def main():
    message = input("Enter original message: ")
    keyword = input("Enter keyword: ")
    function = input("encrypt or decrypt? ")
    file_name = input("File for output (type \"none\" for no file output): ")
    keylist, shiftlist = setup(keyword)
    if function == "encrypt":
        output = encrypt(message, keylist, shiftlist)
    elif function == "decrypt":
        output = decrypt(message, keylist, shiftlist)
    else:
        print("No function specified")
        return
    print(output)
    if file_name != "none":
        with open(file_name) as file:
            file.write(output)

if __name__ == "__main__":
    main()