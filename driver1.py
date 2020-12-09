import NFA
import TRC_TREE
"empty or ends in 1 or 10"
states=[0,1,2,3,4]
accepting_states=[2,3]
alphabet=['0','1',]
start=0
tf = dict()
tf[(0, '0')] = [0];
tf[(0, '1')] = [1,2,7];
tf[(0, 'blank')] = [3];
tf[(1, '0')] = [2];
tf[(1, '1')] = [1];
tf[(2, '0')] = [4];
tf[(2, '1')] = [2];
tf[(3, '0')] = [4];
tf[(3, 'blank')] = [0];
tf[(3, '1')] = [1,2];
tf[(4, '0')] = [0];
tf[(4, '1')] = [1,2];




dozen_8=NFA.nfa(states,alphabet,tf,start,accepting_states)
tree=TRC_TREE.trc_tree(dozen_8)

#tree.get_tree("")
#tree.get_tree("010")
#tree.get_tree("01001")
tree.get_tree("0100",1)
#tree.get_tree("00",0)
#tree.fork_tree("11")
#tree.trie.query("0")