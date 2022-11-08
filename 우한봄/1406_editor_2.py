import sys

class DList:
    class Node:
        """
        각 element(문제에서는 str 값)을 표현하는 노드 초기화 설정
        """
        def __init__(self,item,prev,next):
            self.item=item
            self.prev=prev
            self.next=next
    
    def __init__(self):
        self.head=self.Node(None,None,None)
        self.tail=self.Node(None,self.head,None)
        self.head.next=self.tail
        self.cur=self.tail # 커서 초기화 설정
    
    def insert(self, p, item):
        # [p.prev->p] => [p.prev->n->p]
        t=p.prev
        n=self.Node(item, t,p)
        p.prev=n
        t.next=n
    
    def delete(self,x):
        # [f->x->r] => [f->r]
        f=x.prev
        r=x.next
        f.next=r
        r.prev=f    
    
    def print_list(self):
        p=self.head.next
        while p!=self.tail:
            if p.next != self.tail:
                print(p.item, end="")
            else:
                print(p.item)
            p=p.next   
            
s=list(sys.stdin.readline().strip()) 
dl=DList()

for i in range(len(s)):
    dl.insert(dl.tail, s[i])

# print(dl)
# print(dl.head.item)
# print(dl.head.next.item)
# print(dl.tail.item)

for i in range(int(sys.stdin.readline())):
    command=list(sys.stdin.readline().split())
    if command[0]=="L":
        if dl.cur.prev.prev != None: 
            # head.next 노드(맨 왼쪽)이면 무시
            dl.cur=dl.cur.prev
    elif command[0]=="D":
        if dl.cur.next!=None:
            # tail.prev(맨 오른쪽)이면 무시
            dl.cur=dl.cur.next
    elif command[0]=="B":
        if dl.cur.prev.prev != None: 
            dl.delete(dl.cur.prev)
    else:
        dl.insert(dl.cur, command[1])
        
dl.print_list()
        
        
        