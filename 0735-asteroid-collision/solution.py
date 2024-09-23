class Solution:
    def asteroidCollision(self, asteroids):
        stack = []
        for asteroid in asteroids:
            while stack and asteroid < 0 and stack[-1] > 0:
                if abs(stack[-1]) < abs(asteroid):
                    stack.pop()  
                elif abs(stack[-1]) == abs(asteroid):
                    stack.pop() 
                    break  
                else:
                    break  
            else:
                stack.append(asteroid)
        return stack
