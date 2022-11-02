class Solution:
    def stringMatching(self, words: List[str]) -> List[str]:
        output = []
        words.sort(key=len)
        for i in range(len(words)):
            for word in words[i+1:]:
                if words[i] in word:
                    output.append(words[i])
                    break
        return output