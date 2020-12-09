import numpy as np
import itertools
from scipy import interpolate as itt
import math

class nfa():  
  
    def __init__(self, states, alphabet, transition, start_state, accept_states):
        
        
        self.states = states;
        self.alphabet = alphabet;
        self.transition_function = transition;
        self.start_state = start_state;
        self.accept_states = accept_states;
        self.current_state = start_state; 
        self.epsilon_states=[]

       
                        
                        
        
                        
            
    
    def oracle(self,current_state,trace,word,n,k,boole):        
        
        
        if(k==len(trace)):
            print("this trace works ")
            if (current_state in  self.accept_states):
                return (boole and True)
        
            else:
                return (boole and False)
         
            
            
        possible_locations=[]
        for i in self.transition_function:
            if i[0]==current_state and i[1]==word[n]:
                    possible_locations=self.transition_function.get(i)

        if ((current_state,"blank")  in transition_function ):
            possible_locations.append(self.transition_function.get((current_state,"blank")))
            xx=1
        for j in possible_locations:
            if j==trace[k+1]:
                xx=0
             
                if(self.transition_function.get(current_state,"blank")==j):
                     oracle(self,current_state,path,word,n,k+1,boole)
                else:
                     oracle(self,current_state,path,word,n+1,k+1,boole)                
            if (xx==1):
                                      return(False)
        return
    
        
    
   