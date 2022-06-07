marvelchars= {
"Starlord":
  {"real name": "peter quill",
  "powers": "dance moves",
  "archenemy": "Thanos"},

"Mystique":
  {"real name": "raven darkholme",
  "powers": "shape shifter",
  "archenemy": "Professor X"},

"Hulk":
  {"real name": "bruce banner",
  "powers": "super strength",
  "archenemy": "adrenaline"}
             }
char_name = input("Which character do you want to know about? (Starlord, Mystique, Hulk)\n")

char_stat = input("What statistic do you want to know about? (real name, powers, archenemy)\n")

if char_name=="Starlord".lower():
    if char_stat=="real name":
        print(char_name.title() + "'s", char_stat, "is:", marvelchars["Starlord"]["real name"])
    if char_stat=="powers":
        print(char_name.title() + "'s", char_stat, "are:", marvelchars["Starlord"]["powers"])
    if char_stat=="archenemy":
        print(char_name.title() + "'s", char_stat, "is:", marvelchars["Starlord"]["archenemy"])

if char_name=="Mystique".lower():
    if char_stat=="real name":
        print(char_name.title() + "'s", char_stat, "is:", marvelchars["Mystique"]["real name"])
    if char_stat=="powers":
        print(char_name.title() + "'s", char_stat, "are:", marvelchars["Mystique"]["powers"])
    if char_stat=="archenemy":
        print(char_name.title() + "'s", char_stat, "is:", marvelchars["Mystique"]["archenemy"])



if char_name=="Hulk".lower():
    if char_stat=="real name":
        print(char_name.title() + "'s", char_stat, "is:", marvelchars["Hulk"]["real name"])
    if char_stat=="powers":
        print(char_name.title() + "'s", char_stat, "are:", marvelchars["Hulk"]["powers"])
    if char_stat=="archenemy":
        print(char_name.title() + "'s", char_stat, "is:", marvelchars["Hulk"]["archenemy"])                                               
