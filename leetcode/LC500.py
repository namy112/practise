class Solution(object):
    def findWords(self, words):
        """
        :type words: List[str]
        :rtype: List[str]
        """
        
    #10:01 54 mins
    
    # Go through each alphabet of a word
    # FirstRowIdentified
    # Check if that alpa in list 1. If yes, then check if FirstRowIdentified is null. If yes, then set FirstRowIdentified=List1
    # Or check if it's same as for Now check 2nd alph. 
    #If not than exit out and go to the next number
    # Or append the word to the finalList
    
    
        result=[]
        
        firstRow=['Q','W','E','R','T','Y','U','I','O','P']
        secondRow=['A','S','D','F','G','H','J','K','L']
        thirdRow=['Z','X','C','V','B','N','M']


        for word in words:
            temp=[]
            for c in word.upper():
                if c in firstRow:
                    temp.append('1')
                elif c in secondRow:
                    temp.append('2')
                else:
                    temp.append('3')

            if len(set(temp)) == 1:
                result.append(word)
    

        return result
    
        # check sensitivity of the laters
        # temp[] should be refreshed for everyword
    
    
        
            
        
    
    
    
    
        
        
        