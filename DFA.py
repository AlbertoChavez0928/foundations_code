import numpy as np
import itertools
from scipy import interpolate as itt
import math

class dfa():  
  
    def __init__(self, states, alphabet, transition, start_state, accept_states):
        
        
        self.states = states;
        self.alphabet = alphabet;
        self.transition_function = transition;
        self.start_state = start_state;
        self.accept_states = accept_states;
        self.current_state = start_state;
        self.path=[]
        self.from_list=[]
        for x in self.states:
            templist=[x]
            for i in self.transition_function: 
                if x==self.transition_function.get(i):
                    if i not in templist:
                        node=(i[0],False)
                        templist.append(node)
                        
            res = [] 
            [res.append(x) for x in templist if x not in res]  
            self.from_list.append(templist)
            templist=[]
    
    def step(self,current_state,path,word):        
        if current_state in self.accept_states:
            print("this is the correct word",word)
            return(True)
        
        if current_state not in path:
            path.append(current_state)
        possible_locations=[]
        for i in self.transition_function:
            print("i",i[0],current_state)
            if i[0]==current_state:
                    print("n ")
                    possible_locations.append(i)
        for j in possible_locations:
                print("j",self.transition_function.get(j))
                if (self.transition_function.get(j) not in path):
                    chrr=j[1]
                    word+=chrr
                    print(word)
                    ("next location is ",self.transition_function.get(j))
                    n=self.step(self.transition_function.get(j),path,word)
                    if(n):
                        return(True)      
        if (current_state==self.start_state):
            print("no good strings ")
        return(False)
    
        
    def forward(self,node,trail):
        print("check",trail)
        trail.append(node)
        for i in self.transition_function: 
                if (i[0]==node[0]): 
                    print(self.transition_function.get(i))
                    if not(i in  trail):

                        self.forward(([self.transition_function.get(i),""]),trail)
                    
                        if (self.transition_function.get(i) in self.accept_states):
                            print("passed",trail)
                            trail.pop()
                            
                            return True         
        print("fail") 
        return False
            
    def dfa_reverse(self):
        for x in self.accept_states:
            for j in self.from_list:
                if j[0]==x:
                    p=self.step(j,[])
                    print (p)
    def get_path(self):
        print(self.path)
    def dfa_Traverse(self,input_string):
        i=0
        self.path=[]
        if(len(input_string)):
            tempc=input_string[i] 
            while(len(input_string)>i):
                tempc=input_string[i]
            #trasnifiton function is a dict
                self.path+=(self.current_state,tempc)
                self.current_state =self.transition_function[self.current_state,tempc]
                i+=1
        else:
            input_string="blank"         
        if self.current_state in self.accept_states:
            print("true")
            self.path+=("last state of",input_string,self.current_state)
            self.current_state = self.start_state
            return (True)
            
        else:
            print("false")
            self.path+=("last state",input_string,self.current_state)
            self.current_state = self.start_state
            return (False)
        
        
        