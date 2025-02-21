import matplotlib.pyplot as plt

# Läs in fil
text_path = "dna_raw_complicated.txt"
with open(text_path, "r") as file:
    raw_text = file.read()


def count_dna(raw_text):
    dna_dictionary = {}  # tom dict
    sequences = raw_text.strip().split(">")  # splittar vid > tecknet

    for sequence in sequences[1:]:  # loopar igenom varje sekvens, hoppar över det första tomma
        lines = sequence.strip().split("\n")  # delat alla tecken till egna rader och vid ny rad
        key = lines[0]  # Sparar index 0 som KEY (sekvensid)

        # value = "".join(lines[1:]).lower()  # börjar på index 1 då index 0 är sekvensID. ''.join() gör att det blir utan space.
        value = ''.join(lines[1:]).replace(' ', '').lower() # Joinar alla bokstäver till en sträng, oavsett newline
        value = ''.join(char for char in value if char in 'atcg') # list comprehension - behåller endast a,t,c och g för att ta hand om oönsakd tecken som "N"
        
        # print(value) # value innehåller nu alla bokstäver för varje sekvens på var sin rad

        # Fick hjälp att med DEBUB av CHATGPT då inte alla tecken visades i dna_raw_complicated.
        # Problemet var att texten innehöll andra bokstäver än atcg och dessa behövde filtreras bort
        print(f"DEBUG - Sequence ID: {key}")
        print(f"DEBUG - Sequence value: {value}")
        print(f"DEBUG - Length of sequence: {len(value)}")

        # skapar en ny dictionary med 4 nyckel/värde-par, döper första till a och räknar antalet a i sekvensen
        dna_counting = {
            "a": value.count("a"),
            "t": value.count("t"),
            "c": value.count("c"),
            "g": value.count("g"),
        }

        # Felsökning, skriver ut räkningen
        print(f"DEBUG - DNA counts for {key}: {dna_counting}")
        print()

        # kopplar sekvenserna i ursprungsdictionaryn till antalet räknade tecken i dna_counting-dictionaryn
        dna_dictionary[key] = dna_counting
        
    return dna_dictionary

result = count_dna(raw_text)  # resultatsdictionaryn

# Loopa igenom och skriv ut varje key och value i resultatsdictionaryn
for key, value in result.items():
    print(f" Sequence: {key}\n DNA counts: {value}")
    print()


# Visa diagram över frekvensen av bokstäver

def plot_dna_frequency(dna_dictionary):
    for key, value in dna_dictionary.items():
        plt.figure(figsize=(5, 5)) # anger storleken
        plt.bar(value.keys(), value.values()) # skapar ett stapeldiagram med keys och values
        plt.title(f"DNA Frequency for {key}") # sätter titel
        plt.xlabel("DNA-letters") # sätter labels på x-axeln
        plt.ylabel("Amount") # sätter labels på y-axeln
        plt.show() # visar diagrammen

plot_dna_frequency(result)