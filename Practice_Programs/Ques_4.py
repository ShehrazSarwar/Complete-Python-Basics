# Program to check if the character is vowel or not

ch = input("Enter single character: ")

if len(ch) == 1 and ch.isalpha():
    vowel = "AEIOUaeiou"
    if ch in vowel:
        print("Vowel!")
    else:
        print("Not a Vowel!")
else:
    print("Please enter a sinlge Alphabet!")

# isdigit() used to check if the inputed string is a digit (not check point values float)
# isalpha() used to check if the string contains all the alphabets not any other character
