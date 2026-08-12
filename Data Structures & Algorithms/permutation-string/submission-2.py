class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False
        hashMap = {}
        for c in s1:
            if c in hashMap:
                hashMap[c] += 1
            else:
                hashMap[c]=1
        l = 0
        r = len(s1) 
        tempMap = {}
        # maintain sliding window of length l
        # advance r to l - 1 th position
        for i in range(len(s1)):
            if(s2[i] in tempMap):
                tempMap[s2[i]] += 1
            else:
                tempMap[s2[i]] = 1
        #now we move the window
        while(r!=len(s2)):
            if(tempMap == hashMap):
                return True
            
            #right updates
            if(s2[r] in tempMap):
                tempMap[s2[r]] += 1
            else:
                tempMap[s2[r]] = 1
            r += 1

            #left updates
            if(tempMap[s2[l]] == 1):
                del tempMap[s2[l]]
            else :
                tempMap[s2[l]] -= 1
            l += 1

        return tempMap == hashMap


        
                
            


            
        
            
        