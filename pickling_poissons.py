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
    
  for i in nums.values():
    if min(i)>=n>=max(i):
      return 
  temp=po(n)
  nums.update({temp:nums[temp]+[n]})
  f.dump(nums,"pickledump%i"%(l))
  return temp
