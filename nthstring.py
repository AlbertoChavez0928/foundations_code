import numpy as np
import itertools
from scipy import interpolate as itt
import math

class Word():  
  
    def __init__(self,my_alphabet): 
        
        self.my_alphabet=my_alphabet
        self.alpa_length=len(my_alphabet)
        self.word=[]
        self.wordcount=[]
        self.acceptance=False
        
        
        
        
        
    def cartesian_product(self,numspaces,temp,localindex):
        lis=self.my_alphabet
        newseed=[]
        for l in lis:
            for b in temp:
                newseed.append(l+b)
        if(numspaces>len(newseed[0])):
            self.cartesian_product(numspaces,newseed,localindex)
        else:
            print(newseed[localindex])
        
        
        
    
    def get_nth_string(self,n):
        numspaces = 0
        Sum=0
        if(n==0):
            print("blank")
            return
        else:
            a=1
            r=self.alpa_length
            while (Sum+a)<= n : 
                Sum = Sum + a
                a = a * r 
                numspaces+= 1
                localindex=n-Sum
            
            print("this num  "+str(n)+" has depth of",numspaces)
            word=[]
            j=len(self.my_alphabet)
            list1=self.my_alphabet
            if(n>j):
                self.cartesian_product(numspaces,list1,localindex)
            else:
                print(self.my_alphabet[n-1])
        
