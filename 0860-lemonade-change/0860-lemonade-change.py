class Solution:
    def lemonadeChange(self, bills: list[int]) -> bool:

        if bills[0] != 5:
            return False

        fv,tn,tw = 0,0,0

        for i in range(len(bills)):
            if bills[i] == 5:
                fv += 1
            elif bills[i] == 10:
                tn += 1
                if fv >= 1:
                    fv -= 1
                else:
                    return False
            else:
                tw += 1
                if fv >= 1 and tn >= 1:
                    tn -= 1
                    fv -= 1
                elif fv >= 3:
                    fv -= 3
                else:
                    return False
        return True





        