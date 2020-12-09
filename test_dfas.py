import DFA
##this dfa returns true if you start with 1###
states=[0,1,2,3,4]
accepting_states=[1,2,3]
alphabet=[1,2,3]
start=0
tf = dict()
tf[(0, '1')] = 1;
tf[(0, '2')] = 2;
tf[(0, '3')] = 3;
tf[(1, '1')] = 1;
tf[(1, '2')] = 2;
tf[(1, '3')] = 3;
tf[(2, '1')] = 4;
tf[(2, '2')] = 2;
tf[(2, '3')] = 3;
tf[(3, '1')] = 4;
tf[(3, '2')] = 4;
tf[(3, '3')] = 3;
tf[(4, '1')] = 4;
tf[(4, '2')] = 4;
tf[(4, '3')] = 4;



print("test8 increasine order")

dozen_8=DFA.dfa(states,alphabet,tf,start,accepting_states)

dozen_8.dfa_Traverse("123")
dozen_8.dfa_Traverse("11111")
dozen_8.dfa_Traverse("2222233333")
dozen_8.dfa_Traverse("112233")
dozen_8.dfa_Traverse("3333")
dozen_8.dfa_Traverse("23")

dozen_8.dfa_Traverse("122222333331")
dozen_8.dfa_Traverse("")
dozen_8.dfa_Traverse("32222111")
dozen_8.dfa_Traverse("21212")
dozen_8.dfa_Traverse("212132")
dozen_8.dfa_Traverse("321")



states=[0,1,2]
accepting_states=[2]
alphabet=[1,2,3]
start=0
tf = dict()
tf[(0, '1')] = 1;
tf[(0, '2')] = 2;
tf[(0, '3')] = 1;
tf[(1, '1')] = 1;
tf[(1, '2')] = 1;
tf[(1, '3')] = 1;
tf[(2, '1')] = 1;
tf[(2, '2')] = 1;
tf[(2, '3')] = 1;

dozen_9=DFA.dfa(states,alphabet,tf,start,accepting_states)



def getinv(mydfa):
    nac=[]
    ac=mydfa.accept_states
    for i in mydfa.states :
        if i not in ac :
            nac.append(i)
    mydfa.accept_states=nac
    return mydfa


import nthstring
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
                        res = [] 
                        [res.append(x) for x in new_states if x not in res] 
                    for st in res:
                        
                        if(int(st[0]) in dfa1.accept_states):
                            new_ac.append(st)
                        if(int(st[1]) in dfa2.accept_states):
                            new_ac.append(st)
                            print(new_ac)
                           
                            
                     
                            
                    
   
                           
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
                            new_ac.append(word)
                           
    res = [] 
    [res.append(x) for x in new_states if x not in res]  
    res2 = [] 
    [res2.append(x) for x in new_ac if x not in res2]   
    
              
   
    newdfa=DFA.dfa(res,dfa1.alphabet,newtf,newstart,res2)
    return(newdfa)






def subset(a,b):
    print("n")
    d3=intr(a,getinv(b))
    print(d3.accept_states)
    for i in d3.transition_function:
        print(i,d3.transition_function.get(i))
    j=(d3.start_state,"")
    d3.forward(j,[])
  
    

#subset(dozen_9,dozen_8)































import DFA
##this dfa returns true if you start with 1###
states=[0,1,2,3,4,5]
accepting_states=[2,4]
alphabet=['0','1']
start=0
tf = dict()
tf[(0, '0')] = 1;
tf[(0, '1')] = 3;
tf[(1, '0')] = 2;
tf[(1, '1')] = 5;
tf[(2, '0')] = 5;
tf[(2, '1')] = 3;
tf[(3, '0')] = 5;
tf[(3, '1')] = 4;
tf[(4, '0')] = 1;
tf[(4, '1')] = 5;
tf[(5, '0')] = 5;
tf[(5, '1')] = 5;



