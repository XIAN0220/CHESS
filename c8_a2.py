# -*- coding: utf-8 -*-
"""C8_A2.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1lXQ5ZQYvHG2JAjdzXHXleRlFSb7uNfSJ
"""

def calculate_fibonacci(number):
  x = [1,1]
  for i in range(0,number-2):
    x.append(x[i]+x[i+1])
  return int(x[number-2])
