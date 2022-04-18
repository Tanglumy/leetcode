class Solution:
    
    def evalRPN(self, tokens: List[str]) -> int:
        op_to_binary_fn = {
            "+": lambda x,y:x+y,
            "-": lambda x,y:x-y,
            "*": lambda x,y:int(x*y),
            "/": lambda x, y: int(x / y),
        }
        stack = []
        n = len(tokens)
        result = 0
        for i in range(n):
            if tokens[i] in op_to_binary_fn:
                x1 = stack.pop()
                x2 = stack.pop()
                result = op_to_binary_fn[tokens[i]](x2,x1)
                stack.append(int(result))
            else:
                stack.append(int(tokens[i]))
        return stack[0]
                