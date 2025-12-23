class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        left=0
        dict_count={}
        result=0
        for right in range(len(s)):
            dict_count[s[right]]=dict_count.get(s[right],0)+1
            # dict_count=sorted(dict_count.items(), key=lambda item: item[1])
            max_count=max(dict_count.values())
            window_size=right-left+1
            
            while (window_size-max_count)>k:
                dict_count[s[left]]-=1
                left+=1
                window_size=right-left+1
                max_count=max(dict_count.values())
            result=max(window_size,result)
        return result

