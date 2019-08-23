class Hangman:
    '''
    Holds the state for a single instance of a hangman game.
    '''
    def __init__(self, words):
        self.score = 0
        # Player loses if score becomes greater than this number, i.e. they have this many check failures
        self.max_score = 5
        self.words = words.strip().split()
        self.current = [ bytearray('_'*len(w), 'utf-8') for w in self.words ]
        self.checked_letters = set()
        for w in self.words:
            assert(w.isalpha()), "Cannot play hangman with non alphabetic characters"

    def check_letter(self, letter):
        assert(letter not in self.checked_letters), "Already checked letter '{}'.".format(letter)
        self.checked_letters.add(letter)
        assert(letter.isalpha())
        found = False
        for i in range(len(self.words)):
            for j in range(len(self.words[i])):
                if self.words[i][j] == letter:
                    self.current[i][j] = ord(letter);
                    found = True
        if not found:
            self.score+=1

    def check_win(self):
        return self.get_current_string() == self.get_words_string()

    def check_loss(self):
        return self.score > self.max_score

    def get_current_string(self):
        '''
        Get the current string that has been discovered
        '''
        return ' '.join([ c.decode('utf-8') for c in self.current ])

    def get_words_string(self):
        '''
        Get a string of the words that need to be matched
        '''
        return ' '.join(self.words)

    def play(self, letter):
        '''
        Simulate a turn
        '''
        self.check_letter(letter)
        print('Letters checked: ' + ', '.join(sorted(self.checked_letters)))
        print('Current Words: ' + self.get_current_string())
        print('Score: ' + str(self.score))

        

def main():
    #hm = Hangman('some words for testing')
    hm = Hangman('asdf')
    while (not hm.check_win() and not hm.check_loss()):
        c = input().strip()
        hm.play(c)
    if hm.check_win():
        print('Victory!')
    elif hm.check_loss:
        print('Defeat...')


if __name__ == '__main__':
    main()
