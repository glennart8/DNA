# regular expression
import re
text_path = "dna_raw.txt" # relative path
with open(text_path, "r") as file:
    raw_text = file.read()

# Separera sekvenserna 
# Gör alla bokstäver små
# Skapa dictionarys av varje sekvens där seq1 är nyckeln och cGTA... är value
# Räkna antalet av resp bokstav
# Visa diagram över frekvensen av bokstäver


print(raw_text)



text_fixed_spacing = re.sub(r"\s+"," ", raw_text)
text_list = [text.capitalize() for text in text_fixed_spacing.split(". ")]

# join with newlines for each sentence, we could choose another design
cleaned_text = ".\n".join(text_list)


