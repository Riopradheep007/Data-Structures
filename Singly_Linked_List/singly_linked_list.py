

class Node:
    def __init__(self,data=None,next=None):
        self.data=data
        self.next=next
class LinkedList:
    def __init__(self):
        self.head=None
        
    def insert_at_begining(self,data):
        node=Node(data,self.head)
        self.head=node
        
    def print_data(self):
        if self.head is None:
            print("Linked list is empty")
            
        values=""
        itr=self.head
        while itr:
            values+=str(itr.data)+"-->"
            itr=itr.next
            
        print(values)
    def get_length(self):
        count=0
        itr=self.head
        while itr:
            itr=itr.next
            count+=1
 
        return count
        
        
    def remove_at(self,index):
        if index<0 or index>=self.get_length():
            print("INdex not found")
        if index==0:
            self.head=self.head.next
            
        
        count=0
        itr=self.head
        while itr:
            if count==index-1:
                itr.next = itr.next.next
                break

            itr = itr.next
            count+=1
    def insert_at(self,data,index):
        if index<0 and index>=self.get_length():
            print("please enter the correct index")
        if index==0:
            self.insert_at_begining(data,self.head)
        itr=self.head
        count=0
        while itr:
            if count==index-1:
                node=Node(data,itr.next)
                itr.next=node
                break
            itr=itr.next
            count+=1
    def insert_at_end(self,data):
        if self.head==None:
            node=Node(data,self.head)
            node.next=None
            
        itr=self.head
        
        while itr.next:
            itr=itr.next
        itr.next=Node(data,None)
        

if __name__ == '__main__' :
    
    ll=LinkedList()
    ll.insert_at_begining(5)
    ll.insert_at_begining(7)
    ll.insert_at_begining(8)
    ll.insert_at_begining(9)
    ll.print_data()
    ll.get_length()
    ll.remove_at(1)
    ll.insert_at(12,1)
    ll.insert_at_end(10)
    ll.print_data()
