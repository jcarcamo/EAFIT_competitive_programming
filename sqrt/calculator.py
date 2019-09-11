#!/usr/local/bin/python3
""" 
Contest Problem 3
Protecting the crops.
"""
import sys
import math

class Calculator(object):

    def divideIntoPairs(self, digits):
        pairs = []
        for i in range(len(digits) - 1, -1, -2):
            if i-1 >= 0:
                pairs.append(digits[i-1] + digits[i])
            elif i == 0:
                pairs.append(digits[i])
        return pairs

    def sqrt(self, y):
        # 1. divide number in pairs
        pairs = self.divideIntoPairs(list(y.rstrip()))
        # 2. find the smallest integer that squared is the leftmost digit
        pair = int(pairs.pop())
        n = 0
        while (n+1)**2 <= pair:
            n += 1
        # 3. add that number to our result
        result = str(n)
        doubleResult = int(result)*2
        substraction = pair - doubleResult
        
        # 4. The loop starts here. 
        # Multiply result by 2 and substract it from the prev number
        while len(pairs) != 0:
            pair = pairs.pop()
            temp = int(str(substraction) + pair)
            # 5. Find the int that satisfies concat(result*2,x)*x < temp
            x = 0
            doubleResult = str(int(result)*2)
            while int(doubleResult + str(x+1))*(x+1) < temp:
                x += 1
            
            toSubstract = int(doubleResult + str(x))*(x)
            result += str(x)
            substraction = temp - toSubstract

        return int(result)

    def solveFromInput(self, testCases):
        for i in range(testCases):
            empty = sys.stdin.readline()
            y = sys.stdin.readline()
            result = self.sqrt(y)
            mathOp = int(math.sqrt(int(y)))
            if result == mathOp:
                print('\n',result)
            else:
                print('\n', "ERROR -- math result:", mathOp, "our result:", result)

if __name__ == "__main__":
    testCases = int(sys.stdin.readline())
    calc = Calculator()
    calc.solveFromInput(testCases)