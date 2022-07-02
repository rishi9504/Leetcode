class Solution:
    def toGoatLatin(self, sentence: str) -> str:
        sentence = sentence.split(' ')
        vowel_list = ['a', 'e', 'i', 'o', 'u']
        ma = 'ma'
        for i in range(len(sentence)):
            if sentence[i][0].lower() in vowel_list:
                sentence[i]+=ma
            else:
                sentence[i] = sentence[i][1:] + sentence[i][0] + ma
            sentence[i] += 'a' * (i+1)
        return ' '.join(sentence)
        
