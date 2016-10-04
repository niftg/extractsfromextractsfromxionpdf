from xml.etree import ElementTree

def treeprepare(fname):
    with open(fname,"rt") as f:
        return ElementTree.parse(f)

def fontfind(font,tree):
    pages = tree.findall(".//page")
    r = []
    for p in pages:
        for i in p.findall(".//textbox"):
            for j in i.findall(".//textline"):
                t = ""
                for k in j.findall(".//text[@font='ABCDEE+%s']"%font):
                    t += k.text
                if len(t.strip())>0:
                    r.append({
                        "p":int(p.get("id")),
                        "b":int(i.get("id"))+1,
                        "t":t
                        })
    return r

def findlogexport(pbt, fname):
    f = open(fname, "w")
    for i in pbt:
        f.write(("{p}:{b}\t{t}".format(**i)).strip())
        f.write("\n")
    f.close()

tree = treeprepare("D:\\xionpdf\\xionpdf_xmlextract.xml")
for i in ["kardinal", "ayaka"]:
    findlogexport(fontfind(i, tree), "D:\\xionpdf\\{0}findlog.tsv".format(i))
    print i + " OK"
