#!/usr/bin/env python
# coding: utf-8

# In[ ]:


def gap(g, m, n):
    def is_prime(num):
        if num<=1:
            return False
        if num ==2:
            return True
        if num%2==0:
            return False
        x = 3
        while x*x<=num and num%x!=0:
            x+=2
        return x*x>num
    def no_primes_between(i,g):
        for j in range(i+1,g+i):
            if is_prime(j):
                return False
        return True
            

    for i in range(m,n+1):
        if is_prime(i):
            if is_prime(i+g):
                if no_primes_between(i,g): 
                    return [i,i+g]
                else: pass

