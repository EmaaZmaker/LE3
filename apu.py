class Reverse:
    def __init__(self, text):
        self.text = text

    def reverse_words(self):
        words = self.text.split()
        reversed_words = words[::-1]

        result = ""
        for word in reversed_words:
            result += word + " "
        
        return result.strip() 
sentence = input("Type a sentence: ")
r = Reverse(sentence)
print("Your sentence with words reversed:")
print(r.reverse_words())
