
def findMin(seq,y):
  if y == 1:
    return seq[0]
  return min(seq[y-1],findMin(seq,y-1))

def findMax(seq,y):
  if y == 1:
    return seq[0]
  return max(seq[y-1],findMax(seq,y-1))
    
  
  
if __name__ == '__main__':
  seq=[5,13,3,4,7,10]
  y=len(seq)
  print("The minimum number in the sequence is: ", findMin(seq,y))
  print("The minimum number in the sequence is: ", findMax(seq,y))

