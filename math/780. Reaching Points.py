# https://leetcode.com/problems/reaching-points/

class Solution:
    def reachingPoints(self, sx: int, sy: int, tx: int, ty: int) -> bool:
        
        def validate(x1, y1, x2, y2):
            print(x1, y1, x2, y2)
            if x2 < x1:
                return False
            
            elif x2 == x1:
                
                if y2 >= y1:
                    return (y2 - y1) % x1 == 0
                else:
                    return False
            
            else:
                return validate(y1, x1, y2 % x2, x2)
            
        
        # if tx < ty:
        return validate(sx, sy, tx, ty)
        
        # else:
            # return validate(sy, sx, ty, tx)
            
#             xt = 5 yt = 15
#             x = 5 y = 5
#             x = 5, y = 5 + 5 = 10
#             x = 5, y += 5 = 15
            
#             10cm
            
#             10cm
