##Reversed string operation using slice 
st=input("Enter the string: ")
st1=st[::-1]
print("Enter the reversed string is:",st1,"\n")

##Reversed string using while loop
while True:
    st2=input("Enter the string: ")
    st3=st2[::-1]
    print("Enter the reversed string is:",st3,"\n")
    break

##Reversed string using function:    
def reverse(): 
  str = "" 
  for i in str2: 
    str = i + str
  return str
str2= str(input("Enter the string: "))
print ("The Reversed string is:", reverse(),"\n")


def reverse(st): 
    st4 = "".join(reversed(st)) # join() method to merge all of the characters resulting from the reversed iteration into a new string. 
    return st
str3= str(input("Enter the string: "))
print ("The Reversed string is:", reverse(str3)) 


