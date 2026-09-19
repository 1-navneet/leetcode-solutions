class Solution:
    def checkOverlap(self, radius: int, xCenter: int, yCenter: int, x1: int, y1: int, x2: int, y2: int) -> bool:
        a = max(x1,min(x2,xCenter))
        b = max(y1,min(y2,yCenter))
        c = xCenter - a
        d = yCenter - b
        return c*c + d*d <= radius*radius