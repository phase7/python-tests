#!/usr/bin/env python
# coding: utf-8

# In[36]:


from math import gcd
def lcm(a, b):
        return (a * b) // gcd(a, b)
class fraction:
    def __init__(self, top, bottom ):
        self.num = top
        self.den = bottom
    def __str__(self):
        if (self.den == 1): return str(int(self.num))
        ret = str((self.num)) + "/" + str((self.den))
        return ret
    def __add__(self, ob):
        if isinstance(ob, fraction):
            denm = lcm(self.den, ob.den)
            nume = denm//self.den*self.num + denm//ob.den*ob.num
            
            gcdb = gcd((denm), (nume))
            
            denm = denm//gcdb
            nume = nume // gcdb
            return self.__class__(nume, denm)

var1 = fraction(1,60)
print(var1)

var2 = fraction(6,360)
print(var2)

var3 = var1+ var2
print(var3)


# In[37]:


print(fraction(89,1))

