# https://www.acmicpc.net/problem/4949
import sys
test_input = sys.stdin.readline()

while True:
    input_string = input()
    bracket_dict={
            ')' : '(',
            ']' : '['
            }
    result = '' 
    stack=[]
    if input_string == '.':
        break
    else:
        
        for str in input_string:
            if str in bracket_dict.values():
                stack.append(str)
            elif str in bracket_dict:
                if not stack:
                    result = 'no'
                else:
                    top = stack.pop()
                    if top != bracket_dict[str]:
                        result = 'no'
            
        if not stack and result != 'no':
            result = 'yes'
        else:
            result = 'no'

        print(result)

                          
        
            
# test("So when I die (the [first] I will see in (heaven) is a score list).")
# test("[ first in ] ( first out ).")
# test("Half Moon tonight (At least it is better than no Moon at all].")
# test("A rope may form )( a trail in a maze.")
# test("Help( I[m being held prisoner in a fortune cookie factory)].")
# test("([ (([( [ ] ) ( ) (( ))] )) ]).")
# test(" .")
