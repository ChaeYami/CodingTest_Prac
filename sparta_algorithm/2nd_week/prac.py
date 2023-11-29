'''연결리스트 예제 - 팰린드롬'''

def isPalindrome(ln): # 연결리스트를 전달받아서
    arr = []
    head = ln.head #헤드를 꺼내 

    if not head: #헤드가 없으면 비어있으므로
        return True

	# 헤드가 있으면
    node = head
    while node: # 노드를 옮겨가며 연결리스트의 모든 값을 리스트에 넣는다.
        arr.append(node.val)
        node = node.next

    while len(arr) > 1: # 길이가 1이 될 때 까지
	    # 첫 번째 요소와 마지막 요소를 꺼낸다.
        first = arr.pop(0)
        last = arr.pop()
        if first != last: # 다르면 팰린드롬이 아님
            return False

    return True


'''Stack 예제 - 유효한 괄호'''

def test_problem_stack(s):
    pair = {
        '}': '{',
        ')': '(',
        ']': '[',
    }
    opener = "({["
    stack = []

    for char in s:
        if char in opener:
            stack.append(char)
        else:
            if not stack:
                return False
            top = stack.pop()
            if pair[char] != top:
                return False

    return not stack


'''Queue 예제 - 줄서기'''

from collections import deque

def test_problem_queue(n):
    deq = deque([i for i in range(1, n + 1)])
    
    while len(deq) > 1: # 요소가 2개 이상 남아있는 동안 (하나 남을 때 까지)
        deq.popleft() # deque의 앞에서 꺼낸다.
        deq.append(deq.popleft()) # 두번째는 앞에서 꺼내서 맨뒤에 붙인다.
    return deq.popleft()