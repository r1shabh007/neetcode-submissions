class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # create a dictionary wiht lists
        sorted_words = defaultdict(list)
        for word in strs:
            key = [0] * 26
            for letter in word:
                key[ord(letter) - ord("a")] += 1
            sorted_words[tuple(key)].append(word)
        return list(sorted_words.values())