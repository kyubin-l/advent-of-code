from utils.base_solution import BaseSolution
import re
from tqdm import tqdm

Q_NUM = 15
YEAR = 2022

class Solution(BaseSolution):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def load(self):
        self.sensors = []
        self.beacons = []
        with open(self.filename) as f:
            for line in f.readlines():
                line = line.rstrip()
                vals = re.sub('[^0-9 -]', "", line)
                vals = [int(val.strip()) for val in vals.split()]
                self.sensors.append((vals[0], vals[1]))
                self.beacons.append((vals[2], vals[3]))
        
        self.manhattan = []
        for sensor, beacon in zip(self.sensors, self.beacons):
            self.manhattan.append(self._manhattan_distance(sensor, beacon))
            
    
    def _manhattan_distance(self, coord1, coord2): 
        return abs(coord1[0] - coord2[0]) + abs(coord1[1] - coord2[1])
            
    def solve_part_one(self):
        unavailable_vals = set()
        row = 2_000_000
        
        for sensor, dist, beacon in zip(self.sensors, self.manhattan, self.beacons):
            pos_x_dist = dist - abs(sensor[1] - row)
            if pos_x_dist < 0:
                continue
            
            unavailable_vals.update(range(sensor[0]-pos_x_dist, sensor[0]+pos_x_dist+1))
            
            if sensor[1] == row:
                unavailable_vals.discard(sensor[0])
            if beacon[1] == row:
                unavailable_vals.discard(beacon[0])

        return len(unavailable_vals)
    
    def solve_part_two(self):

        def find_candidates_in_row(row):
            intervals = set()
        
            for sensor, dist in zip(self.sensors, self.manhattan):
                pos_x_dist = dist - abs(sensor[1] - row)
                if pos_x_dist < 0:
                    continue
                
                min_x = max(0, sensor[0]-pos_x_dist)
                max_x_val = min(sensor[0]+pos_x_dist+1, max_x)
                intervals.add((min_x, max_x_val))
                       
            interval_lower_vals = [interval[0] for interval in intervals]

            potential_candidates = set()
            for interval in intervals:
                if interval[1] + 1 in interval_lower_vals:
                    potential_candidates.add(interval[1])
            
            for potential_candidate in potential_candidates:
                valid = False
                for interval in intervals:
                    if interval[0] <= potential_candidate < interval[1]:
                        valid = False
                        break
                    valid = True
                if valid:
                    return potential_candidate, row
                    
        max_x = 4_000_001
            
        for i in tqdm(range(4_000_001)):
            res = find_candidates_in_row(i)
            if res:
                break
            
        return res[0] * 4_000_000 + res[1] 

if __name__ == '__main__':
    sol = Solution(Q_NUM, YEAR)
    sol.load()
    print(sol.solve_part_one())
    print(sol.solve_part_two())