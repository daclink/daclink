from random import choice
import sys
sys.setrecursionlimit(2500)
from time import sleep


def recursiveWalk(left=-42,start=0,right=42, steps=0):
  leftoffset = abs(left) + start
  rightoffset = right - start
  leftoffset = "-"*leftoffset
  rightoffset = "-"*rightoffset
  print(f"{left} {leftoffset} {start: 3} {rightoffset} {right}")
  sleep(0.02)
  if start <= left:
    return steps
  elif start >= right:
    return steps
  else:
    start = start + choice([-1,1])
    return recursiveWalk(left,start,right,steps+1)

for x in range(5,50,2):
  print("steps:", recursiveWalk((-1*x),0,x))
  sleep(x/50)
