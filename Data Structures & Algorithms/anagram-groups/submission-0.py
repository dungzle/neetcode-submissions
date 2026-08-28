class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        string_dict = defaultdict(list)
        for s in strs:
            string_dict["".join(sorted(s))].append(s)
        return [value for _, value in string_dict.items()]