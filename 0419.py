# isdigit 사용
def solution(my_string):
    nums = []
    for i in my_string:
        if i.isdigit():
            nums.append(int(i))
    return sorted(nums)

# isnumeric 사용
def solution(my_string):
    nums = []
    for i in my_string:
        if i.isnumeric():
            nums.append(int(i))
    return sorted(nums)


# try-except 사용
def solution(my_string):
    nums = []
    for i in my_string:
        try:
            nums.append(int(i))
        except:
            continue
    
    return sorted(nums)
        


'''
isdigit : 
isnumeric : 
'''

print(solution("hi12392"))
'''
num = '-3'
a = num.isdigit()
print(a) # False

num = '3'
b = num.isdigit()
print(b) # True

num = 'adfe'
c = num.isdigit()
print(c) # False

num = '-3'
d = num.isnumeric()
print(d) # False
'''