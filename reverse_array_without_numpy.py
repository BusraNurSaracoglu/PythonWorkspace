#!/bin/python3

import math
import os
import random
import re
import sys



if __name__ == '__main__':
    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

def Reverse():
    
    c = []

    for i in reversed (range(n)):  
        c.append(arr[i])

    for i in range(n):
        print(c[i], end =" ")
    return c
    
