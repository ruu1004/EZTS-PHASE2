#Creating node declaration and defination
class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
class singlelinkedlist:
    def __init__(slef):
        slef.head=None
    def insert_begining(self,data):
        nb=Node(data)
        nb.next=self.head
        self.head=nb
    def display(self):
        if self.head is None:
            print("Linked list is empty")
        else:
            temp=self.head
            while temp:
                 if temp.next!=None:
                    print(temp.data,end="--> ")
                 else:
                    print(temp.data,end=" ")
                 temp=temp.next
                
obj=singlelinkedlist()
#Node creation-initialising
n=Node(10)# so n.data in Node class will be 10
obj.head=n#assigning first node as head
n1=Node(20)
obj.head.next=n1#next node value
n2=Node(30)
n1.next=n2
n3=Node(40)
n2.next=n3
n4=Node(50)
n3.next=n4
print("Before inserting 100")
obj.display()
print('')
print("After inserting 100")
obj.insert_begining(100)
obj.display()
print('')
print("After inserting 555")
obj.insert_begining(555)
obj.display()

