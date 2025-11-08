import os, sys
GOOD = os.getenv("GOOD_HASH","").strip()
BAD  = os.getenv("BAD_HASH","").strip()
CMD  = os.getenv("TEST_CMD","python manage.py test").strip()
if not GOOD or not BAD:
    print("ERROR: set GOOD_HASH and BAD_HASH")
    sys.exit(2)
os.system("git fetch --all --tags --prune")
os.system(f"git bisect start {BAD} {GOOD}")
os.system(f"git bisect run {CMD}")
os.system("git bisect reset")
