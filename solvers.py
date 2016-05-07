from helpers import *
from sets import Set
one=[]
result1=[]
result2=[]
result3=[]
main_res=[[]]

class KMapSolver(object):
    NUMBER_OF_VARS = None
    ZONES = {}
    

    def __init__(self, map_data):
        self.map_data = map_data
        self.groups = []
        self.result_group_set = []
        self.gp=[]
        self.po=[]
        self.fo=[]
        self.terms = []
        self.trm = []
        self.result = ''
        self.total_error=0

    def create_group(self, i, j):
        size = 0
        result = []        

        if self.map_data[i][j] == 1:
            one.append((i,j))
            #print "one=", one

        # Try 1 element
        _result = []
        if self.map_data[i][j] > 0:
            size = 1
            _result.append([(i,j),])

        if size == 1:
            result = _result
            result1.append((i,j))
##            print "1 element=",result
##            print "result1=",result1
        else: return result

        # Try 2 elements
        _result = []
        down = go_down(self.map_data, i, j)
        if self.map_data[i][j] > 0 and  down[2] > 0:
            size = 2
            _result.append([(i,j), (down[0], down[1])])
            result2.append([(i,j), (down[0], down[1])])

        right = go_right(self.map_data, i, j)
        if self.map_data[i][j] > 0 and right[2] > 0:
            size = 2
            _result.append([(i,j), (right[0], right[1])])
            result3.append([(i,j), (right[0], right[1])])

        if size == 2:
            result = _result
##            print "2 element=",result
##            print "result2=",result2
##            print "result3=",result3
        else: return result

        # Try 4 elements
        if self.NUMBER_OF_VARS < 3: return result
        _result = []
        el = go_right(self.map_data, down[0], down[1])##use of down??
        _sqr_4_group = [(i,j), (down[0], down[1]), (right[0], right[1]), (el[0], el[1])]
        if all(self.map_data[xy[0]][xy[1]] > 0 for xy in _sqr_4_group):##Not Clear
            size = 4
            _result.append(_sqr_4_group)

        if size == 4: result = _result

        _cursor = (i, j)
        _horizontal_4_group = [_cursor]
        el = go_right(self.map_data, _cursor[0], _cursor[1]); _cursor = (el[0], el[1]); _horizontal_4_group.append(_cursor)
        el = go_right(self.map_data, _cursor[0], _cursor[1]); _cursor = (el[0], el[1]); _horizontal_4_group.append(_cursor)
        el = go_right(self.map_data, _cursor[0], _cursor[1]); _cursor = (el[0], el[1]); _horizontal_4_group.append(_cursor)

        if all(self.map_data[xy[0]][xy[1]] > 0 for xy in _horizontal_4_group):
            size = 4
            _result.append(_horizontal_4_group)

        if self.NUMBER_OF_VARS > 3: # no vertical 4 block in 3-var map
            _cursor = (i, j)
            _vertical_4_group = [_cursor]
            el = go_down(self.map_data, _cursor[0], _cursor[1]); _cursor = (el[0], el[1]); _vertical_4_group.append(_cursor)
            el = go_down(self.map_data, _cursor[0], _cursor[1]); _cursor = (el[0], el[1]); _vertical_4_group.append(_cursor)
            el = go_down(self.map_data, _cursor[0], _cursor[1]); _cursor = (el[0], el[1]); _vertical_4_group.append(_cursor)

            if all(self.map_data[xy[0]][xy[1]] > 0 for xy in _vertical_4_group):
                size = 4
                _result.append(_vertical_4_group)

        if size == 4:
            result = _result
           # print "4 element=",result
        else: return result

        # Try 8 elements
        if self.NUMBER_OF_VARS < 4: return result
        _result = []

        _cursor = (i, j)
        _horizontal_8_group = [_cursor]
        el = go_right(self.map_data, _cursor[0], _cursor[1]); _cursor = (el[0], el[1]); _horizontal_8_group.append(_cursor)
        el = go_right(self.map_data, _cursor[0], _cursor[1]); _cursor = (el[0], el[1]); _horizontal_8_group.append(_cursor)
        el = go_right(self.map_data, _cursor[0], _cursor[1]); _cursor = (el[0], el[1]); _horizontal_8_group.append(_cursor)
        el = go_down(self.map_data, _cursor[0], _cursor[1]); _cursor = (el[0], el[1]); _horizontal_8_group.append(_cursor)
        el = go_left(self.map_data, _cursor[0], _cursor[1]); _cursor = (el[0], el[1]); _horizontal_8_group.append(_cursor)
        el = go_left(self.map_data, _cursor[0], _cursor[1]); _cursor = (el[0], el[1]); _horizontal_8_group.append(_cursor)
        el = go_left(self.map_data, _cursor[0], _cursor[1]); _cursor = (el[0], el[1]); _horizontal_8_group.append(_cursor)

        if all(self.map_data[xy[0]][xy[1]] > 0 for xy in _horizontal_8_group):
            size = 8
            _result.append(_horizontal_8_group)


        _cursor = (i, j)
        _vertical_8_group = [_cursor]
        el = go_right(self.map_data, _cursor[0], _cursor[1]); _cursor = (el[0], el[1]); _vertical_8_group.append(_cursor)
        el = go_down(self.map_data, _cursor[0], _cursor[1]); _cursor = (el[0], el[1]); _vertical_8_group.append(_cursor)
        el = go_left(self.map_data, _cursor[0], _cursor[1]); _cursor = (el[0], el[1]); _vertical_8_group.append(_cursor)
        el = go_down(self.map_data, _cursor[0], _cursor[1]); _cursor = (el[0], el[1]); _vertical_8_group.append(_cursor)
        el = go_right(self.map_data, _cursor[0], _cursor[1]); _cursor = (el[0], el[1]); _vertical_8_group.append(_cursor)
        el = go_down(self.map_data, _cursor[0], _cursor[1]); _cursor = (el[0], el[1]); _vertical_8_group.append(_cursor)
        el = go_left(self.map_data, _cursor[0], _cursor[1]); _cursor = (el[0], el[1]); _vertical_8_group.append(_cursor)

        if all(self.map_data[xy[0]][xy[1]] > 0 for xy in _vertical_8_group):
            size = 8
            _result.append(_vertical_8_group)


        if size == 8: result = _result
        #print "8 element=",result
        return result

    def verify_group(self, grp):
        for i, x in enumerate(self.result_group_set):
            if is_subset(grp, x):
                self.result_group_set[i] = grp
                return
            if is_subset(x, grp):
                return
        self.result_group_set.append(grp)
