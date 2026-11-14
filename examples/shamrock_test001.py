"""TEST-001: Classic Fill Shamrock.

First PES integration target for Brother SE600.
This script intentionally uses explicit stitches so the encoder test is
separate from the future high-level digitizer.
"""
import math
from pathlib import Path
from pyembroidery import EmbPattern, EmbThread
from sthuwan_embroidery.pes import write_se600_pes

MM = 10.0  # pyembroidery coordinate unit = 0.1 mm

def heart_polygon(cx, cy, scale, rotation=0.0, samples=120):
    pts = []
    cr, sr = math.cos(rotation), math.sin(rotation)
    for i in range(samples):
        t = 2 * math.pi * i / samples
        x = 16 * math.sin(t) ** 3
        y = -(13 * math.cos(t) - 5 * math.cos(2*t) - 2 * math.cos(3*t) - math.cos(4*t))
        x *= scale / 32.0
        y *= scale / 32.0
        pts.append((cx + x*cr - y*sr, cy + x*sr + y*cr))
    return pts

def scanline_fill(pattern, polygon, spacing=0.40, stitch=2.5):
    # Simple even-odd horizontal fill for deterministic TEST-001 output.
    ys = [p[1] for p in polygon]
    y = min(ys)
    reverse = False
    while y <= max(ys):
        xs = []
        for a, b in zip(polygon, polygon[1:] + polygon[:1]):
            if (a[1] <= y < b[1]) or (b[1] <= y < a[1]):
                x = a[0] + (y-a[1])*(b[0]-a[0])/(b[1]-a[1])
                xs.append(x)
        xs.sort()
        for j in range(0, len(xs)-1, 2):
            x0, x1 = xs[j], xs[j+1]
            if reverse: x0, x1 = x1, x0
            pattern.move_abs(x0*MM, y*MM)
            n = max(1, int(abs(x1-x0)/stitch))
            for k in range(1, n+1):
                pattern.stitch_abs((x0+(x1-x0)*k/n)*MM, y*MM)
            reverse = not reverse
        y += spacing

p = EmbPattern()
thread = EmbThread()
thread.set("#FFFFFF")
p.add_thread(thread)

# Three heart-shaped leaves arranged around a central junction.
leaves = [
    heart_polygon(0, -6.2, 14.0, 0.0),
    heart_polygon(-6.0, 0.0, 14.0, -2*math.pi/3),
    heart_polygon(6.0, 0.0, 14.0, 2*math.pi/3),
]
for leaf in leaves:
    scanline_fill(p, leaf)

# Visible centered stem: repeated narrow running passes for TEST-001.
for offset in (-0.6, -0.2, 0.2, 0.6):
    p.move_abs(offset*MM, 3.0*MM)
    p.stitch_abs((offset+0.8)*MM, 8.0*MM)
    p.stitch_abs((offset+1.8)*MM, 13.0*MM)

p.end()
out = write_se600_pes(p, Path("output") / "SHAMROCK.PES", version=1)
print(f"Wrote {out}")
