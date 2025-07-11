def solution(s):
    stack = []
    
    for bracket in s:
        if bracket == '(':
            stack.append(bracket)
        elif bracket == ')':
            if not stack:
                return False
            stack.pop()
                
    if not stack:
        return True
    return False
