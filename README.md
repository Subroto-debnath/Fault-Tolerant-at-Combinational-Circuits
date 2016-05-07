# Fault-Tolerant-at-Combinational-Circuits
It shows the simplest solutions of a boolean function and provides which one is best for implementation.
#Requirements
Python 2.7
#Use
Input:
F(W,X,Y,Z)=5,10,12,14

Don't care F'(W,X,Y,Z)=4,11
Output:

Group= [[(1, 0), (2, 0)], [(1, 0), (1, 1)], [(2, 3), (3, 3)]]

Result= BC'D' + A'BC' + ACD'

Error posibility for the result= 0.268
 
 
 
Group= [[(1, 0), (1, 1)], [(2, 3), (3, 3)], [(2, 3), (2, 0)]]

Result= A'BC' + ACD' + ABD'

Common-term= (2, 3)

Error posibility for the result= 0.231

 
 
Group= [[(1, 0), (1, 1)], [(2, 3), (2, 0)], [(3, 2), (3, 3)]]

Result= A'BC' + ABD' + AB'C

Error posibility for the result= 0.268

#Acknowledgement
The Goal of this system is to develop a simulation-based method which is based on maximizing the probability of logical masking when a soft error occurs. This is done by extracting sub-circuits from an original multi-level circuit and then re-synthesizing each extracted sub-circuit to increase fault masking against a single fault.
