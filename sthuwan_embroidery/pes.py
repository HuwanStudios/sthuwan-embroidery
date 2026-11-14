from pathlib import Path
from pyembroidery import write_pes
from .machines import BROTHER_SE600, validate_bounds

def pattern_size_mm(pattern):
    left, top, right, bottom = pattern.bounds()
    # pyembroidery coordinates are 0.1 mm units.
    return (right - left) / 10.0, (bottom - top) / 10.0

def write_se600_pes(pattern, path, version=1):
    width_mm, height_mm = pattern_size_mm(pattern)
    validate_bounds(width_mm, height_mm, BROTHER_SE600)
    path = Path(path)
    path.parent.mkdir(parents=True, exist_ok=True)
    # Upstream pyembroidery performs the actual PES/PEC binary encoding.
    write_pes(pattern, str(path), settings={"version": version})
    return path
