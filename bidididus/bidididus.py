#!/usr/local/bin/python3
""" 
Contest Problem 1
Global Raining Problem Solution.
"""
import sys

class GlobalRaining(object):
    
    def iterativeSolve(self, str):
        stack = []
        result = 0
        x = 0
        y = 0
        for c in str:
            if c == '\\':
                stack.append((x,y))
                y -= 1
            if c == '/':
                if len(stack) != 0:
                    xTemp, yTemp = stack[-1]
                    if  y < yTemp:
                        stack.pop()
                        result += x - xTemp
                y += 1
            x += 1
        return result


    def solveFromFile(self, file):
        with open(file) as f:
            size = int(f.readline())
            for i in range(size):
                word = list(f.readline())
                result = self.iterativeSolve(word, 0)
                print(result)

    def solveFromInput(self, size):
        for i in range(size):
            word = list(sys.stdin.readline())
            result = self.iterativeSolve(word)
            print(result)

if __name__ == "__main__":
    size = int(sys.stdin.readline())
    g = GlobalRaining()
    g.solveFromInput(size)