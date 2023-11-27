from structures import LinkedList, Stack, Queue
from prac import isPalindrome, test_problem_stack, test_problem_queue

'''LinkedList'''

l1 = LinkedList() # 1->2->2->1
for num in [1, 2, 2, 1]:
    l1.append(num)

l2 = LinkedList()
for num in [1, 2]:
    l2.append(num)


assert isPalindrome(l1) # assert 뒤의 값을 true로 확언하겠다 (true가 맞는지 test하는 것)
assert not isPalindrome(l2) # assert not 뒤의 값을 false로 확언하겠다 (false 가 맞는지 test하는 것)


'''Stack'''

def test_stack():
    stack = Stack()

    stack.push(1)
    stack.push(2)
    stack.push(3)
    stack.push(4)
    stack.push(5)
    '''
    현재 스택
    5
    4
    3
    2
    1
    '''
	# 스택에서 pop 하면 제일 위에 거 (마지막 거이기 때문에)
    assert stack.pop() == 5
    assert stack.pop() == 4
    assert stack.pop() == 3
    assert stack.pop() == 2
    assert stack.pop() == 1
    assert stack.pop() is None
    assert stack.is_empty()


'''Stack 예제 - 유효한 괄호'''
assert test_problem_stack("()")
assert test_problem_stack("()[]{}")
assert test_problem_stack("({[][]})")
assert test_problem_stack("({[]})")
assert not test_problem_stack("(]")
assert not test_problem_stack("(()]")
assert not test_problem_stack("(((])")
assert not test_problem_stack("((())")


'''Queue'''

def test_queue():
    queue = Queue()

    queue.push(1)
    queue.push(2)
    queue.push(3)
    queue.push(4)
    queue.push(5)

    assert queue.pop() == 1
    assert queue.pop() == 2
    assert queue.pop() == 3
    assert queue.pop() == 4
    assert queue.pop() == 5
    assert queue.pop() is None
    assert queue.is_empty()
    
    
test_queue()

'''Queue 예제 - 줄서기'''

assert test_problem_queue(2) == 2
assert test_problem_queue(3) == 2
assert test_problem_queue(4) == 4
assert test_problem_queue(5) == 2
assert test_problem_queue(6) == 4
assert test_problem_queue(7) == 6