##        print "grp=",self.result_group_set

    def group_to_term(self, grp):
        grp = set(grp)
        result = ""
        # Using lowercase a, b, c, d as complement of A, B, C, D
        if not grp.isdisjoint(self.ZONES['A']): result += 'A'
        if not grp.isdisjoint(self.ZONES['a']): result += 'a'
        if not grp.isdisjoint(self.ZONES['B']): result += 'B'
        if not grp.isdisjoint(self.ZONES['b']): result += 'b'
        if self.NUMBER_OF_VARS > 2:
            if not grp.isdisjoint(self.ZONES['C']): result += 'C'
            if not grp.isdisjoint(self.ZONES['c']): result += 'c'
        if self.NUMBER_OF_VARS > 3:
            if not grp.isdisjoint(self.ZONES['D']): result += 'D'
            if not grp.isdisjoint(self.ZONES['d']): result += 'd'

        for cmpl in ['Aa', 'Bb', 'Cc', 'Dd']:
            result = result.replace(cmpl, '')
        return result.replace('a', 'A\'').replace('b', 'B\'').replace('c', 'C\'').replace('d', 'D\'')

    def solution(self,group_set):
        print " "
        print "Group=", group_set
        terms=[]
        for x in group_set:
            terms.append(self.group_to_term(x))
        
        for x in 'ABCD':
            cmpl_x = x + '\''
            if x in terms and cmpl_x in terms:
                terms.remove(x)
                terms.remove(cmpl_x)
                if '1' not in terms:
                    terms.append('1')
        self.result =  reduce(lambda p, q: (p+' + '+q), terms, '0').replace('0 + ', '')
        print "Result=", self.result
        del self.terms[:]
        probability=[[.23,.34,.21,.45],[.56,.43,.38,.63],[.31,.71,.52,.37],[.48,.12,.27,.23]]
        re=group_set
        po=len(re)
        result=[]
        for i in range(0,po):
            j=len(re[i])
            for j in range(0,j):
                result.append(re[i][j])
        e_result=result
        l=len(result)
        for i in range(0,l):
            count=0
            for j in range(0,l):
                if result[i]==result[j]:
                    count=count+1
            if(count>1)and (result[i] in one):
                [p,q]=result[i]
                print"Common-term=", result[i]
                result[i]=(-1,-1)
                probability[p][q]=probability[p][q]/count
        total_error=0
        for i in range(len(one)):
            [p,q]=one[i]
            total_error=total_error+probability[p][q]
        le=len(group_set)
        number_of_gates=le+(le-1)
        total_error=total_error/number_of_gates
        print "Error posibility for the result=", total_error
        print " "
                
                               
        
    def final_group(self,data):
        t=Set(one)
        one_element=0
        two_element=0
        three_element=0
        four_element=0

        #try 1 element
        for i in range(len(data)):
            po=data[i]
            fo=[data[i]]
            s=Set(po)
            if s.issuperset(t):
                print "result=", fo
                self.solution(fo)
                one_element=1

        #try 2 elements
        if one_element==0:
            for i in range(len(data)):
                for j in range(i+1,len(data)):
                    po=data[i]+data[j]
                    fo=[data[i]]+[data[j]]
                    s=Set(po)
                    if s.issuperset(t):
                        self.solution(fo)
                        two_element=1

        #try 3 elements
        if two_element==0:
            for i in range(len(data)):
                for j in range(i+1,len(data)):
                    for k in range(j+1,len(data)):
                        po=data[i]+data[j]+data[k]
                        fo=[data[i]]+[data[j]]+[data[k]]
                        s=Set(po)
                        if s.issuperset(t):
                            self.solution(fo)
                            three_element=1

        #try 4 elements
        if three_element==0:
            for i in range(len(data)):
                for j in range(i+1,len(data)):
                    for k in range(j+1,len(data)):
                        for l in range(k+1,len(data)):
                            po=data[i]+data[j]+data[k]+data[l]
                            s=Set(po)
                            if s.issuperset(t):
                                self.solution(fo)
                                four_element=1
                            
                
                                      

    def solve(self):
        for i, row in enumerate(self.map_data):
            for j, elem in enumerate(row):
                for group in self.create_group(i, j):
                    self.verify_group(group)
        print "one=",one
        print self.result_group_set
        self.final_group(self.result_group_set)
        
     
        

    

