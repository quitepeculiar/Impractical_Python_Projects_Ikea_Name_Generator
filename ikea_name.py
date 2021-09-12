import random

first = ("Brunstarr", "Kristianne", "Idalinnea", "Sissil", "Rödask", "Hedsäv",
         "Leikny", "Tilltalande", "Hallvi", "Sanela", "Malm", "Nordli", "Flekke",
         "Friheten", "Vimle", "Vallentuna", "Ektorp", "Vinliden", "Söderhamn",
         "Ekenäset", "Kivik", "Askeby", "Holmsund", "Alex", "Linnmon", "Dvala",
         "Lönset", "Rosenskärm", "Rumsmalva", "Skogslök", "Lyktfibbla", "Turill",
         "Sarakajsa", "Oddhild", "Bernhardina", "Ingunn", "Evali", "Vallkrassing",
         "Moalie", "Pedersborg", "Resenstad", "Ugilt", "Kattrup", "Törslev",
         "Vistoft", "Råvaror", "Tannisby", "Vadheim", "Idanäs", "Hauga", "Hafslo",
         "Vadsö", "Hokkåsen", "Vatneström", "Tussöy", "Hyllis", "Dröna", "Lekman",
         "Gopån", "Rejsa", "Rissla", "Kuggis", "Pallra", "Hyvens", "Manick", "Flysta")

last = ("Åsveig", "Gunva", "Drakblomma", "Skäggört", "Mildrun", "Stenmätare",
        "Taggbräken", "Hervor", "Kryddbuske", "Brandspira", "Brimnes", "Hemnes",
        "Släkt", "Flottebo", "Lycksele", "Nockeby", "Bråthult", "Stocksund",
        "Sälleryd", "Sandbacken", "Landskrona", "Nyhamn", "Malfors", "Kallax",
        "Adils", "Luröy", "Mjölkklocka", "Praktvädd", "Klubbsporre", "Vänderot",
        "Omtänksam", "Gurli", "Vitmossa", "Ingabritta", "Gråfibbla", "Polarvide",
        "Tiphede", "Spangsbro", "Skanderup", "Klejs", "Lohals", "Taulov",
        "Lisbjerg", "Rörkär", "Resenstad", "Slattum", "Gladstad", "Songesand",
        "Hamarvik", "Hyllestad", "Hövåg", "Drömmande", "Lack", "Bestå", "Bläddra",
        "Malaren", "Lurpassa", "Tjena", "Tjog", "Sockerbit", "Kvarnvik", "Fjällbo")

print("So you need a name for your NPC in an RPG.\n")
print("Here's a name for that character, inspired by a certain Swedish company:")

while True:
    firstName = random.choice(first)
    lastName = random.choice(last)

    print("\n")
    print("{} {}".format(firstName, lastName))
    #print("\n")

    try_again = input("\nHow does this suit? Want another name? \n(Enter y go again, or else n to quit) \n ")
    if try_again.lower() == "n":
        break

input("\nPress Enter to exit.")
