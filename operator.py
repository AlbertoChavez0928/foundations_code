import DFA


def getinv(mydfa):
    
    nac=[]
    ac=mydfa.accept_states
    for i in mydfa.states :
        if i not in ac :
            nac.append(i)
            
    
    
    dfa2=DFA.dfa(mydfa.states,mydfa.alphabet,mydfa.transition_function,mydfa.start_state ,nac)  
    print("old",mydfa.accept_states)
    print("bold",dfa2.accept_states)

    return dfa2



def union(dfa1,dfa2,intersect=0,getunion=1):
    if (dfa1.alphabet !=  dfa1.alphabet):
        print("error must contain synonymous alphabets")
        return
    
    new_states=[]
    word1=""
    word2=""
    new_ac=[]
    newtf=dict()  
    newstart=""
    for keys1 in dfa1.transition_function:
        value1=dfa1.transition_function.get(keys1)
        for keys2 in dfa2.transition_function:
            value2=dfa2.transition_function.get(keys2)
            if ((keys1[1])== (keys2[1])):
                word1=""
                word2=""
                word1+=str(keys1[0])
                word1+=str(keys2[0])
                word2+=str(value1)
                word2+=str(value2)
                if(keys1[0]==dfa1.start_state and keys2[0]==dfa2.start_state):
                    newstart=word1
                new_states.append(word1)
       
                    
                       
                newtf[(word1,keys1[1])]=word2
    if(getunion==1):   
                    temp=[]
                    for s in dfa1.states:
                        for i in dfa2.states:
                            word=""
                            word+=str(s)
                            word+=str(i)
                            temp.append(word)
                    for st in temp:
                        if(int(temp[0]) in dfa1.accept_states):
                            new_ac.append(st)
                        if(int(temp[1]) in dfa1.accept_states):
                            new_ac.append(st)
                           
                            
                     
                            
                    
   
                           
    res = [] 
    [res.append(x) for x in new_states if x not in res]  
    res2 = [] 
    [res2.append(x) for x in new_ac if x not in res2]   
    
              
   
    newdfa=DFA.dfa(res,dfa1.alphabet,newtf,newstart,res2)
    return(newdfa)




def intr(dfa1,dfa2,intersect=0,getunion=1):
    if (dfa1.alphabet !=  dfa1.alphabet):
        print("error must contain synonymous alphabets")
        return
    
    new_states=[]
    word1=""
    word2=""
    new_ac=[]
    newtf=dict()  
    newstart=""
    for keys1 in dfa1.transition_function:
        value1=dfa1.transition_function.get(keys1)
        for keys2 in dfa2.transition_function:
            value2=dfa2.transition_function.get(keys2)
            if ((keys1[1])== (keys2[1])):
                word1=""
                word2=""
                word1+=str(keys1[0])
                word1+=str(keys2[0])
                word2+=str(value1)
                word2+=str(value2)
                if(keys1[0]==dfa1.start_state and keys2[0]==dfa2.start_state):
                    newstart=word1
                new_states.append(word1)
       
                    
                       
                newtf[(word1,keys1[1])]=word2
    if(getunion==1):   
                    print("else4444444444")
                    for s in dfa1.accept_states:
                        for i in dfa2.accept_states: 
                            word=""
                            word+=str(s)
                            word+=str(i)
                            print("new",word)
                            new_ac.append(word)
                    print(new_ac)
    res = [] 
    [res.append(x) for x in new_states if x not in res]  
    res2 = [] 
    [res2.append(x) for x in new_ac if x not in res2]   
    
              
   
    newdfa=DFA.dfa(res,dfa1.alphabet,newtf,newstart,res2)
    return(newdfa)


states=[0,1,2,3]
accepting_states=[2]
alphabet=[0,1]
start=0
tf = dict()

tf[(0, '0')] = 1;
tf[(0, '1')] = 2;
tf[(1, '0')] = 1;
tf[(1, '1')] = 1;
tf[(2, '0')] = 3;
tf[(2, '1')] = 2;
tf[(3, '0')] = 3;
tf[(3, '1')] = 2;

dozen_4=DFA.dfa(states,alphabet,tf,start,accepting_states)
dozen_4.dfa_Traverse("")
dozen_4.dfa_Traverse("001")
dozen_4.dfa_Traverse("11")
dozen_4.dfa_Traverse("101")
dozen_4.dfa_Traverse("1001")
dozen_4.dfa_Traverse("0")
dozen_4.dfa_Traverse("100000")
dozen_4.dfa_Traverse("0000000")
dozen_4.dfa_Traverse("1010101")
dozen_4.dfa_Traverse("1111")
dozen_4.dfa_Traverse("111001")
dozen_4.dfa_Traverse("010")




states=[0,1,2,3,4,5]
accepting_states=[1,2,3,4]
alphabet=[0,1]
start=0
tf = dict()
tf[(0, '0')] = 1;
tf[(0, '1')] = 3;
tf[(1, '0')] = 5;
tf[(1, '1')] = 2;
tf[(2, '0')] = 1;
tf[(2, '1')] = 5;
tf[(3, '0')] = 4;
tf[(3, '1')] = 5;
tf[(4, '0')] = 5;
tf[(4, '1')] = 3;
tf[(5, '0')] = 5;
tf[(5, '1')] = 5;



dozen_5=DFA.dfa(states,alphabet,tf,start,accepting_states)
dozen_5.dfa_Traverse("")
dozen_5.dfa_Traverse("0101")
dozen_5.dfa_Traverse("11")
dozen_5.dfa_Traverse("101")
dozen_5.dfa_Traverse("10101")
dozen_5.dfa_Traverse("01")
dozen_5.dfa_Traverse("100000")
dozen_5.dfa_Traverse("0000000")
dozen_5.dfa_Traverse("1010101")
dozen_5.dfa_Traverse("1111")
dozen_5.dfa_Traverse("111001")
dozen_5.dfa_Traverse("010")
def equality(a,b):
        f=subset(a,b)
        h=subset(b,a)
        g=f and h
        print(g)
        return(g)
def subset(a,b):
   
    v=getinv(b)
   
    d3=intr(a,v)
    for i in d3.accept_states:
        print ("a",i)
 
    if (d3.step(d3.start_state,[],[])):
        print("this failed")
        return False
    else:
        print("this is a subset")
        return True
    
equality(dozen_4,dozen_4)
