print('Hello world!')
print("Hello python!!")

x = 1
x = x + 2
print(x)
print(type(x)) #type used to check the data type of any variable

print(str(x))
print(type(x))  #still int type because we haven't saved it

x = str(x) #now it is converted to string type and replaced with the old value in x
#now x have type str
print(type(x))

x = int(x) #first we have to convert it back to int(we can't perform arithmetic operations on string)
y = x**2 #here ** is representing x^2 
print("x^2 =",y)  # comma add space by default

x = 0
if 0 == x:  # it's the same thing x == 0
    print(x)

A,B = 1.5,3  #Sine we have A = float type so answer will be in float for Floor Division otherwise decimal
C = A//B    #Floor Division (Excludes the decimal point)
print(C,A/B)

Str1 = "Shehraz"
print(Str1[0])  #Same like java or C++ we can access individual characters using indexing

#str,int and float (these are three data common data types of python) there is no concept of ptr and double