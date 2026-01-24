class Solution(object):
    def squareIsWhite(self, coordinates):

        x,y = coordinates

        if x in 'aceg' and y in "1357":
            return False
        if x in 'bdfh' and y in "2468":
            return False
            
        return True    


        