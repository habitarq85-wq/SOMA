import os
from PIL import Image

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
RECURSOS_DIR = os.path.join(BASE_DIR, "recursos_graficos")
MAX_W = 1920
QUALITY = 82

total_original = 0
total_new = 0
count = 0

for root, dirs, files in os.walk(RECURSOS_DIR):
    for f in files:
        if not f.lower().endswith(".png"):
            continue
        path = os.path.join(root, f)
        try:
            img = Image.open(path)
            w, h = img.size
            if w > MAX_W:
                ratio = MAX_W / w
                img = img.resize((MAX_W, int(h * ratio)), Image.LANCZOS)
            original = os.path.getsize(path)
            if img.mode in ("RGBA", "P"):
                img = img.convert("RGB")
            new_path = os.path.splitext(path)[0] + ".jpg"
            img.save(new_path, "JPEG", quality=QUALITY, optimize=True)
            new_size = os.path.getsize(new_path)
            total_original += original
            total_new += new_size
            count += 1
            print(f"  {f}: {original//1024}KB -> {new_size//1024}KB ({new_size*100//original}%)")
        except Exception as e:
            print(f"  ERROR {f}: {e}")

print(f"\n--- {count} imagenes optimizadas ---")
print(f"Original:  {total_original//1024//1024} MB")
print(f"Optimizado: {total_new//1024//1024} MB")
print(f"Ahorro:    {(total_original-total_new)//1024//1024} MB")
