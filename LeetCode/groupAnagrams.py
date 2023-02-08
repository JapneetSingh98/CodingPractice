class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        output = {}
        for word in strs:
            srtd = ''.join(sorted(word))
            if srtd in output:
                output[srtd].append(word)
            else:
                output[srtd] = [word]

        act_output = []
        for key in output:
            act_output.append(output[key])
        return act_output