class StringExercise:

    def __init__(self):
        pass   # Do some initial setup in this constructor method, if needed

    def reverse_string(self, input_str):
        """
        Reverses order of characters in string input_str.
        """
        rev=input_str[::-1]
        return rev

    def is_english_vowel(self, character):
        """
        Returns True if character is an english vowel
        and False otherwise.
        """
        if character=='a' or character=='e' or character=='i' or character=='o' or character=='u':
            return True
        if character=='A' or character=='E' or character=='I' or character=='O' or character=='U':
            return True
        return False

    def find_longest_word(self, sentence):
        """
        Returns the longest word in string sentence.
        In case there are several, return the first.
        """
        words=sentence.split(" ")
        max=-1
        ans=""
        for word in words:
            if(len(word)>max):
                max=len(word)
                ans=word
        return ans

    def get_word_lengths(self, text):
        """
        Returns a list of integers representing
        the word lengths in string text.
        """
        lst=[]
        words=text.split(" ")
        for word in words:
            lst.append(len(word))
        return lst


