import sys

def read_text_from_file(filename):
  with open(filename,"r",errors="ignore") as file:
    text = file.read()
  return(text)

"""Accepts a string and should return the number of words in the string"""
def count_words(text):
  "TODO: missing code"
  return(0)

"""Accepts a string and should count the number of alphabetic letters
recall that .isalpha() will check if a character is alphabetic"""
def count_letters(text):
  "TO DO: Missing code"
  return(0)

"""Accepts a string and should estimate the number of sentences. Hint:
What character(s) do most sentences tend to end with? """
def count_sentences(text):
  "TODO: Missing code"
  return(0)

"""Accepts a string and 
should employ the helper functions above to count 
the number of words, letters, and sentences

Then, use the Coleman-Liau Index to compute 
the readability index and return it
"""
def compute_readability(text):
  """TO DO: Missing code"""
  return(0)

"""
Already implemented harness function to read text from 
a tile, compute the readability index, and then
return the estimated reading level 
"""
def readability(filename):
  text = read_text_from_file(filename).replace("\n","")
  grade = compute_readability(text)
  if (grade < 1):
    print("Suggested Reading Grade: Pre-K")
  elif (grade > 16):
    print("Suggested Reading Grade: Graduate")
  else:
    print("Suggested Reading Grade: " + str(round(grade)))

def main():
  readability(sys.argv[1])
