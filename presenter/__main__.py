import argparse
from pathlib import Path
import sys

parser = argparse.ArgumentParser()
parser.add_argument('component', choices=['dm', 'player'])
args = parser.parse_args()

DIR = Path(__file__).resolve().parent
sys.path.append(str(DIR.parent))

match args.component:
    case 'dm':
        from presenter import dm
        dm.main(args)
    case 'player':
        from presenter import player
        player.main(args)
