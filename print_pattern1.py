# PROBLEM: Based on input param "count", print the pattern
"""
count = 3
*
**
***
**
*
"""
"""
count = 5
*
**
***
****
*****
****
***
**
*
"""
# SOLUTION: Using List comprehension, find the solution of increment and decrement and join them together.
print("\n".join(['*'*i for i in range(1,count+1)]) + "\n" + "\n".join(['*'*i for i in range(count-1,0,-1)]))

