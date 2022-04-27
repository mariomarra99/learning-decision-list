import pandas as pd
import numpy as np

def all_same_output(examples,target):
    v = examples[target].iloc[0]
    for i in examples[target][::]:
        if v != i:
            return (False,None)
        v = i
    return (True,v)    
    
def find_subset(examples, attributes, target):
    for a in attributes:
        keys = set([i for i in examples[a]])
        for k in keys:
            e = examples[examples[a]==k]
            r = all_same_output(e,target)
            if r[0]:
                return ('|' + a + ' -> ' + k, r[1], e)
    return (None,None,None)

def learn_decision_list(examples,attributes,target,l):
    if len(examples) == 0:
        return [('Trivial', 'No')]
    t, o, example_t = find_subset(examples,attributes,target)
    if not t:
        raise Exception('Failure')
    l.append((t,o))
    learn_decision_list(examples.drop(example_t.index),attributes,target,l)
    return l

def print_like_tree(toStr,l):
    acap = 1
    for i in l:
        if i[1] == 'Yes':
            toStr += ' => ' + i[0] + ' : ' + i[1]
            acap -= 1
        else:
            toStr += '\n' + '\t'*acap + i[0] + ' : ' + i[1]
        acap+=1
    print(toStr)
            
def main():
    rw = pd.read_csv('restaurant_waiting.csv')
    (features,target) = (rw.columns[0:10],rw.columns[10])
    decision_list = learn_decision_list(rw,features,target,[])
    print('Stampa lineare : \n' + str(decision_list))
    print_like_tree('Stampa like-tree : \n' , decision_list)
    
main()
