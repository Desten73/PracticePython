class WordsFinder:
    def __init__(self, *filename):
        self.__file_name = filename

    def get_all_words(self):
        all_words = {}
        for name in self.__file_name:
            with open(name, encoding="utf-8") as text:
                text = text.read()
                remove_symbol = [',', '.', '=', '!', '?', ';', ':', ' - ']
                for symbol in remove_symbol:
                    text = text.replace(symbol, "")
                all_words[name] = [word.lower() for word in text.split()]
        return all_words

    def find(self, word):
        res = {}
        for name, words in self.get_all_words().items():
            if word.lower() in words:
                res[name] = words.index(word.lower()) + 1
        return res

    def count(self, word):
        res = {}
        for name, words in self.get_all_words().items():
            if word.lower() in words:
                res[name] = words.count(word.lower())
        return res


finder2 = WordsFinder('test.txt')
print(finder2.get_all_words()) # Все слова
print(finder2.find('TEXT')) # 3 слово по счёту
print(finder2.count('teXT')) # 4 слова teXT в тексте всего
