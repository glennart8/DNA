import re

# Läs in fil
text_path = "dna_raw.txt"
with open(text_path, "r") as file:
    raw_text = file.read()


def count_dna(raw_text):
    dna_dictionary = {}
    sequences = raw_text.strip().split('>') # 

    for sequence in sequences[1:]: # hoppa över det första tomma
        lines = sequence.strip().split("'\n") # delat alla tecken till egna rader och vid ny rad
        key = lines[0]
        value = ''.join(lines[1:]).lower()
        
        dna_counting = {
            'a': value.count('a'),
            't': value.count('t'),
            'c': value.count('c'),
            'g': value.count('g'),
        }

        dna_dictionary[key] = dna_counting

    return dna_dictionary
        # därefter, spara resterande bokstäver till value


    # dela sekvenserna i par 
    
    # gör en dictionary av varje sekvens och räkna antalet bokstäver
result = count_dna(raw_text)

for key, value in result.items():
    print(f"Sequence: {key}")
    print(f"DNA counts: {value}")
    print()




# Visa diagram över frekvensen av bokstäver
