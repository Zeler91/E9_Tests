import random

word_base = ['skillfactory', 'testing', 'blackbox', 'pytest', 'unittest', 'coverage']
attempts = 4

def fill_base_from_file(path_file):
    word_base = []
    f = open(path_file, encoding="utf-8")
    for word in f:
        word_base.append(word[:-1])
    return word_base


class AI():
    wb = []
    secret_word = ''
    current_word = ''
    attempts_count = 0

    def init_conf(self, word_base, att):
        self.wb = word_base
        self.attempts_count = att
        self.secret_word = self.wb[random.randint(0,len(self.wb) - 1)]

    def split(self, word):
        space_word = ''
        for i in range(0, len(word)):
            space_word += word[i] + " "
        return space_word

    def print_word(self, let = ''):
        if not let:
            for i in range(0, len(self.secret_word)):
                self.current_word += "_"
        else:
            find_let = self.secret_word.find(let, 0, len(self.secret_word))
            if find_let != -1:
                for i in range(0, self.secret_word.count(let, 0, len(self.secret_word))):
                    self.current_word = self.current_word[0:find_let] + self.secret_word[find_let] + self.current_word[find_let+1:]
                    find_let = self.secret_word.find(let, find_let+1, len(self.secret_word))
        return self.split(self.current_word)
    
    def check_letter(self, let):
        if let not in self.secret_word:
            self.attempts_count -= 1
            return "Wrong! " + "You have {} attempts".format(self.attempts_count)
        else:
            return "Good! " + "You have {} attempts".format(self.attempts_count)

def play_test():
    bot = AI()
    rus_base = fill_base_from_file("word_rus.txt")
    bot.init_conf(word_base, attempts)
    # bot.init_conf(rus_base, attempts)
    print(bot.print_word())
    while bot.attempts_count > 0:
        print("Type letter")
        letter = input()
        print(bot.check_letter(letter))
        print(bot.print_word(letter))
        if bot.attempts_count <= 0:
            print("You lose!!! The secret word was - " + bot.secret_word)
            break
        if bot.current_word == bot.secret_word:
            print("You win!!!")
            break



if __name__ == '__main__':  
    play_test()

