
#len() to find the total length
Str1 = "Shehraz"
print(len(Str1))  #len() funtion counts the number of characters


#.startswith() and .endswith()
#boolean funtion
print(Str1.startswith('S'))
print(Str1.endswith('S'))


#To find the first occurance postion (index) of any sub string or Character
#.find(), it's also can take starting index, so that we don't have to check the whole string
Str2 = "I love python!"
print(" ".join(Str2))
print(Str2.find('I'))  #first occurance index
print(Str2.find('Z'))  #will return -1 if not found
print(Str2.find("love"))
Pos1 = Str2.find("love")
Space_Pos = Str2.find(" ",Pos1)  #here Pos1 is the starting position
print(Str2[Space_Pos+1:]) #Exclude 2nd space and print python! only


#To count the no of times the character occurs or sub string
#.count()
print(Str2.count("o"))
print(Str2.count("love"))


#To replace anything in string
#.replace(old,new)
print("Old:",Str2)
Str2 = Str2.replace("love","like")
print("Updated:",Str2)


#To capitalize 1st char of a String
#.capitalize()
new = "sheeraz Sarwar"
new = new.capitalize()
print(new)

#To find if the sub string or character is in the string or not
#in and not in Operators (we can use it with if also)
fruit = 'banana'
print('n' in fruit)
print('m' in fruit)
print('nan' in fruit)

#To Convert string to upper and lower case (also can be used with input())
print(fruit.upper())
print(new.lower())
String_input = input("Enter String: ").lower() #can be .upper()
print(String_input)
