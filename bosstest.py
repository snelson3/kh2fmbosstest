from kh2lib import CodeGen
import os,sys

if not len(sys.argv) == 3:
    raise Exception("Usage: python bosstest.py <original_boss> <new_boss>")

cg = CodeGen(out_fn=os.path.join("cheats","F266B00B.pnach"))

## Run these then start a new game to make a new file with ease
#cg.apply_all_abilities()
#cg.apply_all_forms()
#cg.apply_all_items()

## If your bad like me uncomment this so you don't die
#cg.apply_inf_hp()

cg.replace_boss(int(sys.argv[1]),int(sys.argv[2]))

cg.write_pnach(debug=False)