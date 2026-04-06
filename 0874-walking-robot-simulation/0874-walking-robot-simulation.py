class Solution:
    def robotSim(self, commands: List[int], obstacles: List[List[int]]) -> int:
        x, y = 0, 0
        
        # Directions: North, East, South, West
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        d = 0  # start facing North
        
        res = 0
        
        # Convert obstacles list to set for fast lookup
        obstacle_set = {tuple(o) for o in obstacles}
        
        for c in commands:
            if c == -1:  # turn right
                d = (d + 1) % 4
            elif c == -2:  # turn left
                d = (d - 1) % 4
            else:
                dx, dy = directions[d]
                
                for _ in range(c):
                    if (x + dx, y + dy) in obstacle_set:
                        break
                    
                    x += dx
                    y += dy
                    
                    res = max(res, x*x + y*y)
        
        return res 