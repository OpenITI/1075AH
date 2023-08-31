import re

fp = "1069ShihabDinQalyubi.HashiyataQalyubiWaCumayra.Shamela0021843-ara1"

matn_fp = "0676Nawawi.MinhajTalibin.Shamela0021843BK1-ara1"
h1_fp = "1069ShihabDinQalyubi.HashiyataQalyubi.Shamela0021843BK2-ara1"
h2_fp = "0957ShihabDinRamli.HashiyataCumayra.Shamela0021843BK3-ara1"

with open(fp, mode="r", encoding="utf-8") as file:
    text = file.read()

header, splitter, text = re.split("(#META#Header#End#)", text)
print(len(text))
matn = ""
h1 = ""
h2 = ""

spans = [
    '<span class="matn">',
    '</span><span class="matn-hr"></span>',
    '<span class="matn-hr"></span>'
    ]


for page in re.split("(PageV\d+P\d+)", text):
    if page.startswith("Page"):
        print(page)
        matn += "\n" + page + "\n"
        h1 += "\n" + page + "\n"
        h2 += "\n" + page + "\n"
    else:
        spl_page = re.split("<[\n~# ]*span", page)
        try:
            matn += "~~"+spl_page[1]
            h1 += spl_page[2]
            h2 += spl_page[3]
        except:
            print("Not exactly for elements on page")

matn, h1, h2 = [re.sub("</span>", "", t) for t in [matn, h1, h2]]
matn, h1, h2 = [re.sub(' *class[\n~#]*=[\n~#]*"matn[\n~#]*-?[\n~#]*[\n~#]*h?[\n~#]*r?[\n~#]*">', "", t) for t in [matn, h1, h2]]        
h1, h2 = [re.sub("### \| \[حاشية.+", "", t) for t in [h1, h2]]
matn, h1, h2 = [re.sub("# \n|~~\n", "", t) for t in [matn, h1, h2]]
with open(matn_fp, mode="w", encoding="utf-8") as file:
    file.write(header+splitter+matn)
with open(h1_fp, mode="w", encoding="utf-8") as file:
    file.write(header+splitter+h1)
with open(h2_fp, mode="w", encoding="utf-8") as file:
    file.write(header+splitter+h2)
