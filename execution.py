#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the aVeryBigSum function below.
def aVeryBigSum(ar):
    A = ar.split('\n')[1].split()
    return sum(map(int, A))

if __name__ == '__main__':


    # ar = list(map(int, input().rstrip().split()))
    ar = """5
1000000001 1000000002 1000000003 1000000004 1000000005"""
    result = aVeryBigSum(ar)

    print(result)