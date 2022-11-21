class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for token in tokens:
            if token.lstrip('-').isdigit():
                stack.append(int(token))
            else:
                num = stack.pop()
                if token == '+':
                    stack[-1] += int(num) 
                if token == '-':
                    stack[-1] -= int(num) 
                if token == '*':
                    stack[-1] *= int(num) 
                if token == '/':
                    stack[-1] = int(stack[-1] / num) 
        return stack[-1]