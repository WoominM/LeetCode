class Solution:
    def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:
        import collections
        import re

        paragraph = re.sub(r'[^\w]', ' ', paragraph).lower().split()
        paragraph = [word for word in paragraph if word not in banned]

        counts = collections.Counter(paragraph)
        return counts.most_common(1)[0][0]