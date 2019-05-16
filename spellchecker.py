



# WORDS = open('file_path.txt', 'r').read().strip().split()
WORDS = ['home', 'Assignment', 'school', 'bag']

class SpellChecker:

    def __init__(self):
        pass

    def edits1(self, word):
        "All edits that are one edit away from `word`."
        letters = 'abcdefghijklmnopqrstuvwxyz'
        splits = [(word[:i], word[i:]) for i in range(len(word) + 1)]
        deletes = [L + R[1:] for L, R in splits if R]
        transposes = [L + R[1] + R[0] + R[2:] for L, R in splits if len(R) > 1]
        replaces = [L + c + R[1:] for L, R in splits if R for c in letters]
        inserts = [L + c + R for L, R in splits for c in letters]
        return set(deletes + transposes + replaces + inserts)

    def edits2(self, word):
        "All edits that are two edits away from `word`."
        return (e2 for e1 in self.edits1(word) for e2 in self.edits1(e1))

    def candidates(self, word):
        "Generate possible spelling corrections for word."
        return (self.known([word]) or self.known(self.edits1(word)) or self.known(self.edits2(word)) or [word])

    def known(self, words):
        "The subset of `words` that appear in the dictionary of WORDS."
        return set(w for w in words if w in WORDS)

    def fused_words(self, word):
        """
        If two word are joined it will be handled

        """
        correct_words= []

        for i in range(len(word)):
            word_1 = word[:i]
            word_2 = word[i:]
            if (word_1 in WORDS) and (word_2 in WORDS):
                correct_words.append(word_1+' '+ word_2)

        return correct_words

    def correction(self, word):

        if word not in WORDS:
            final_list = self.candidates(word) + self.fused_words(word)
        else:
            final_list = []
        final_list.remove(word)
        return final_list







