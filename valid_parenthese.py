class py_solution:
    def is_valid_parenthese(self, str1):
        stack = []
        pchar = {"(":")","{":"}","[":"]"}
        
        for i in str1:
            if i in pchar:
                stack.append(i)
            elif len(stack) == 0 or pchar[stack.pop()] != i:
                return False
        return len(stack) == 0
    
print(py_solution().is_valid_parenthese("(){}[]"))
print(py_solution().is_valid_parenthese("()[{)}"))
print(py_solution().is_valid_parenthese("()"))
