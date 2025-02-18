import re

# Läs in fil
text_path = "dna_raw.txt"
with open(text_path, "r") as file:
    raw_text = file.read()


def count_dna(raw_text):
    dna_dictionary = {}  # tom dict
    sequences = raw_text.strip().split(">")  # splittar vid > tecknet

    for sequence in sequences[
        1:
    ]:  # loopar igenom varje sekvens, hoppar över det första tomma
        lines = sequence.strip().split(
            "\n"
        )  # delat alla tecken till egna rader och vid ny rad
        key = lines[0]  # Sparar index 0 som KEY (sekvensid)
        value = "".join(
            lines[1:]
        ).lower()  # börjar på index 1 då index 0 är sekvensID. ''.join() gör att det blir utan space.
        # print(value) # value innehåller nu alla bokstäver för varje sekvens på var sin rad

        # skapar en ny dictionary med 4 nyckel/värde-par, döper första till a och räknar antalet a i sekvensen
        dna_counting = {
            "a": value.count("a"),
            "t": value.count("t"),
            "c": value.count("c"),
            "g": value.count("g"),
        }

        # kopplar sekvenserna i ursprungsdictionaryn till antalet räknade tecken i dna_counting-dictionaryn
        dna_dictionary[key] = dna_counting

    return dna_dictionary


result = count_dna(raw_text)  # resultatsdictionaryn

# Loopa igenom och skriv ut varje key och value i resultatsdictionaryn
for key, value in result.items():
    print(f" Sequence: {key}\n DNA counts: {value}")
    print()

# Visa diagram över frekvensen av bokstäver
