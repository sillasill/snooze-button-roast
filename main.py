#!/usr/bin/env python3
"""Snooze Button Roast entry: writes one roast line to /output/entry.txt."""

ROAST = "My alarm clock rang at 6 AM on a Saturday like a personal trainer who showed up uninvited \u2014 and the snooze button whispered, 'Pretend you're dead.'"

from pathlib import Path

Path("/output").mkdir(parents=True, exist_ok=True)
Path("/output/entry.txt").write_text(ROAST + "\n", encoding="utf-8")
