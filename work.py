class Node:
    def __init__(self,data):
        self.data = data
        self.next = None
        
class linkedlist:
    def __init__(self):
        self.head = None
    
    def display(self):
        itr = self.head
        while itr:
            print(itr.data, end="-->")
            itr = itr.next
        print("None")
    
    def insert_position(self,pos,data):
        new=Node(data)
        
        itr=self.head
        for i in range(pos-2):
            itr=itr.next
        
        new.next=itr.next
        itr.next=new
        
l1=linkedlist()

l1.head=Node(10)
l1.head.next=Node(20)
l1.head.next.next=Node(30)
print("Before:")
l1.display()l1.insert_position(3,40)
print("After:")
l1.display()
-----------------------------------------------------------------------------------------------
class Node:
    def __init__(self,data):
        self.data = data
        self.next = None
        
class linkedlist:
    def __init__(self):
        self.head = None
    
    def display(self):
        itr = self.head
        while itr:
            print(itr.data, end="-->")
            itr = itr.next
        print("None")
    
    def remove_value(self,value):
        if self.head.data==value:
            self.head=self.head.next
            return
        itr=self.head
        
        while itr.next:
            if itr.next.data == value:
                itr.next = itr.next.next
                return
            itr=itr.next
                
               
l1=linkedlist()

l1.head=Node(10)
l1.head.next=Node(20)
l1.head.next.next=Node(30)
l1.head.next.next.next=Node(40)
print("Before:")
l1.display()
l1.remove_value(20)
print("After:")
l1.display()
-----------------------------------------------------------------------------------
class Node:
    def __init__(self,data):
        self.data=data
        self.next=None

head=Node(10)
second=Node(20)
third=Node(30)
fourth=Node(40)

head.next=second
second.next=third
third.next=fourth
fourth.next=second

slow=head
fast=head

flag=False

while fast and fast.next:
    slow=slow.next
    fast=fast.next.next

    if slow==fast:
        flag=True
        break

print(flag)
-------------------------------------------------------------------------------------------------
class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
    
class linkedlist:
    def __init__(self):
        self.head = None
    
    def display(self):
        itr = self.head
        while itr:
            print(itr.data, end="-->")
            itr = itr.next
        print("None")

l1=linkedlist()

l1.head=Node(10)
l1.head.next=Node(20)
l1.head.next.next=Node(30)
l1.head.next.next.next=Node(40)
l1.head.next.next.next.next=Node(50)

slow=l1.head
fast=l1.head

while fast and fast.next:
    slow=slow.next
    fast=fast.next.next

print("Middle =",slow.data)
----------------------------------------------------------------------------------------------
class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
     
class linkedlist:
    def __init__(self):
        self.head = None
    
    def display(self):
        itr = self.head
        while itr:
            print(itr.data, end="-->")
            itr = itr.next
        print("None")     
l1=linkedlist()    
l1.head=Node(10)
l1.head.next=Node(20)
l1.head.next.next=Node(30)
prev=None
curr=l1.head
while curr:
    nxt=curr.next
    curr.next=prev
    prev=curr
    curr=nxt

l1.head=prev
itr=l1.head

while itr:
    print(itr.data,end=" -> ")
    itr=itr.next

print("None")
---------------------------------------------------------------------------------------
class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
        
class linkedlist:
    def __init__(self):
        self.head = None
    
    def display(self):
        itr = self.head
        while itr:
            print(itr.data, end="-->")
            itr = itr.next
        print("None")   
    
l1=linkedlist()

l1.head=Node(10)
l1.head.next=Node(20)
l1.head.next.next=Node(30)
l1.head.next.next.next=Node(20)
l1.head.next.next.next.next=Node(10)

seen=set()
dup=set()

itr=l1.head
while itr:

    if itr.data in seen:
        dup.add(itr.data)
    else:
        seen.add(itr.data)
    itr=itr.next
print("Duplicates =",dup)