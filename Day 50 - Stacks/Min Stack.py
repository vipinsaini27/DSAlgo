"""
Problem Description
Design a stack that supports push, pop, top, and retrieve the minimum element in constant time.
push(x) -- Push element x onto stack.
pop() -- Removes the element on top of the stack.
top() -- Get the top element.
getMin() -- Retrieve the minimum element in the stack.
NOTE:
All the operations have to be constant time operations.
getMin() should return -1 if the stack is empty.
pop() should return nothing if the stack is empty.
top() should return -1 if the stack is empty.

Problem Constraints
1 <= Number of Function calls <= 107

Input Format
Functions will be called by the checker code automatically.

Output Format
Each function should return the values as defined by the problem statement.

Example Input
Input 1:
push(1)
push(2)
push(-2)
getMin()
pop()
getMin()
top()

Input 2:
getMin()
pop()
top()

Example Output
Output 1:
 -2 1 2
Output 2:
 -1 -1

Example Explanation
Explanation 1:
Let the initial stack be : []
1) push(1) : [1]
2) push(2) : [1, 2]
3) push(-2) : [1, 2, -2]
4) getMin() : Returns -2 as the minimum element in the stack is -2.
5) pop() : Return -2 as -2 is the topmost element in the stack.
6) getMin() : Returns 1 as the minimum element in stack is 1.
7) top() : Return 2 as 2 is the topmost element in the stack.
Explanation 2:
Let the initial stack be : []
1) getMin() : Returns -1 as the stack is empty.
2) pop() :  Returns nothing as the stack is empty.
3) top() : Returns -1 as the stack is empty.
"""

"""
Solution Approach
What if you maintained the current minimum in a variable and only stored the places where the 
minimum changes or the element is the same as the minimum.
pop() becomes a little trickier in such a case.
You only pop() from the min stack if the top() of the min stack is the same as the current 
minimum.
Space complexity: O(N + X) where X = number of places where minimum changes or the element is 
the same as the minimum.
"""

class MinStack:
    
    def __init__(self):
        self.stack = []
        self.minStack = []
    
    def push(self, x):
        minElem = self.getMin()
        if minElem != -1:
            if minElem > x:
                self.pushMinStack(x)
        else:
            self.pushMinStack(x)

        self.stack.append(x)

    def pushMinStack(self, x):
        self.minStack.append(x)

    def popMinStack(self):
        if len(self.minStack) > 0:
            return self.minStack.pop()

        return -1

    def topMinStack(self):
        if len(self.minStack) > 0:
            return self.minStack[-1]

        return -1

    # @return nothing
    def pop(self):
        minStackTop = self.topMinStack()
        stackTop = self.top()

        if minStackTop != -1 and stackTop != -1:
            if minStackTop == stackTop:
                self.popMinStack()
            return self.stack.pop()


    # @return an integer
    def top(self):
        if len(self.stack) > 0:
            return self.stack[-1]
        
        return -1

    # @return an integer
    def getMin(self):
        if len(self.minStack) > 0:
            return self.minStack[-1]
        return -1
