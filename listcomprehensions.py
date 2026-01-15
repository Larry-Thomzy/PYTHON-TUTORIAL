# List Comprehensions
# List Comprehensions is a very powerful tool, which creates a new list based on another list, in a single, readable line.


sentence = "I am a python dev"
sent_list = sentence.split()
print(sent_list)


#This program create a list of integers which specify the length of each word in a certain sentence, but only if the word is not the word "the".


sentence = "the quick brown fox jumps over the lazy dog"
words = sentence.split()
word_lengths = []
for word in words:
      if word != "the":
          word_lengths.append(len(word))
print(words)
print(word_lengths)



# another way of doing this
sentence = "the quick brown fox jumps over the lazy dog"
words = sentence.split()
word_lengths = [len(word) for word in words if word != "the"]
print(words)
print(word_lengths)