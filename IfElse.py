#!/bin/python3

import math
import os
import random
import re
import sys



if __name__ == '__main__':
    n = int(input().strip())
    assert (n>1)
    even = lambda x:print("Not Weird") if (x in range(6)) else print("Weird") if(x in range(21))else print("Not Weird")
    odd=lambda x: print("Weird") if x%2!=0 else even(x)
    odd(n)