import re

fp = "1067HajjiKhalifa.KashfZunun.Shia003356Vols-ara1"

letters = "ابتثجحخدذرزسشصضطظعغفقكلمنوهي"

with open(fp, mode="r", encoding="utf-8") as file:
    text = file.read()

def get_index_of_first_two_letters(par):
    if par[:2] == "ال":
        a, b = par[2:4]
    else:
        a, b = par[:2]
    try:
        a = letters.index(a)
        b = letters.index(b)
        return a, b
    except:
        return None, None

chapters = text.split("### | ")
new = chapters[0]
for i, c in enumerate(chapters[1:]):
    print(i)
    if i == 0: # chapter alif
        new += "### | " + c
    else:
        pars = re.split("[\r\n]+# ", c)
        new += "### | "+pars[0]
        prev = 0
        for j, par in enumerate(pars[1:]):
            nxt = prev + 6
            for k in range(1, 10): # check the second letter of the next paragraphs
                try:
                    next_par = pars[j+k]
                    if i == letters.index("غ"):
                        print(next_par[:10])
                except:
                    print("no next paragraph")
                    continue
                a, b = get_index_of_first_two_letters(next_par)
                #print(a,b)
                if b:
                    nxt = b
                    break
##            try:
##                if par[:2] == "ال":
##                    a, b = par[2:4]
##                else:
##                    a, b = par[:2]
##                a = letters.index(a)
##                b = letters.index(b)
            a, b = get_index_of_first_two_letters(par)
            if a:
                if i == letters.index("غ"):
                    print(a, b, prev, nxt)
                #print(a,b, prev)
                if a != i:
                    new += "\n# " + par
                elif prev <= b <= nxt:
                    new += "\n### $ " + par
                    prev = b
                else:
                    new += "\n# " + par
                #print("passed")
##            except:
            else:
                new += "\n# " + par

with open(fp+"_test", mode="w", encoding="utf-8") as file:
    file.write(new)

##    
##            if re.findall("^(?:ال)?{}".format(letters[i]), par):
##                print("### $ " + par[:15])
##            else: print("# " + par[:15])
##    

