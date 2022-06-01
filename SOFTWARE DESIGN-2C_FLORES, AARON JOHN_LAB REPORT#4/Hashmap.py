def display_hash(hashTable):
      
    for i in range(len(hashTable)):
        print(i, end = " ")
          
        for j in hashTable[i]:
            print("---", end = " ")
            print(j, end = " ")
              
        print()

HashTable = [[] for _ in range(10)]
  

def Hashing(keyvalue):
    return keyvalue % len(HashTable)
  

def insert(Hashtable, keyvalue, value):
      
    hash_key = Hashing(keyvalue)
    Hashtable[hash_key].append(value)
  

insert(HashTable, 21, 'Alison')
insert(HashTable, 21, 'Aaron')
insert(HashTable, 20, 'John')
insert(HashTable, 7, 'Kass')
insert(HashTable, 24, 'Zion')
  
display_hash (HashTable)
