class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        l1=len(s1)
        l2=len(s2)
        str1_arr=[0]*26
        str2_arr=[0]*26
        if l1>l2:
            return False
        for i in range(l1):
            str1_arr[ord(s1[i])-97]+=1
            str2_arr[ord(s2[i])-97]+=1

        if str1_arr==str2_arr:
            return True
        for i in range(l1,l2):
            str2_arr[ord(s2[i])-97]+=1
            str2_arr[ord(s2[i-l1])-97]-=1
            if str1_arr==str2_arr:
                return True 
        return False
