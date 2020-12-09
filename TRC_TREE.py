import numpy as np
import itertools
from scipy import interpolate as itt
import math
import NFA
import TRIE

class trc_tree():  
  
    def __init__(self, my_nfa):
        
        
        self.root = my_nfa.start_state;
        self.trie = TRIE.Trie(chr(self.root))
        self.nfa=my_nfa
        self.treminating_states=[]
        for k in self.nfa.states:
            terminator=True
            for l in self.nfa.transition_function:
                if (l[0]==k):
                    terminator=False
            if (terminator):
                self.treminating_states.append(k)
                
                
        
        ''' not that word is actually the path or being built string is the true string you have given'''
    def fill_tree(self,node,word,visits,list_of_words,str_index,string_var,empt):
        
            
        if(empt):
            if(node in self.nfa.accept_states):
                list_of_words.append(word+" true")
            else:
                list_of_words.append(word+"false")
                
       
        if (str_index==len(string_var)):
            if(node in self.nfa.accept_states):
                list_of_words.append(word+" true")
            else:
                list_of_words.append(word+"false")
            return
        if(not empt):
            if (not((node,string_var[str_index])in self.nfa.transition_function)):
                list_of_words.append(word+"break")

        visits.append(node)
      
        for i in self.nfa.transition_function: 
                if (i[0]==node):
                    
                    if (i[1]==string_var[str_index] or i[1]=="blank"):
                        branchextension=(i)
                        possible_locations=[]
                        possible_locations=self.nfa.transition_function.get(branchextension)
                 
                        for j in possible_locations:
                                
                                ctf=str(i[1])
                                if(i[1]=="blank"):
                                    if(j not in visits):
                                        newpart=("\'€\'"+"-->"+str(j))
                                        newpart+="--"
                                        list_of_words.append(word+newpart)
                                        print(j,visits)
                                        self.fill_tree(j,(word+newpart),visits,list_of_words,str_index,string_var,empt)
                               
                                else:
                                    
                                    newpart=("\'"+str(i[1])+"\'-->"+str(j))
                                    newpart+="--"
                                    list_of_words.append(word+newpart)
                                    self.fill_tree(j,(word+newpart),visits,list_of_words,str_index+1,string_var,empt)
                             
                                
                        
                        
        return list_of_words                
    def bt(self,node,word,visits,str_index,string_var,empt,return_t):    
            if(empt):
                if(node in self.nfa.accept_states):
                    print("found")
                    l=(word+" true")
                    return l
                else:
                    return ("")
    
                
       
            if (str_index==len(string_var)):
                if(node in self.nfa.accept_states):
                        return_t=(word+" true")
                        return return_t
                else:
                    return ""
                    
            
            visits.append(node)
            for i in self.nfa.transition_function: 
                    if (i[0]==node):
                        
                        if (i[1]==string_var[str_index] or i[1]=="blank"):
                        
                            branchextension=(i)
                            possible_locations=[]
                            possible_locations=self.nfa.transition_function.get(branchextension)
                        
                            for j in possible_locations:
                                if(i[1]=="blank"):
                                    if(j not in visits):
                                        newpart=("\'€\'"+"-->"+str(j))
                                        newpart+="--"
                                        l=self.bt(j,(word+newpart),visits,str_index,string_var,empt,return_t)
                                        if (l):
                                            return l
                                else:
                                    newpart=("\'"+str(i[1])+"\'-->"+str(j))
                                    newpart+="--"
                                    l=self.bt(j,(word+newpart),visits,str_index+1,string_var,empt,return_t)
                                    if (l):
                                        return l
            return ""
    def get_tree(self,string1,back_track):
        empt=False
        if(string1==""):
            string1=" "
            empt=True
            
        if(back_track):
            
            self.trace=self.bt(self.root,str(self.root)+"--",[],0,string1,empt,"")
            if(self.trace):
                print("found a trace",self.trace)
            else:
                print("no trace found")
        else:    
            self.trace=self.fill_tree(self.root,str(self.root)+"--",[],[],0,string1,empt)
            counter=0
            print("generating traces for string\"",string1,"\"")
            for i in self.trace:
                temp=i[-5:]
                if(temp==" true" or temp=="false"or temp=="break"):
                    self.trie.insert(i)
                    counter=counter+1
                    print("tace number:",counter,"")
        self.trace=[]
        
    def fork_tree(self,string1):
        empt=False
        if(string1==""):
            string1=" "
            empt=True
        self.trace=self.fill_tree(self.root,str(self.root)+"--",[],[],0,string1,empt)
        counter=0
        print("generating traces for string\"",string1,"\"")
        for i in self.trace:
            temp=i[-5:]
           
            if(temp==" true" or temp=="false"):
                print(i)
                self.trie.insert(i)
                counter=counter+1
                print("tace number:",counter,"")
        self.trace=[]
        
        