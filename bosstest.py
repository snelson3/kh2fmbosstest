from kh2lib import CodeGen
import os,sys

if not len(sys.argv) == 3:
    raise Exception("Usage: python bosstest.py <original_boss> <new_boss>")

cg = CodeGen(out_fn=os.path.join("cheats","F266B00B.pnach"))

## Uncomment these then start a new game to make a new file with ease
#cg.apply_all_abilities()
#cg.apply_all_forms()
#cg.apply_all_items()

## If your bad like me uncomment this so you don't die
#cg.apply_inf_hp()

# Uncomment to have roxas able to do RC commands (makes fights more likely to not softlock)
#cg.apply_roxas_rc_code()

cg.replace_boss(int(sys.argv[1]),int(sys.argv[2]))

cg.write_pnach(debug=False)