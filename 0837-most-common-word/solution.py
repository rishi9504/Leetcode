from collections import Counter
import re

class Solution:
    def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:
        c = Counter(re.split('[!?\',;. ]', paragraph.lower()))
        for (word, count) in c.most_common():
            if word not in banned and word != '':
                return word