class KMapSolver2(KMapSolver):
    NUMBER_OF_VARS = 2
    ZONES = {'A': {(1, 0), (1, 1)},
             'a': {(0, 0), (0, 1)},
             'B': {(0, 1), (1, 1)},
             'b': {(0, 0), (1, 0)},}


class KMapSolver3(KMapSolver):
    NUMBER_OF_VARS = 3
    ZONES = {'A': {(1, 0), (1, 1), (1, 2), (1, 3)},
             'a': {(0, 0), (0, 1), (0, 2), (0, 3)},
             'B': {(0, 2), (0, 3), (1, 2), (1, 3)},
             'b': {(0, 0), (0, 1), (1, 0), (1, 1)},
             'C': {(0, 1), (0, 2), (1, 1), (1, 2)},
             'c': {(0, 0), (1, 0), (0, 3), (1, 3)}}


class KMapSolver4(KMapSolver):
    NUMBER_OF_VARS = 4
    ZONES = {'A': {(2, 0), (2, 1), (2, 2), (2, 3), (3, 0), (3, 1), (3, 2), (3, 3)},
             'a': {(0, 0), (0, 1), (0, 2), (0, 3), (1, 0), (1, 1), (1, 2), (1, 3)},
             'B': {(1, 0), (1, 1), (1, 2), (1, 3), (2, 0), (2, 1), (2, 2), (2, 3)},
             'b': {(0, 0), (0, 1), (0, 2), (0, 3), (3, 0), (3, 1), (3, 2), (3, 3)},
             'C': {(0, 2), (1, 2), (2, 2), (3, 2), (0, 3), (1, 3), (2, 3), (3, 3)},
             'c': {(0, 0), (1, 0), (2, 0), (3, 0), (0, 1), (1, 1), (2, 1), (3, 1)},
             'D': {(0, 1), (1, 1), (2, 1), (3, 1), (0, 2), (1, 2), (2, 2), (3, 2)},
             'd': {(0, 0), (1, 0), (2, 0), (3, 0), (0, 3), (1, 3), (2, 3), (3, 3)}}
