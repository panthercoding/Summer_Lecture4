"""
run pip install pandas in the Shell to download the Pandas module 
"""
import pandas as pd 

"""
Accepts a word token (string) and should remove
any non-alphabetic characters at the beginning and end of the word

Should return an empty string "" if there are no alphabetic characters
(try counting them using the count_letters helper function from readability)

I recommend removing non-alphabet characters starting at the beginning until
we reach an alphabet character (while loop), and vice versa for the string end,
and then returning the cleaned word.
"""
def clean_word(word):
 """missing code"""
 return(0)
 
"""
Accepts a list of words and should build a new list
of words without any duplicates. I recommend starting with an empty
list for the new list and adding each word of word_list if the word does not
already appear in the new list. Then, it should return the new list of words.
"""
def remove_duplicates(word_list):
 """ missing code """

"""
Pre-written function (no TODO) that reads the csv file containing Taylor Swift lyrics
and returns a Pandas dataframe (which is analyzed in the next function).
"""
def build_database(filename):
  df = pd.read_csv("taylor_swift_lyrics.csv",encoding="latin1")
  return(df)

"""Should return an inverted index as specified below """
def build_index(database):
  index = {}

  num_entries = database.shape[0]
  for entry_number in range(num_entries):
    lyric_data = database.iloc[entry_number]

    song_name = lyric_data["track_title"]
    album_name = lyric_data["album"]
    lyric_words = lyric_data["lyric"].split(" ")

    """
    TODO: First, use string concatenation to make a combined
    title for the song in the form "songName (album Name)"
    with parantheses.
    
    Then, form a new list of cleaned words
    by iterating through each word in lyric_words and using the
    function clean_words. Finally, modify your list using
    remove_duplicates so that each word is unique. 

    Finally, iterate through your list of cleaned, unique words in 
    the lyric line, check if each word is already in the index (dictionary). It 
    it is, add it to the set affiliated with the word using the .add() method. 
    Otherwise, create a new dictionary entry with the key being the word
    and the correspoding value between a set containing the combined title.

    The goal is to build a dictionary that maps words to songs that contain them
    """
  return(index)

def search(index):
 print("-------------------------------------------------")
 print("Search for Taylor Swift Songs Using a Lyric Word")
 print("-------------------------------------------------\n")
 query = input("Enter a Search Request (ENTER/RETURN to quit): ")
 while (query != ""):
   query = clean_word(query)
   if (query in index.keys()):
     songs = sorted(list(index[query]))
     print("\nSongs Found\n--------------")
     for song in songs:
       print(song)
   else:
     print("No song found")
   query = input("\nEnter a Search Request (ENTER/RETURN to quit): ")

 print("Awesome! Hope you enjoyed our service.")

def main():
  df = build_database("taylor_swift_lyrics.csv")
  index = build_index(df)
  search(index) 

main()
