class Solution:
    def decodeString(self, s: str) -> str:
        stack = []
        stack_k = []
        
        char = ''
        num = 0
        for c in s:
            if c == '[':
                stack.append(char)
                stack_k.append(num)
                char = ''
                num = 0
                continue
            elif c == ']':
                char = stack.pop() + char * int(stack_k.pop())
                continue
                
            if c.isdigit():
                num = num * 10 + int(c)            
            else:
                char += c
        return char
