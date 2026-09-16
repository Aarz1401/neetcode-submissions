class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        dict_ = {}

        for s in strs:
            s_normalized = "".join(sorted(s.lower()))
            if s_normalized in dict_:
                dict_[s_normalized] += [s]
            else:
                dict_[s_normalized] = [s]
        return_arr = []
        for value in dict_.values():
            return_arr.append(value)
        return return_arr


            
