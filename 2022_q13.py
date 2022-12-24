from utils.base_solution import BaseSolution
from itertools import zip_longest
import numpy as np
import copy

Q_NUM = 13
YEAR = 2022

def compare(left, right):
    if isinstance(left, int) and isinstance(right, int):
        if left == right:
            return 'Dohun'
        else: 
            return left < right
    elif isinstance(left, list) and isinstance(right, list):
        if not left and not right:
            return 'Kyubin'
                
        for l, r in zip_longest(left, right):
            if l is None:
                return True
            if r is None: 
                return False
                    
            if not isinstance(compare(l, r), str):
                return compare(l, r) 
    else:
        return compare([left], right) if isinstance(left, int) else compare(left, [right])
    

def bubbleSort(arr):
    n = len(arr)
    swapped = False
    for i in range(n-1):
        for j in range(0, n-i-1):
            if not compare(arr[j], arr[j + 1]):
                swapped = True
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
        if not swapped:
            return

class Solution(BaseSolution):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def load(self):
        self.tasks = []
        cur_task = []
        with open(self.filename) as f:
            for line in f.readlines():
                line = line.rstrip()
                if not line:
                    if not cur_task:
                        continue
                    self.tasks.append(cur_task)
                    cur_task = []
                    continue
                cur_task.append(eval(line))
            self.tasks.append(cur_task)
                        
    def solve_part_one(self):
        val = 0
        for i, task in enumerate(self.tasks, 1):
            if not compare(task[0], task[1]):
                continue
            val += i
        
        # return np.sum(np.array(range(1,len(self.tasks)+1))*np.array([compare(s[0], s[1]) for s in self.tasks]))
        return val

    def solve_part_two(self):
        result = [[[2]], [[6]]]
        tasks = copy.deepcopy(self.tasks)
        for task in tasks:
            result.append(task[0])
            result.append(task[1])
            
        int_list = []
        for task in result:
            while isinstance(task, list):  
                if not task:
                    task = 0
                    break                  
                task = task[0]
            int_list.append(task)
        
        print(int_list)
        int_list.sort()
        print(int_list)
        print(len(int_list))
        
        idx1 = int_list.index(2) + 1
        idx2 = int_list.index(6) + 1
        print(idx1)
        print(idx2)
        
        return idx1 * idx2
            
if __name__ == '__main__':
    sol = Solution(Q_NUM, YEAR)
    sol.load()
    print(sol.solve_part_one())
    print(sol.solve_part_two())