import fileinput
import math

tableau = [['E','N','C','R','Y'],['P','T','A','B','D'],['F','G','H','I','K'],
           ['L','M','O','Q','S'],['U','V','W','X','Z']]

# receive a letter and return its position row, col
def getPosition(letter):
    for i in range(0,5):
        for j in range(0,5):
            if(letter == tableau[i][j]):
                return [i, j]
    return 0

# receive a list and split it by two, return both lists
def split_list(a_list):
    half = len(a_list) // 2
    return a_list[:half], a_list[half:]

# receive a plain text message, return an encrypted message
def encrypt(plain):
    upper, lower, one, letters = [], [], [], []

    # iterate over the message and get the position of each char
    for c in plain:
        position = getPosition(c)
        if(position):
            upper.append(position[0])
            lower.append(position[1])

    # merge upper and lower lists into one
    one = upper + lower

    # group back into pairs and turn to letter using tableau
    for i in xrange(0,len(one),2):
        letters.append(tableau[one[i]][one[i+1]])

    # convert the list to string
    cyphered = ''.join(letters)

    return cyphered

# receive and encrypted message, return a plain text message
def decrypt(cyphered):
    upper, lower, one, letters = [], [], [], []

    # iterate over the cyphered message and get position in tableau of each char
    for c in cyphered:
        position = getPosition(c)
        if(position):
            one.append(position[0])
            one.append(position[1])

    # split list into lower and upper
    upper, lower = split_list(one)

    # group each element in upper with its corresponding in lower
    # find the letter corresponding to that grouping and append it to the msg
    for i in range(0,len(upper)):
        letters.append(tableau[upper[i]][lower[i]])

    # convert the list to string
    message  = ''.join(letters)

    return message

def main():
    instructions = []

    # parse input file
    for line in fileinput.input():
        try:
            # add line after removing the newline character
            instructions.append(line[:-1])
        except:
            break

    # instructions[0] - mode
    # instructions[1] - message
    if instructions[0] == 'ENCRYPT':
        cyphered = encrypt(instructions[1])
        print(cyphered)
    else:
        message = decrypt(instructions[1])
        print(message)

if __name__ == '__main__':
    main()