dozen_1=DFA.dfa(states,alphabet,tf,start,accepting_states)
print("test1 only two of the same adjcent")
dozen_1.dfa_Traverse("00")
dozen_1.dfa_Traverse("11")
dozen_1.dfa_Traverse("001100")
dozen_1.dfa_Traverse("110011")
dozen_1.dfa_Traverse("1100")
dozen_1.dfa_Traverse("11001100")
dozen_1.dfa_Traverse("101")
dozen_1.dfa_Traverse("010")
dozen_1.dfa_Traverse("")
dozen_1.dfa_Traverse("1010101")
dozen_1.dfa_Traverse("1111")
dozen_1.dfa_Traverse("111001")




import DFA
##this dfa returns true if you start with 1###
states=[0,1,2]
accepting_states=[2]
alphabet=[0,1]
start=0
tf = dict()
tf[(0, '0')] = 1;
tf[(0, '1')] = 2;
tf[(1, '0')] = 1;
tf[(1, '1')] = 1;
tf[(2, '0')] = 2;
tf[(2, '1')] = 2;



dozen_2=DFA.dfa(states,alphabet,tf,start,accepting_states)
print("test2 start with one")
dozen_2.dfa_Traverse("001")
dozen_2.dfa_Traverse("11")
dozen_2.dfa_Traverse("101")
dozen_2.dfa_Traverse("1001")
dozen_2.dfa_Traverse("0")
dozen_2.dfa_Traverse("1000001")
dozen_2.dfa_Traverse("0000000")
dozen_2.dfa_Traverse("1010101")
dozen_2.dfa_Traverse("1111")
dozen_2.dfa_Traverse("0111001")
dozen_2.dfa_Traverse("")
dozen_2.dfa_Traverse("0001")




states=[0,1]
accepting_states=[2]
alphabet=[0,1,2]
start=0
tf = dict()
tf[(0, '0')] = 1;
tf[(0, '1')] = 2;
tf[(1, '0')] = 1;
tf[(1, '1')] = 2;
tf[(2, '0')] = 0;
tf[(2, '1')] = 2;





dozen_3=DFA.dfa(states,alphabet,tf,start,accepting_states)
print("test3 ends with 1")
dozen_3.dfa_Traverse("001")
dozen_3.dfa_Traverse("11")
dozen_3.dfa_Traverse("01")
dozen_3.dfa_Traverse("1001")
dozen_3.dfa_Traverse("010")
dozen_3.dfa_Traverse("100001")
dozen_3.dfa_Traverse("00000001")
dozen_3.dfa_Traverse("01010")
dozen_3.dfa_Traverse("11110")
dozen_3.dfa_Traverse("11100")
dozen_3.dfa_Traverse("110")
dozen_3.dfa_Traverse("")




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

print("test4 starts and ends with one")

print("")
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


print("test5 alternation characters")
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























import DFA
import numpy as np
##this dfa returns true if you start with 1###
states=[0,1,2,3]
accepting_states=[3]
alphabet=['0','1']
start=0
tf = dict()
tf[(0, '0')] = 1;
tf[(0, '1')] = 2;
tf[(1, '0')] = 3;
tf[(1, '1')] = 2;
tf[(2, '0')] = 1;
tf[(2, '1')] = 3;
tf[(3, '0')] = 3;
tf[(3, '1')] = 3;

print("test6 atleast 2 of the same adjactent")
dozen_6=DFA.dfa(states,alphabet,tf,start,accepting_states)
dozen_6.dfa_Traverse("")
dozen_6.get_path()
dozen_6.dfa_Traverse("001")
dozen_6.get_path()
dozen_6.dfa_Traverse("11")
dozen_6.get_path()
dozen_6.dfa_Traverse("101")
dozen_6.get_path()
dozen_6.dfa_Traverse("1001")
dozen_6.get_path()
dozen_6.dfa_Traverse("0")
dozen_6.get_path()
dozen_6.dfa_Traverse("100000")
dozen_6.get_path()
dozen_6.dfa_Traverse("0000000")
dozen_6.get_path()
dozen_6.dfa_Traverse("1010101")
dozen_6.get_path()
dozen_6.dfa_Traverse("1111")
dozen_6.get_path()
dozen_6.dfa_Traverse("10101")
dozen_6.get_path()
dozen_6.dfa_Traverse("1")

