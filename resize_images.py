"""
Resize all images under the lipari/ folder to 1280px width.
Skips files matching title.* and map.* patterns.
Preserves aspect ratio. Overwrites originals.
"""

import os
import sys
from pathlib import Path
from PIL import Image

TARGET_WIDTH = 1280
SKIP_PREFIXES = ("title", "map")
IMAGE_EXTENSIONS = {".jpg", ".jpeg", ".png", ".gif", ".webp", ".bmp"}

def should_skip(filename: str) -> bool:
    stem = Path(filename).stem.lower()
    return stem in SKIP_PREFIXES

def resize_image(filepath: Path) -> str | None:
    try:
        with Image.open(filepath) as img:
            w, h = img.size
            if w <= TARGET_WIDTH:
                return f"  SKIP (already {w}x{h})"

            ratio = TARGET_WIDTH / w
            new_h = round(h * ratio)
            resized = img.resize((TARGET_WIDTH, new_h), Image.LANCZOS)

            # Preserve EXIF for JPEG
            exif = img.info.get("exif")
            save_kwargs = {}
            if filepath.suffix.lower() in (".jpg", ".jpeg"):
                save_kwargs["quality"] = 85
                if exif:
                    save_kwargs["exif"] = exif
            elif filepath.suffix.lower() == ".png":
                save_kwargs["optimize"] = True

            resized.save(filepath, **save_kwargs)
            return f"  {w}x{h} -> {TARGET_WIDTH}x{new_h}"
    except Exception as e:
        return f"  ERROR: {e}"

def main():
    root = Path(__file__).parent
    processed = 0
    resized = 0
    skipped_name = 0
    skipped_small = 0
    errors = 0

    print(f"Scanning: {root}")
    print(f"Target width: {TARGET_WIDTH}px")
    print(f"Skipping: {', '.join(p + '.*' for p in SKIP_PREFIXES)}")
    print("-" * 60)

    for dirpath, _, filenames in os.walk(root):
        for fname in sorted(filenames):
            fpath = Path(dirpath) / fname

            if fpath.suffix.lower() not in IMAGE_EXTENSIONS:
                continue

            rel = fpath.relative_to(root)

            if should_skip(fname):
                print(f"  SKIP (excluded name): {rel}")
                skipped_name += 1
                continue

            processed += 1
            result = resize_image(fpath)
            print(f"  {result}: {rel}")

            if result and result.startswith("  SKIP"):
                skipped_small += 1
            elif result and result.startswith("  ERROR"):
                errors += 1
            else:
                resized += 1

    print("-" * 60)
    print(f"Total images found : {processed + skipped_name}")
    print(f"Excluded (title/map): {skipped_name}")
    print(f"Already ≤ {TARGET_WIDTH}px  : {skipped_small}")
    print(f"Resized            : {resized}")
    print(f"Errors             : {errors}")

if __name__ == "__main__":
    main()
