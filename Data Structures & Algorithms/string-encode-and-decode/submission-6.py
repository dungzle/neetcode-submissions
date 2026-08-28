class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded = []
        for s in strs:
            temp = str(len(s)) + "#" + s
            encoded.append(temp)
        return "".join(encoded)

    def decode(self, s: str) -> List[str]:
        decoded = []
        i = 0
        while i < len(s):
            j = i
            while s[j] != "#":
                j += 1
            count = int(s[i:j])
            i = j + 1
            j = i + count
            decoded.append(s[i:j])
            i = j
            
        return decoded