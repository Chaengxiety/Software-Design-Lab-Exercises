def rev(string):
    if len(string) == 0:
      return string
    else:
      return rev(string[1:])+string[0]
x = input("Enter string: ")
print("The reverse of the string is: ", rev(x))

