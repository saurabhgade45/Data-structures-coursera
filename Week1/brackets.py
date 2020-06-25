s = input()
stack = []
backup = []
def bracket(s):
    count = 0
    
    for char in s:
        count =count + 1
        if char =='(' or char =='{' or char =='[':
            stack.append(char)
            backup.append(count)
        elif char==')':
            if not stack:
                return count
            x = stack.pop()
            if x != '(':
                return count
            else:
                backup.pop()

        elif char ==']':
            if not stack:
                return count
            x = stack.pop()
            if x!= '[': 
                return count
            else:
                backup.pop()
            
        elif char =='}':
            if not stack:
                return count
            x = stack.pop()
            if x!= '{': 
                return count
            else:
                backup.pop()

    if backup:
        x = len(backup)
        x = x-1
        y = backup[x]
        return(y)       
    if stack:
        return count
    else:
        return("Success")
     
    print(stack)
        
print(bracket(s))