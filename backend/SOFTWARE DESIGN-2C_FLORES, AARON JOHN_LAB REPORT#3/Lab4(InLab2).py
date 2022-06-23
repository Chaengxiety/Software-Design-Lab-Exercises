def compute(x,y):
  if y == 0:
    return 0
  
  if y > 0:
    return (x+compute(x,y-1))

 

    
x=10
y=20
print("The sum is : ",compute(x,y))