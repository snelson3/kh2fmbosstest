from kh2lib import CodeGen
import os,sys

if not len(sys.argv) == 3:
    raise Exception("Usage: python bosstest.py <original_boss> <new_boss>")

cg = CodeGen(out_fn=os.path.join("cheats","F266B00B.pnach"))
cg.apply_all_abilities()
cg.apply_all_forms()
cg.apply_all_items()
cg.apply_inf_hp()
cg.replace_boss(int(sys.argv[1]),int(sys.argv[2]))
#cg.apply_loc_code("test", 14, 89)
cg.write_pnach(debug=False)