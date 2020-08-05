from kh2lib import CodeGen
import os
cg = CodeGen(out_fn=os.path.join("cheats","F266B00B.pnach"))
v = cg.read_csv("bosstable.csv")
del v[1]
# csv for each world
# for each boss (source)
# loop through each boss
# skip if self or a replace only
# put info for replacement in world (mention if important)
ws = {}
for o in v:
    original = v[o]
    w = original["world"]
    if w == "06b":
        w = "06"
    old_id = o
    if w not in ws:
        ws[w] = []
    for n in v:
        new = v[n]
        new_id = n
        if new == original:
            continue
        if "ReplaceOnly" in new["ttype"]:
            continue
        important = "Maybe"
        if new["ttype"] == "Second":
            important = "No"
        if original["ttype"] == "ReplaceOnlySecond":
            important = "No"
        # old_id, new_id, old boss, new boss, likely to work
        r = [old_id, new_id, original["name"], new["name"], important]
        ws[w].append(r)
for c in ws:
    import csv
    with open('{}.csv'.format(c), 'w', newline='') as csvfile:
        spamwriter = csv.writer(csvfile)
        spamwriter.writerow(["old_id","new_id","old boss","new boss","likely to work", "working/functional/broken","notes"])
        for row in ws[c]:
            spamwriter.writerow(row)
    
    
    
