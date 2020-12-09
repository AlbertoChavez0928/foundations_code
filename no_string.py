import DFA

states=[0]
accepting_states=[]
alphabet=[0,1]
start=0
tf = dict()
tf[(0, '0')] = 0
tf[(0, '1')] = 0


no_string=DFA.dfa(states,alphabet,tf,start,accepting_states)
no_string.dfa_Traverse("00")

no_string.dfa_Traverse("1")

no_string.dfa_Traverse("11")

no_string.dfa_Traverse("")
