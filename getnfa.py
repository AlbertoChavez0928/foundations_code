def getnfa(mydfa):
    
    new_tf = dict()
    ac=mydfa.accept_states
    for i in mydfa.transition_function :
        new_tf[i] = [mydfa.transition_function.get(i)]

    nfa=NFA.nfa(mydfa.states,mydfa.alphabet,new_tf,mydfa.start_state ,ac)  
    return nfa
