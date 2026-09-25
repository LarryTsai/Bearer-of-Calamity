"""Validate current reading copies; --sync regenerates them from current sources."""
import sys
from build_story import main

if __name__ == '__main__':
    if '--sync' in sys.argv:
        sys.argv.remove('--sync')
    elif '--check' not in sys.argv:
        sys.argv.append('--check')
    raise SystemExit(main())
