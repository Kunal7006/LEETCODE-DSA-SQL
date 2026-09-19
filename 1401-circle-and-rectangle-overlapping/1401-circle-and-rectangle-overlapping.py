class Solution:
    def checkOverlap(
        self,
        radius: int,
        xCenter: int,
        yCenter: int,
        x1: int,
        y1: int,
        x2: int,
        y2: int,
    ) -> bool:

        if x1 > xCenter:
            xi = x1
        elif x2 < xCenter:
            xi = x2
        else:
            xi = xCenter

        if y1 > yCenter:
            yi = y1
        elif y2 < yCenter:
            yi = y2
        else:
            yi = yCenter

        d = ((xi - xCenter) ** 2 + (yi - yCenter) ** 2) ** 0.5

        if radius >= d:
            return True
        else:
            return False
