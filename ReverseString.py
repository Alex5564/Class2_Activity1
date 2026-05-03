class Reverse:

    def __init__(self, string):
        self.string = string

    def reverse_string(self):
        return self.string[::-1]

user_word = input("Enter a string to reverse: ")
reverser = Reverse(user_word)
print(f"Reversed String: {reverser.reverse_string()}")        