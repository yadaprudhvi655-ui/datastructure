class Node:
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
ll.display()            
            