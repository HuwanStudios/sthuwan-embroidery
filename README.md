# StHuwan Embroidery Engine

Machine-aware embroidery tooling with the **Brother SE600** as the first physically validated target.

## Priority
1. Generate genuine PES through the upstream pyembroidery encoder.
2. Validate designs against the SE600 100 x 100 mm (4 x 4 in) field.
3. Physically test every compatibility milestone on the actual machine.
4. Build digitizing tools (fill, satin, running stitch, underlay) above the encoder.

## TEST-001
Classic Fill Shamrock — three heart-shaped leaves, visible centered stem, one thread color.

This repository does **not** treat renaming an image to .pes as embroidery conversion.

## Upstream
PES encoding uses the MIT-licensed pyembroidery project. Install dependencies with:

```bash
python -m pip install -r requirements.txt
```

Then:

```bash
python examples/shamrock_test001.py
```

Output: `output/SHAMROCK.PES`

Physical Brother SE600 recognition and sew-out remain the acceptance test.
