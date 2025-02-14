
# In python Strings and Numeric values can operate together with *

A,B = 2,3
Txt = '@'
print(2*Txt*3)   #this will work fine, this will first multiply 2X3 = 6 and print 6 @'s

A = str(A) #A = "2"
print((A+Txt)*B) #(A+Txt) = 2@ and then print it 3 Times Because of *B = *3