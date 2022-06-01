class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

class CLL: 
    def __init__(self):
        self.last = None
    
    def addToEmpty(self,data):

        if(self.last != None):
            return self.last
        
        temp = Node(data)
        self.last = temp

        self.last.next = self.last
        return self.last
    
    def addBegin(self, data):
 
        if (self.last == None):
            return self.addToEmpty(data)
 
        temp = Node(data)
        temp.next = self.last.next
        self.last.next = temp
 
        return self.last
 
    def addEnd(self, data):
 
        if (self.last == None):
            return self.addToEmpty(data)
 
        temp = Node(data)
        temp.next = self.last.next
        self.last.next = temp
        self.last = temp
 
        return self.last
 
    def addAfter(self, data, item):
 
        if (self.last == None):
            return None
 
        temp = Node(data)
        p = self.last.next
        while p:
            if (p.data == item):
                temp.next = p.next
                p.next = temp
 
                if (p == self.last):
                    self.last = temp
                    return self.last
                else:
                    return self.last
            p = p.next
            if (p == self.last.next):
                print(item, "not present in the list")
                break
 
    def traverse(self):
        if (self.last == None):
            print("List is empty")
            return
 
        temp = self.last.next
        while temp:
            print(temp.data, end = " ")
            temp = temp.next
            if temp == self.last.next:
                break

if __name__ == "__main__":
    L = CLL()
    last = L.addBegin(13)
    last = L.addBegin(2)
    last = L.addEnd(22)
    last = L.addEnd(1)
    last = L.addAfter(10,3)

    L.traverse()
