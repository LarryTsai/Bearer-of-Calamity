"""Compatibility entry point; current layout is managed by build_story.py."""
import sys
from build_story import main

if __name__ == '__main__':
    raise SystemExit(main())
