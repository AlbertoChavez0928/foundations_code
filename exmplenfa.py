"00b or 11b"
states=[0,1,2,3,4,5,6]
accepting_states=[6]
alphabet=['0','1','b']
start=0
tf = dict()
tf[(0, '0')] = [1,2];
tf[(0, '1')] = [3,4];
tf[(1, '0')] = [5];
tf[(2, '1')] = [3];
tf[(3, '1')] = [5];
tf[(4, '0')] = [1];
tf[(5, 'b')] = [6];

t1=[0,2,3,5,6]
t2=[0,1,5,6]
t3=[0,3,5,6]
t4=[0,4,1,5,6]




 "00 or 11 followed by 2 letters"
states=[0,1,2,3,4,5,6,7]
accepting_states=[7]
alphabet=['0','1','b','a']
start=0
tf = dict()
tf[(0, '0')] = [1,2];
tf[(0, '1')] = [3,4];
tf[(1, '0')] = [5];
tf[(2, '1')] = [3];
tf[(3, '1')] = [5];
tf[(4, '0')] = [1];
tf[(5, 'b')] = [6];
tf[(5, 'a')] = [6];
tf[(6, 'b')] = [7];
tf[(6, 'a')] = [7];
tf[(5, '0')] = [1,2];
tf[(5, '1')] = [3,4];
tf[(6, '0')] = [1,2];
tf[(6, '1')] = [3,4];


t1=[0,2,3,5,6,7]
t2=[0,2,3,5,6,1,5,6,7]
t3=[0,3,5,6,7]
t4=[0,4,1,5,6,7]

"contains a number ""


states=[0,1,2]
accepting_states=[2]
alphabet=['1','2','3','a','b']
start=0
tf = dict()
tf[(0, 'a')] = [0,1];
tf[(0, 'b')] = [0,1];
tf[(0, 'blank')] = [1];

tf[(1, '1')] = [2];
tf[(1, '2')] = [2];
tf[(1, '3')] = [2];
tf[(1, 'blank')] = [0];



t1=[0,1,0,1,2,]
t2=[0,0,0,1,2]
t3=[0,1,0,0,1,2]
t4=[0,1,2]





"aei string"

states=[0,1,2,3]
accepting_states=[3]
alphabet=['a','e','i','o','u']
start=0
tf = dict()
tf[(0, 'a')] = [0,1];
tf[(0, 'e')] = [0];
tf[(0, 'i')] = [0];
tf[(0, 'o')] = [0];
tf[(0, 'u')] = [0];
tf[(1, 'e')] = [2];
tf[(2, 'i')] = [3];

t1=[0,0,0,1,2,3]
t2=[0,0,0,1,2]
t3=[0,0,0,1,2,3]
t4=[0,1,2,3]



"bat or cat"

states=[0,1,2,3,4]
accepting_states=[4]
alphabet=['b','c','a','t']
start=0
tf = dict()
tf[(0, 'b')] = [0,1];
tf[(0, 'blank')] = [2];
tf[(2, 'c')] = [0,1];
tf[(1, 'a')] = [3];

tf[(3, 't')] = [4];

t1=[0,0,0,1,3,4]
t2=[0,2,1,3,4]
t3=[0,0,0,2,1,3,4]
t4=[0,2,0,1,3,4]

