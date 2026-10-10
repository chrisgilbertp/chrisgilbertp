"""Locate the marker centres in Figure 5 (figure5.png) and convert them to axis units.

Usage:
    python3 digitise_figure5.py figure5.png

Needs numpy and Pillow. The script finds the axis frame and the tick marks,
fits a linear pixel-to-value map for each axis, and prints the centre of each
blue marker. Both series are drawn in the same blue, so circles (energy) and
squares (accuracy) must be told apart by shape. Markers that overlap (epsilon
0.01, 0.02 and 0.20) merge into a single blob; README.md explains how those
three points were resolved.
"""
import sys

import numpy as np
from PIL import Image


def load(path):
    return np.asarray(Image.open(path).convert("RGB")).astype(np.int32)


def groups(idx):
    """Centres of runs of consecutive integers."""
    idx = np.asarray(idx)
    if idx.size == 0:
        return []
    parts = np.split(idx, np.where(np.diff(idx) > 1)[0] + 1)
    return [float(p.mean()) for p in parts]


def fit(values, pixels):
    """Least-squares line pixel = a * value + b. Returns a, b and the largest residual in pixels."""
    values = np.asarray(values, dtype=float)
    pixels = np.asarray(pixels, dtype=float)
    A = np.vstack([values, np.ones_like(values)]).T
    (a, b), *_ = np.linalg.lstsq(A, pixels, rcond=None)
    return a, b, float(np.abs(pixels - (a * values + b)).max())


def shift(a, dy, dx):
    H, W = a.shape
    out = np.zeros_like(a)
    ys = slice(max(0, dy), H + min(0, dy))
    xs = slice(max(0, dx), W + min(0, dx))
    yd = slice(max(0, -dy), H + min(0, -dy))
    xd = slice(max(0, -dx), W + min(0, -dx))
    out[yd, xd] = a[ys, xs]
    return out


def erode(m, r):
    out = m.copy()
    for dy in range(-r, r + 1):
        for dx in range(-r, r + 1):
            out &= shift(m, dy, dx)
    return out


def dilate(m, r):
    out = np.zeros_like(m)
    for dy in range(-r, r + 1):
        for dx in range(-r, r + 1):
            out |= shift(m, dy, dx)
    return out


def components(m):
    H, W = m.shape
    seen = np.zeros(m.shape, dtype=bool)
    comps = []
    for y0, x0 in zip(*np.nonzero(m)):
        if seen[y0, x0]:
            continue
        seen[y0, x0] = True
        stack, pts = [(int(y0), int(x0))], []
        while stack:
            y, x = stack.pop()
            pts.append((y, x))
            for dy in (-1, 0, 1):
                for dx in (-1, 0, 1):
                    yy, xx = y + dy, x + dx
                    if 0 <= yy < H and 0 <= xx < W and m[yy, xx] and not seen[yy, xx]:
                        seen[yy, xx] = True
                        stack.append((yy, xx))
        comps.append(np.array(pts))
    return comps


def main(path):
    im = load(path)
    dark = im.sum(axis=2) < 200
    H, W = dark.shape
    cols = groups(np.where(dark.sum(axis=0) > 0.5 * H)[0])
    rows = groups(np.where(dark.sum(axis=1) > 0.5 * W)[0])
    L, R, T, B = cols[0], cols[-1], rows[0], rows[-1]

    # Tick marks sit just outside each spine.
    left = groups(np.where(dark[:, round(L) - 9:round(L) - 1].sum(axis=1) >= 6)[0])
    right = groups(np.where(dark[:, round(R) + 2:round(R) + 10].sum(axis=1) >= 6)[0])
    bottom = groups(np.where(dark[round(B) + 2:round(B) + 10, :].sum(axis=0) >= 6)[0])
    assert (len(left), len(right), len(bottom)) == (6, 7, 8), "tick detection failed"

    # Pixel rows increase downwards, so the tick lists run top to bottom on the
    # two vertical axes and left to right on the horizontal axis.
    aL, bL, eL = fit([110, 100, 90, 80, 70, 60], left)
    aR, bR, eR = fit([98, 96, 94, 92, 90, 88, 86], right)
    aX, bX, eX = fit([0.025, 0.05, 0.075, 0.10, 0.125, 0.15, 0.175, 0.20], bottom)
    print("largest tick residual in pixels: left %.2f, right %.2f, horizontal %.2f" % (eL, eR, eX))

    blue = (np.abs(im[:, :, 0] - 31) + np.abs(im[:, :, 1] - 119) + np.abs(im[:, :, 2] - 180)) < 90
    inside = np.zeros(blue.shape, dtype=bool)
    inside[round(T) + 3:round(B) - 2, round(L) + 3:round(R) - 2] = True
    inside[400:510, 1100:1500] = False  # legend box
    # A 7 x 7 opening removes the lines (about 4 px wide) and keeps the markers.
    blobs = components(dilate(erode(blue & inside, 3), 3))
    print("marker blobs found:", len(blobs))
    for pts in sorted(blobs, key=lambda p: p[:, 1].mean()):
        y0, y1 = pts[:, 0].min(), pts[:, 0].max()
        x0, x1 = pts[:, 1].min(), pts[:, 1].max()
        cx, cy = (x0 + x1) / 2.0, (y0 + y1) / 2.0
        print("x %6.1f  y %6.1f  size %2dx%2d  epsilon %.4f  energy %6.2f  accuracy %6.2f" % (
            cx, cy, x1 - x0 + 1, y1 - y0 + 1, (cx - bX) / aX, (cy - bL) / aL, (cy - bR) / aR))


if __name__ == "__main__":
    main(sys.argv[1] if len(sys.argv) > 1 else "figure5.png")
