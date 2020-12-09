import DFA

states=[0]
accepting_states=[0]
alphabet=[0,1]
start=0
tf = dict()
tf[(0, '0')] = 1;
tf[(0, '1')] = 1;
tf[(1, '0')] = 1;
tf[(1, '1')] = 1;

empty_string=DFA.dfa(states,alphabet,tf,start,accepting_states)

empty_string.dfa_Traverse("")
