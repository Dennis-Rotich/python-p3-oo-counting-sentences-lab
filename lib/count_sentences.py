#!/usr/bin/env python3

class MyString:
  def __init__(self, value = ''):
    if type(value) is str:
      self.value = value
    else:
      print("The value must be a string.")

  @property
  def value(self):
    return self._value
  
  @value.setter
  def value(self, v):
    if isinstance(v,str):
      self._value = v
    else:  
      print("The value must be a string.")

  def is_sentence(self):
    if self.value[-1] == ".":
      return True
    else:
      return False
    
  def is_question(self):
    if self.value[-1] == "?":
      return True
    else:
      return False 

  def is_exclamation(self):
    if self.value[-1] == "!":
      return True
    else:
      return False

  def count_sentences(self):
    # Split the string into a list of sentences
    sentences = self.value.split('.') + self.value.split('!') + self.value.split('?')
    # Remove any empty strings from the list
    sentences = [sentence for sentence in sentences if sentence]
    # Return the count of sentences
    length = len(sentences)
    if length == 0:
      return 0
    return length-2      
  pass

simple_string = MyString("one. two. three?")
empty_string = MyString()
complex_string = MyString("This, well, is a sentence. This is too!! And so is this, I think? Woo...") 
print(simple_string.count_sentences())
print(empty_string.count_sentences())
print(complex_string.count_sentences())