#!/usr/bin/env python3
"""
  sum_timestamps.py

  takes a list of timestamps in format:
    ["1:30", "11:49"]
  and returns the sum in the same format
"""

def sum_timestamps(timestamps):
    hrs = mins = secs = 0

    for stamp in timestamps:
        times = stamp.split(':')
        secs += int(times[-1])
        mins += int(times[-2])
        try: hrs += int(times[-3])
        except: pass

    mins += int(secs/60)
    secs = secs % 60
    hrs += int(mins/60)
    mins = mins % 60

    hrs = f"{hrs}:" if hrs else ""
    mins = f"{mins:02d}:" if hrs else f"{mins}:"
    secs = f"{secs:02d}" if mins else f"{secs}"

    return hrs + mins + secs
