# Coursework Assessment 1
# Name:Monika Rogoziniene
# Student No:2334768

# A Caesar Cipher Program
import os.path

def welcome():
    # add your code here
    print('Welcome to the Caesar Cipher')
    print('This program encrypts and decrypts text with the Caesar Cipher.')

    return

def enter_message():
    mode = ''
    message = ''
    shift = 0
    filename = ''
    while True:
        mode = input('Would you like to encrypt (e) or decrypt (d): ')
        if mode in ('e', 'd'):
            break
        else:
            print('Invalid Mode')

    #filename = message_or_file(mode)
    if mode == 'e':
        message = input('What message would you like to encrypt: ').upper()
    if mode == 'd':
        message = input('What message would you like to decrypt: ').upper()
    shift = int(input('What is the shift number: '))
    
    return (mode, message, shift)


def encrypt(message,shift):
   
    #print(" Let's encrypt message", message, "with shift", shift)

    message = message.upper()
    result = ''
    
    for char in message:
        if char.isalpha():
            #deals with overflow
            new_ascii_index = ord(char) + shift
            if (new_ascii_index > 90):
                new_ascii_index = new_ascii_index - 26
            #-------------
                
            result = result + chr(new_ascii_index)
        else:
            result = result + char
            
    return result


def decrypt(message,shift):
    # add your code here
     #print(" Let's decrypt5 message", message, "with shift", shift)
    
    message = message.upper()
    result = ''
    
    for char in message:
        if char.isalpha():
           
            #deals with overflow
            new_ascii_index = ord(char) - shift
            
            #print(new_ascii_index)
            if (new_ascii_index < 65):
                new_ascii_index = new_ascii_index + 26
            #-------------
             
            result = result + chr(new_ascii_index)
        else:
            result = result + char
            
    return result
    #return ''
        

def process_file(filename, mode, shift):
    list_messages = []
    file_path = os.path.join(os.getcwd(), filename)
    with open(file_path, 'r') as file:
    # Read the contents of the file
        if mode == "d":
            for line in file:
                list_messages.append(decrypt(line.strip(), shift))
        if mode == "e":
            for line in file:
                list_messages.append(encrypt(line.strip(), shift))    
    return list_messages


def write_messages(lines):
    # add your code here
    # os.path.join pakele lokacija
    # os.getcwd() issaugo failo direktorija.
    full_path = os.path.join(os.getcwd(), 'results.txt')
    with open(full_path, 'w') as file:
        for string in lines:
            file.write(string + '\n')     
        return "[]"


def is_file(filename):
    if os.path.exists(filename):
        return True
    else:
        return False        

def message_or_file():    
    mode = ''
    filename = None
    message = None
    shift = 0
    while True:
        mode = input('Would you like to encrypt (e) or decrypt (d): ')
        if mode in ('e', 'd'):
            break
        else:
            print('Invalid Mode')
    while True:
        c_f = input('Would you like to read from a file (f) or the console (c)?')
        if c_f in ('f', 'c'):
            break
        else:
            print('Invalid source')
        
    if c_f == 'f':
        while True:
            filename = input('Enter a filename:')
            if  is_file(filename) == True:
                break
            else:
                print('Invalid filename')
    else:
        if mode == 'e':
            message = input('What message would you like to encrypt: ')
        if mode == 'd':
            message = input('What message would you like to decrypt: ')
   
    shift = int(input('What is the shift number: '))
    return (mode, message, filename, shift)
"""
MAIN DRIVER FUNCTION
----------------------------------------------------------------------------------------------
Requirements:
    • Prompt users to select a mode: encrypt (e) or decrypt (d).
    • Check if the mode the user entered is valid.
    If not, continue to prompt the user until a valid mode is selected.
    • Prompt the user for the message they would like to encrypt/decrypt.
    • encrypt/decrypt the message as appropriate and print the output.
    • Prompt the user whether they would like to encrypt/decrypt another message.
        • Check if the user has entered a valid input (y/n).
          If not, continue to prompt the user until they enter a valid response.
          Depending upon the response you should either:
            • End the program if the user selects no.
            • Proceed directly to step 2 if the user says yes.
    • Your program should be as close as possible to the example shown in the assessment specification.
"""
def main():
    # welcome the user
    welcome()
    '''
    while True:
       mode, message, shift = enter_message()

       if(mode == 'e'):
          result= encrypt(message, shift)
          print(result)

       elif(mode =='d'):
           result= decrypt(message, shift)
           print(result)  
    '''
    while True:
        #surenka visus duomenis is comanad promnt
        #pakelia duoenis is failo ( d arba e )
        #issaugo viska i faila
        mode, message, filename, shift = message_or_file()
        if filename != None:
            lines = process_file(filename, mode, shift)
            write_messages (lines)
        else:
            if(mode == 'e'):
                result= encrypt(message, shift)
                print(result)
            elif(mode =='d'):
                result= decrypt(message, shift)
                print(result)
                
        y_n = input('Would you like to encrypt or decrypt another message? (y)/(n):')
        if  y_n == 'n':
            break
        if  y_n == 'y':
            return main()
        if y_n !=('y', 'n'):
            print("Invalid answer")       
    return


# Program execution begins here
if __name__ == '__main__':
    main()

    #result = encrypt("alix123", 5)
    #rint(result)
