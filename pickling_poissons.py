import os
import pickle

initialised=False

def checking(n,l):
  if not initialised:
    if os.path.exists("pickledump%i"%(l)):
      f=open("pickledump%i"%(l),"r+")
      nums=f.load
    else:
      f=open("pickledump%i"(l),"w+")
      nums={}
    initialised=True
    
  if n in nums:
    return nums[n]
  temp=po(n)
  nums.update({n:temp})
  f.dump(nums,"pickledump%i"%(l))
  return temp
