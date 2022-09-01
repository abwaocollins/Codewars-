import math
def make_readable(seconds):
    ss = int(seconds % 60)
    mm = int(((seconds - ss) / 60)%60)
    hh = int(((((seconds - ss) / 60)-mm)/60)%100)

    return f"{hh:02d}:{mm:02d}:{ss:02d}"

print(make_readable(60))