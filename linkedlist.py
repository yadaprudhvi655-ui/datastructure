class Node:
    def _init_(self):
        self.data=None
        self.next=None
class Linkedlist:
    def _inti_(self):
        self.head=None
    def add_end(self.data):
        new=Node(data)
        if self.head is None:
            self.head=new                
        itr=self.head()
        while itr.next:
            itr=itr.next
        itr.next=new
            