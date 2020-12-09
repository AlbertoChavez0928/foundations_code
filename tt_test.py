import NFA
import TRC_TREE
"has 00 or 11"
states=[1,2,3]
accepting_states=[3]
alphabet=['0','1']
start=1
tf = dict()

tf[(1, '0')] = [1,2];
tf[(2, '0')] = [3];
tf[(3, '0')] = [2,3];

tf[(1, '1')] = [2];
tf[(2, '1')] = [1,3];
tf[(3, '1')] = [3];

TEST1=NFA.nfa(states,alphabet,tf,start,accepting_states)
tree=TRC_TREE.trc_tree(TEST1)

tree.get_tree("00",1)
tree.get_tree("11",1)
tree.get_tree("01",1)
tree.get_tree("01",1)
tree.get_tree("101",1)
tree.get_tree("010",1)






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




TEST2=NFA.nfa(states,alphabet,tf,start,accepting_states)
tree=TRC_TREE.trc_tree(TEST2)

tree.get_tree("",1)
tree.get_tree("010",1)
tree.get_tree("01001",1)
tree.get_tree("0100",1)
tree.get_tree("00",1)
tree.fork_tree("11")
tree.trie.query("0")



















"ends in 0 or "
states=[0,1,2,3,4]
accepting_states=[2]
alphabet=['0','1',]
start=0
tf = dict()
tf[(0, '0')] = [1];
tf[(0, '1')] = [0];
tf[(1, '0')] = [2];
tf[(1, '1')] = [1];
tf[(2, '0')] = [4];
tf[(2, '1')] = [2];
tf[(3, '0')] = [4];
tf[(3, '1')] = [1,2];
tf[(4, '0')] = [0];
tf[(4, '1')] = [1,2];

TEST3=NFA.nfa(states,alphabet,tf,start,accepting_states)
tree=TRC_TREE.trc_tree(TEST3)
tree.get_tree("100",1)
tree.get_tree("00",1)
tree.get_tree("11",1)
tree.get_tree("01",1)
tree.get_tree("01",1)
tree.get_tree("101",1)
tree.get_tree("010",1)
#tree.get_tree("")
#tree.get_tree("010")
#tree.get_tree("01001")
#tree.get_tree("00",0)
#tree.fork_tree("11")
tree.trie.query("0")





states=[0,1,2,3,]
accepting_states=[3]
alphabet=['a','b',]
start=0
tf = dict()

tf[(0, 'blank')] = [1];
tf[(1, 'a')] = [1,2];
tf[(1, 'b')] = [2];
tf[(2, 'a')] = [0,2];
tf[(2, 'b')] = [3];
tf[(3, 'b')] = [1];

TEST4=NFA.nfa(states,alphabet,tf,start,accepting_states)
tree=TRC_TREE.trc_tree(TEST4)
tree.get_tree("a",1)
tree.get_tree("bb",1)
tree.get_tree("aa",1)
tree.get_tree("aba",1)
tree.get_tree("bb",1)
tree.get_tree("ababa",1)
tree.get_tree("aab",1)
#tree.get_tree("")
#tree.get_tree("010")
#tree.get_tree("01001")
#tree.get_tree("00",0)
#tree.fork_tree("11")
tree.trie.query("0")
