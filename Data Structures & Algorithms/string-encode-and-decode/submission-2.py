class Solution:

    def encode(self, strs: List[str]) -> str:
        returnstr = ""
        for string in strs:
            returnstr+="Aadil"
            returnstr+="-"
            returnstr+=(string)
        return returnstr


    def decode(self, s: str) -> List[str]:
        if(s == ""):
            return []
        returnstr = s[6:]
        return returnstr.split("Aadil-")
