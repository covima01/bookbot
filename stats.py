def word_count(text):
    words = text.split()
    num_words = len(words)
    return num_words

def char_count(text):
    characters = {}
    t_count = 0  # Special counter for 't'
    
    for char in text:
        lower_char = char.lower()
        
        if lower_char == 't':  # Special debug for 't'
            t_count += 1
            
        if lower_char not in characters:
            characters[lower_char] = 1
        else:
            characters[lower_char] += 1
            
    return characters

def sorted_list(characters):
   sorted_dictionary = dict(sorted(characters.items(), key=lambda x: x[1], reverse=True))
   result = []
   for character in sorted_dictionary:
      if character.isalpha():
         result.append(f"{character}: {sorted_dictionary[character]}")
   
   return result
