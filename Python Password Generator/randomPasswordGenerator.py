# A random password generator for any specified length
import random

# A list of usable characters for a password
usableChars = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z',
                'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z',
                '0', '1', '2', '3', '4', '5', '6', '7', '8', '9',
                '~', '`', '!', '@', '#', '$', '%', '^', '&', '*', '(', ')', '_', '-', '+', '=', '{', '}', '[', ']', '|', '<', ',', '>', '.', '?', '/'];

subChars = {'s': ['5', 'S', '$'], '5': ['s', 'S', '$'], 'S': ['s', '5', '$'], '$': ['s', 'S', '5'],
            'i': ['!', 'l', '1'], '!': ['i', '1', 'l'], '1': ['i', 'l', '!'], 'l': ['!', '1', 'i'],
            'g': ['G', '9', '6'], 'G': ['g', '9', '6'], '9': ['G', 'g', '6'], '6': ['G', 'g', '9'],
            'a': ['A', '@'], 'A': ['a', '@'], '@': ['A', 'a'],
            't': ['T', '7'], 'T': ['t', '7'], '7': ['T', 't'],
            'e': ['E', '3'], 'E': ['e', '3'], '3': ['E', 'e'],
            'o': ['O', '0'], 'O': ['o', '0'], '0': ['O', 'o'],
            'b': ['B', '8'], 'B': ['b', '8'], '8': ['B', 'b']};

def createPassword(password_length, lenOfUsableChars):
    ''' (int, int) -> str

    Takes in password length and the length of the usable characters list as integers and returns a randomly generated password as a string.
    '''
    password = '';

    # Randomly gets a character index and adds the character to the password
    for char in range(int(password_length)):
        charIndex = random.randint(0, lenOfUsableChars);
        password += usableChars[charIndex];
    
    return password;

def getCharSub(password):
    ''' (str) -> str

    Takes in a existing password as a string and returns a new password that substitutes existing characters with similar ones and returns it as a string.
    '''
    newPassword = '';
    for char in password:
        if char in subChars:
            subCharIndex = random.randint(0, len(subChars[char]) - 1);
            char = subChars[char][subCharIndex];
            newPassword += char;
        else:
            newPassword += char;
    return newPassword;

def passwordSearch(passwordName, file):
    ''' (str, file) -> str

    Takes in the name associated with a password as a string and a file and returns line containing the specified password if applicable as a string.
    '''
    line = file.readline();
    
    while line != '':
        if passwordName in line:
            return line.strip();
        line = file.readline();

def choosePasswordType():
    ''' (noneType) -> noneType
    
    User is asked info on password and password options.
    '''

    fileName = 'passwords.txt'; # File name can be changed to any name you want
    file = open(fileName, 'a'); # Append mode for appending password to the end of the file

    lenOfUsableChars = len(usableChars) - 1;

    passwordName = input('What is the password for?: ');
    print('Options:\n1: password with special characters\n2: password without special characters (only letters and numbers)\n3: password with replacement characters (3 instead of E or vice versa)\n4: search for password in file\n');
    passwordOption = input('What password type would you like or want to search for?: ');

    # Password_length is not needed for password option for since it is searching for an existing password
    if passwordOption != '4':
        password_length = input('How long should the password be?: ');

    # Each password option corresponds to a number
    if passwordOption == '1':
        password = createPassword(password_length, lenOfUsableChars);
        print('Generated password is: ' + password + ' and is for ' + passwordName);
        file.write('\n' + passwordName + ' password: ' + password); # Write the generated password to the specified file
        file.close();
        print('Password successfully written to: ' + fileName);
    elif passwordOption == '2':
        password = createPassword(password_length, lenOfUsableChars - 26); # Subtract special character indices from the list
        print('Generated password is: ' + password + ' and is for ' + passwordName);
        file.write('\n' + passwordName + ' password: ' + password);
        file.close();
        print('Password successfully written to: ' + fileName);
    elif passwordOption == '3':
        password = createPassword(password_length, lenOfUsableChars);
        print('Original password: ' + password);
        newPassword = getCharSub(password); # Create a new password with substituted characters
        print('Modified password with substituted characters: ' + newPassword);
        file.write('\n' + passwordName + ' password: ' + newPassword);
        file.close();
        print('Password successfully written to: ' + fileName);
    elif passwordOption == '4':
        file.close();
        file = open(fileName, 'r');
        foundPassword = passwordSearch(passwordName, file);
        print(foundPassword);
    else:
        print('Please choose one of the available options');

choosePasswordType();