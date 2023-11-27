'''LinkedList'''
'''
O -> O -> O -> O -> O -> O -> O
'''
class ListNode:
    def __init__(self, val = 0, next = None):
        self.val = val # 상자
        self.next = next # 화살표


class LinkedList:
    def __init__(self):
        self.head = None # 제일 첫 요소

    def append(self, val):
        if not self.head: # 헤드가 없다면
            self.head = ListNode(val, None) # 헤드 노드를 하나 만들고 다음거는 없다
            return

        node = self.head # 제일 앞을 노드로 설정
        while node.next: # 다음 요소가 있을 동안 (없을 때 까지)
            node = node.next # 노드를 다음걸로 업데이트

        node.next = ListNode(val, None) # 다음 요소 없으면 새로 만들기!
        
        
'''Stack'''

'''
연결리스트를 응용해서, 대신 제일 앞이 아니라 제일 위여야 하므로 가장 처음 걸 top으로 한다.
O 
↓
O
↓ 
O
↓ 
O
↓ 
O
형태가 된다.
'''
class Node:
    def __init__(self, val = 0, next = None):
        self.val = val #상자
        self.next = next # 화살표
        
class Stack:
    def __init__(self):
        self.top = None
        
    '''
    스택은 쌓으므로 append가 아닌 push, 
    연결리스트와 다른 점 : 새로 들어온 게 항상 top
    '''
    def push(self, val):
        # node = Node(val,None) : 새로 들어오면
        # node.next = self.top : 기존에 가장 위에(top)였던 애를 다음 노드로
        # self.top = node : 그리고 지금 새로 만든 노드를 top으로
        # 결국 val,next 에서 top 이었던 것을 next로 만드는 것이므로 한줄로 표현하면
        self.top = Node(val,self.top)
        
    
    def pop(self):
        if not self.top: # 없을 때
            return None # None을 넣어준다
        
        # pop 이므로 top 을 위에서 두번째걸로, 즉 다음걸로 바꿔줘야 함
        node = self.top 
        self.top = node.next
        # 그리고 선택된 노드(아직 제일 위에거이지만 top은 다음으로 넘겨준)를 반환한다.
        return node.val
        
    def is_empty(self):
        return self.top is None # pop 에서 넣어준 None 이 리턴되었다면 -> 없다면!
        
        
        
'''Queue'''

'''
노드 클래스는 연결리스트, 스택과 동일하다.
class Node:
    def __init__(self, val=0, next=None):
        self.val = val # 상자
        self.next = next # 화살표
'''

class Queue:
    def __init__(self):
        self.front = None # 가장 앞에 있는 게 중요하므로 front

    def push(self, value):
        if not self.front: # 맨 앞에가 없으면
            self.front = Node(value) # 노드 만들어서 front로
            return
            
		#맨 앞이 있으면
        node = self.front # 제일 앞 노드를 잡아서
        while node.next: # 다음 노드가 있는 동안 (다음 노드가 없을 때 까지)
            node = node.next # 다음 노드를 계속 잡는다. 
	    
        '''
	    다음 노드가 없으면 새로 상자를 만들어서 들어온 value를 대입, 
	    그리고 다음 노드로 가리키게 해준다(화살표를 만든다. next는 화살표를 의미함)
	    '''
        node.next = Node(value) 

    def pop(self):
        if not self.front: # 꺼낼 게 없으면
            return None

        node = self.front # 꺼낼 게 있으면 
        self.front = self.front.next # 맨 앞부터 (처음 넣은 것 부터) 꺼낸다.
        return node.val

    def is_empty(self):
        return self.front is None