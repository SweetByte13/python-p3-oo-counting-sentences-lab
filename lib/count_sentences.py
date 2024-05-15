#!/usr/bin/env python3

import re


class MyString:
  def __init__(self, value=''):
    self.value = value
    if value is str:
        self._value = value
    else:
        print("The value must be a string.")
 
  def is_sentence(self):
      return self.value.endswith('.')
  def is_question(self):
      return self.value.endswith('?')
  def is_exclamation(self):
      return self.value.endswith('!')
    
  def count_sentences(self):
        listOfSentences = re.split(r'[.?!]', self.value)
        sentences = list(filter(None, listOfSentences))
        countOfSentences =  len(sentences)
        return int(countOfSentences)