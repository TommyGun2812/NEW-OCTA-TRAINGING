import os, shutil, random
from pathlib import Path

random.seed(42)
src_root = Path("dataset_all")
dst_root = Path("dataset")
splits = ["train", "val", "test"]

# Crear carpetas
for split in splits:
    (dst_root / split).mkdir(parents=True, exist_ok=True)

for cls in os.listdir(src_root):
    cls_path = src_root / cls
    if not cls_path.is_dir():
        continue
    imgs = [x for x in cls_path.iterdir() if x.suffix.lower() in [".jpg", ".jpeg", ".png"]]
    random.shuffle(imgs)

    n = len(imgs)
    n_train = int(0.8 * n)
    n_val = int(0.1 * n)

    splits_imgs = {
        "train": imgs[:n_train],
        "val": imgs[n_train:n_train + n_val],
        "test": imgs[n_train + n_val:],
    }

    for split, files in splits_imgs.items():
        dst_cls = dst_root / split / cls
        dst_cls.mkdir(parents=True, exist_ok=True)
        for f in files:
            shutil.copy(f, dst_cls / f.name)

print("Split completo. Estructura creada en 'dataset/train', 'dataset/val', 'dataset/test'")
