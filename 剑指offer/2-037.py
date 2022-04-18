class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stack = []
        for cur_ast in asteroids:
            while stack and stack[-1] > 0 and cur_ast < 0:
                pre_ast = stack.pop()
                if abs(pre_ast) > abs(cur_ast):
                    stack.append(pre_ast)
                    cur_ast = 0
                    break
                elif abs(pre_ast) == abs(cur_ast):
                    cur_ast = 0
                    break
            if cur_ast:
                stack.append(cur_ast)
        return stack
