"""Compatibility audit: current builder preserves ordinary Markdown sections."""
import sys
from build_story import main
if __name__ == '__main__':
    if '--check' not in sys.argv:
        sys.argv.append('--check')
    raise SystemExit(main())
