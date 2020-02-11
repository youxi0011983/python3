#!/usr/bin/env python3

class MyNumbers:
  def __iter__(self):
    self.a = 1
    return self
 
  def __next__(self):
    if self.a <= 20:
      x = self.a
      self.a += 1
      return x
    else:
      raise StopIteration("It's  going to loop...")
 
myclass = MyNumbers()
myiter = iter(myclass)
 
for x in myiter:
  print(x)