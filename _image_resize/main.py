from pathlib import Path
from PIL import Image

orig = Path(r"C:\Users\Declan\Desktop\Website_Trials\ankutattoo\assets\img\gallery")
thumbs = Path(r"C:\Users\Declan\Desktop\Website_Trials\ankutattoo\assets\img\gallery_thumbs")
root = Path(r"C:\Users\Declan\Desktop\Website_Trials\ankutattoo")

orig_walk = orig.glob('**/*')
files = [x for x in orig_walk if x.is_file()]
files = [x for x in files if x.suffix == '.jpg']

basewidth = 300
for file in files:
    img = Image.open(file)
    wpercent = (basewidth / float(img.size[0]))
    hsize = int((float(img.size[1]) * float(wpercent)))
    img = img.resize((basewidth, hsize), Image.ANTIALIAS)
    rel_path = file.relative_to(orig)
    thumb_file = thumbs.joinpath(rel_path)
    thumb_file.parent.mkdir(parents=True, exist_ok=True)
    img.save(thumb_file)

    rel_path_root = file.relative_to(root)
    rel_thumb_root = thumb_file.relative_to(root)
    print(f"  - image_path: /{rel_path_root.as_posix()}\n"
          f"    thumb_path: /{rel_thumb_root.as_posix()}\n"
          f"    name: {file.stem}")