##this dfa returns true if you start with 1###
states=[0,1,2,3,4]
accepting_states=[1,2,3]
alphabet=['1','2','3']
start=0
tf = dict()
tf[(0, '1')] = 1;
tf[(0, '2')] = 2;
tf[(0, '3')] = 3;
tf[(1, '1')] = 1;
tf[(1, '2')] = 4;
tf[(1, '3')] = 4;
tf[(2, '1')] = 1;
tf[(2, '2')] = 2;
tf[(2, '3')] = 4;
tf[(3, '1')] = 1;
tf[(3, '2')] = 2;
tf[(3, '3')] = 3;
tf[(4, '1')] = 4;
tf[(4, '2')] = 4;
tf[(4, '3')] = 4;


def getstr1(mydfa):
    Sample_word=nthstring.Word(mydfa.alphabet)
    x=200
    j=1
    a=0
    while j:
        if(mydfa.dfa_Traverse(Sample_word.get_nth_string(a))):
            j=0
            print(str(Sample_word.get_nth_string(a)))
        mydfa.get_path()
        a=a+1



dozen_7=DFA.dfa(states,alphabet,tf,start,accepting_states)




dozen_7.dfa_Traverse("2222233333")
dozen_7.dfa_Traverse("112233")
dozen_7.dfa_Traverse("122222333331")
dozen_7.dfa_Traverse("")
dozen_7.dfa_Traverse("21212")
dozen_7.dfa_Traverse("212132")
dozen_7.dfa_Traverse("321")
dozen_7.dfa_Traverse("32222111")
dozen_7.dfa_Traverse("3333")
dozen_7.dfa_Traverse("3")
dozen_7.dfa_Traverse("322")
dozen_7.dfa_Traverse("11111")
print("dozen_7=getinv(dozen_7)")
dozen_7=getinv(dozen_7)
dozen_7.dfa_Traverse("2222233333")
dozen_7.dfa_Traverse("112233")
dozen_7.dfa_Traverse("122222333331")
dozen_7.dfa_Traverse("")
dozen_7.dfa_Traverse("21212")
dozen_7.dfa_Traverse("212132")
dozen_7.dfa_Traverse("321")
dozen_7.dfa_Traverse("32222111")
dozen_7.dfa_Traverse("3333")
dozen_7.dfa_Traverse("3")
dozen_7.dfa_Traverse("322")
dozen_7.dfa_Traverse("11111")



getstr1(dozen_6)


print("starts or ends in 1")
d10=union(dozen_2,dozen_3)
print(d10.accept_states)
d10.dfa_Traverse("001")
d10.dfa_Traverse("11")
d10.dfa_Traverse("101")
d10.dfa_Traverse("1001")
d10.dfa_Traverse("0")
d10.dfa_Traverse("1000001")
d10.dfa_Traverse("0000000")
d10.dfa_Traverse("1010101")
d10.dfa_Traverse("1111")
d10.dfa_Traverse("0111001")
d10.dfa_Traverse("")
d10.dfa_Traverse("0001")

print("starts and ends in 1")


d11=intr(dozen_2,dozen_3)
print(d11.accept_states)
d11.dfa_Traverse("001")
d11.dfa_Traverse("11")
d11.dfa_Traverse("101")
d11.dfa_Traverse("1001")
d11.dfa_Traverse("0")
d11.dfa_Traverse("1000001")
d11.dfa_Traverse("0000000")
d11.dfa_Traverse("1010101")
d11.dfa_Traverse("1111")
d11.dfa_Traverse("0111001")
d11.dfa_Traverse("")
d11.dfa_Traverse("0001")