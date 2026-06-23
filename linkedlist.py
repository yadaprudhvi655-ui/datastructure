"""class Node:
    def __init__(self,data):
        self.data=data
        self.next=None

class Linkedlist:
    def __init__(self):
        self.head=None

    def add_end(self,data):
        new=Node(data)
        if self.head is None:
            self.head=new
            return

        itr=self.head
        while itr.next:
            itr=itr.next
        itr.next=new

    def display(self):
        itr=self.head
        while itr:
            print(itr.data,end="-->")
            itr=itr.next

ll=Linkedlist()
ll.add_end(50)
ll.add_end(100)
ll.add_end(150)
ll.add_end(200)
ll.display()"""           
#wap to find the middle point of a linkedlist using slow and faster            
class Node:
    def  __init__(self,data):
        self.data=data
        self.next=None
class Linkedlist:
    def __init__(self):
        self.head=None

    def add_end(self,data):
        new=Node(data)
        if self.head is None:
            self.head=new
            return   
        itr=self.head  
        while itr.next:
            itr=itr.next
        itr.next=new
    def middle(self):
        slow = self.head
        fast = self.head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        print("Middle element =", slow.data) 
     
    def display(self):
        itr=self.head
        while itr:
            print(itr.data,end="-->")
            itr=itr.next    

ll=Linkedlist()
ll.add_end(50)
ll.add_end(100)
ll.add_end(150)
ll.add_end(200)
ll.middle()
ll.display()
#remove element from start/end of ll
#add an ele at a given position
#remove any 2 nodes from ll
#finding a loop in ll
#slow and fast pointer
#reverse a single ll
#find out duplicates in ll
