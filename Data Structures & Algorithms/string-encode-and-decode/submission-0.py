class Solution:
    def encode(self, strs: List[str]) -> str:
        res = ""
        for s in strs:
            res += str(len(s)) + "#" + s
        return res

    def decode(self, s: str) -> List[str]:
        res = []
        i = 0
        
        while i < len(s):
            # j finds the delimiter '#'
            j = i
            while s[j] != '#':
                j += 1
            
            # Length of the string payload
            length = int(s[i:j])
            
            # Extract s[j + 1 : j + 1 + length]
            start = j + 1
            end = start + length
            res.append(s[start:end])
            
            # Jump index i directly to the next length prefix
            i = end
            
        return res