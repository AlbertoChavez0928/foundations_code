import DFA
def make_char_DFA(c,my_alphabet):
    states=[0,1,]
    start=0
    accepting_states=[1]
    tf=dict()
    state=0
    for ch in my_alphabet:
      
        if (ch==c):
            state=1
        tf[(0, ch)] = state;
        tf[(1, ch)] = state;
        
    
    tf[(1, c)] = 2;
    new_dfa=DFA.dfa(states,alphabet,tf,start,accepting_states)
    print(tf)
    new_dfa.dfa_Traverse("c")
    new_dfa.dfa_Traverse("ac")
    new_dfa.dfa_Traverse("ab")
    new_dfa.dfa_Traverse("cb")
    

    
    
    
    
alphabet=['a','b','c']
make_char_DFA('c',alphabet)
