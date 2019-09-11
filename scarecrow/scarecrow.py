#!/usr/local/bin/python3
""" 
Contest Problem 2
Protecting the crops.
"""
import sys

class ScarecrowPlacer(object):
    def __init__(self):
        self.HEALTHY = '.'
        self.INFERTILE = '#'

    def solve(self, fieldSize, fieldDesc):
        count = 0
        skip = 0
        for fType in fieldDesc:
            if fType == self.HEALTHY and skip == 0:
                skip = 2
                count += 1
            else:
                if skip > 0:
                    skip -= 1
        return count

    def solveFromInput(self, testCases):
        for i in range(testCases):
            fieldSize = int(sys.stdin.readline())
            fieldDesc = list(sys.stdin.readline())
            result = self.solve(fieldSize, fieldDesc)
            print("Case " + str(i + 1) + ":", result)

if __name__ == "__main__":
    testCases = int(sys.stdin.readline())
    placer = ScarecrowPlacer()
    placer.solveFromInput(testCases)