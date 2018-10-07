#
#   Use this class definition to work from.
#   This way of reading the dictionary is quite messy.
#   It is done this way to make testing easier.
#
from Node import Node
from string import ascii_lowercase
from read_dictionary import read_dictionary

valid_words = None

class WordGameNode(Node):
   def __init__(self, name, parent = None):
      # Ensure lowercase letters (no digits or special chars)
      for letter in name:
         assert letter in ascii_lowercase

      # dictionary made global so words of same length don't have to traverse dictionary again
      global valid_words
      if valid_words == None or len(valid_words) != len(name):
         # We only need to examine words which have the same length as our word (self.name)
         valid_words = read_dictionary("/etc/dictionaries-common/words", len(name))
      self.name = name
      self.parent = parent

   def __str__(self):
      return self.name

   def get_children(self):
      # all one letter mutations of the word
      child_words = []
      
      for i, letter in enumerate(self.name):
          for j in range(26):
            if chr(ord("a") + j) != letter and self.name[:i] + chr(ord("a") + j) + self.name[i+1:] in valid_words:
                child_words.append(WordGameNode(self.name[:i] + chr(ord("a") + j) + self.name[i+1:], WordGameNode(self.name)))
      
      return child_words # return a list of WordGameNode objects.

   def get_path(self):
      return path
