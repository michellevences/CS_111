import random


print('Program #3: Mind Reader')
print('BTT CS 111: Program Design I in Python')

print('''
Our subconscious get expressed in different ways, including
through choices we make, how we type, and how quickly we type.
Python libraries include Artificial Intelligence (AI) neural 
network tools that can recognize patterns.
For this program choose the algorithm analysis level. Higher
levels take longer, but are more accurate. Level 4 works most
of the time.
      ''')
level = input('Enter level > 1:')



def get_Random_Letter():
    # Get a random number, which will be the offset from 'a' or 'A'
    letter_offset = random.randrange(0, 25)
    # Randomly choose between upper and lower case
    if bool(random.getrandbits(1)):
        # Make it upper case
        # 65 is the code number for 'A'
        random_char = chr(65 + letter_offset)
    else:
        # Make it lower case
        # 97 is the code number for 'a'
        random_char = chr(97 + letter_offset)
    return random_char
  
secret_char = get_Random_Letter()

def get_Digit_Table():
    counter = 99
    while counter >= 0:
      if counter % 10 == 9:
        print('\r')
      
      if counter < 10:
        print(' ', end='')

      if counter % 9 == 0 and counter < 90: 
        print(str(counter) + ':', secret_char, end=' ')
      else:
        print(str(counter) + ':', get_Random_Letter() , end=' ')

      counter -= 1
          
get_Digit_Table()

print('''1. Choose any two-digit number in the table above (e.g. 73).
2. Subtract its two digits from itself (e.g. 73 - 7 - 3 = 63) 
3. Find this new number (e.g. 63) and remember the letter next to it.''')
analyzing = input("4. Press 'a' to analyze responses:")
print('Your letter is:', secret_char)
