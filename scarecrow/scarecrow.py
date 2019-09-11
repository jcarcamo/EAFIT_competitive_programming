#!/usr/local/bin/python3
""" 
Contest Problem 2
Protecting the crops.
"""
import sys

class ScarecrowPlacer(object):
    def solve(self, fieldSize, fieldDesc):
        return "Coming soon"

    def solveFromInput(self, testCases):
        for i in range(testCases):
            fieldSize = int(sys.stdin.readline())
            fieldDesc = list(sys.stdin.readline())
            result = self.solve(fieldSize, fieldDesc)
            print("Case " + i + ":", result)

if __name__ == "main":
    placer = ScarecrowPlacer()
    testCases = int(sys.stdin.readline())
    placer.solveFromInput(testCases)