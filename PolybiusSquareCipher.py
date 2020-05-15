def main():
    print('Welcome to the Polybius square cipher\n')
    print('Type 1 to encrypt using the Polybius square cipher ')
    print('Type 2 to decrypt using the Polybius square cipher ')
    print('Type 3 to see how the Polybius square cipher works ')
    print('Type 4 to quit')

    mode = input('Created for educational purposes only\n')
    mode = int(mode)
    
    # Encryption mode
    if mode == 1:
        print("Enter the message you wish to encrypt")
        message = input('Please enter only lowercase letters: ')
        encryption(message)
        input("Press Enter to return to the menu")
        main()
        
    # Decryption mode    
    elif mode == 2:
        message = input('Enter the message you wish to decrypt:\n')
        decryption(message)
        input("Press Enter to return to the menu")
        main()
        
    # How it works     
    elif mode == 3:
        print("The Polybius square is a substitution cipher described by the ancient greek historian Polybius in 150 BC.")
        print("The dimensions of the square used in this program are 5x5, with letters i and j combined to fit the entire alphabet in the square.")
        print("This is the 5x5 square used by this program:\n")
        print("""
                   1  2  3  4  5
                1  A  B  C  D  E
                2  F  G  H I/J K
                3  L  M  N  O  P
                4  Q  R  S  T  U
                5  V  W  X  Y  Z
              """)
        input("Press Enter to return to the menu")
        main()
        
    # Quit
    elif mode == 4:
        raise SystemExit(1)
        
    else:
        print("Error\n")
        input("Press Enter to return to the menu")
        main()
        
def encryption(message):
    encrypted = '' # variable created to store the encrypted message
    # Creating polybius_square list to store every ciphered letter following the alphabet order
    polybius_square = [11, 21, 31, 41, 51, 12, 22, 32, 42, 42, 52, 13, 23, 33, 43, 53, 14, 24, 34, 44, 54, 15, 25, 35, 45, 55]
    alphabet = ['a','b','c','d','e','f','g','h','i', 'j', 'k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']

    for letter in message:
        if letter in alphabet: # checks if the letter is in the defined alphabet list
            index = alphabet.index(letter) # returns the index of the letter in alphabet
            
            # returns the corresponding encrypted letter stored in the square by using the index 
            encrypted = encrypted + ' ' + str(polybius_square[index])
        else:
            print("The letter typed is not in the Polybius Cipher. Please only enter valid letters from the alphabet without spaces or special characters")
            input("Press enter to return to the menu")
            main()
            
    print(encrypted)

def decryption(message):
    decrypted = ''
    # Splitting user inputs separated by spaces in a list
    messagelist = message.split() 
   
    polybius_square = ['11','21','31','41','51','12','22','32','42','42','52','13','23','33','43','53','14','24','34','44','54','15','25','35','45','55']
    alphabet = ['a','b','c','d','e','f','g','h','(i/j)', 'ij','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']

    for number in messagelist:
        if number in polybius_square:
            index =  polybius_square.index(number)
        
            decrypted = decrypted + str(alphabet[index])
        else:
            print("The number typed is not in the Polybius Cipher. Please only enter valid numbers from the Polybius cipher with a space between each of them.")
            input("Press enter to return to the menu")
            main()  
            
    print(decrypted) 
    
if __name__ == "__main__":
    main()
