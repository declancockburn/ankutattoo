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



## Crop already existing thumbs height to 300px

orig = Path(r"C:\Users\Declan\Desktop\Website_Trials\ankutattoo\assets\img\gallery")
root = Path(r"C:\Users\Declan\Desktop\Website_Trials\ankutattoo")
thumbs = Path(r"C:\Users\Declan\Desktop\Website_Trials\ankutattoo\assets\img\gallery_thumbs")
thumbs_sqr = Path(r"C:\Users\Declan\Desktop\Website_Trials\ankutattoo\assets\img\gallery_thumbs_sqr")

thumbs_walk = thumbs.glob('**/*')

files = [x for x in thumbs_walk if x.is_file()]
files = [x for x in files if x.suffix == '.jpg']

for file in files:
# file = files[0]
    img = Image.open(file)
    w, h = img.size
    if h > 300:
        delta = h - 300
        top = delta // 2
        bottom = delta // 2
        if delta % 2 == 1:
            bottom += 1
        img_cropped = img.crop((0, top, w, h-bottom))
    else:
        img_cropped = img.crop((0, 0, w, h))
    rel_path = file.relative_to(thumbs)
    thumb_sqr_file = thumbs_sqr.joinpath(rel_path)
    thumb_sqr_file.parent.mkdir(parents=True, exist_ok=True)
    img_cropped.save(thumb_sqr_file)
    main_root = orig.joinpath(file.relative_to(thumbs))

    rel_main_root = main_root.relative_to(root)
    rel_thumb_root = thumb_sqr_file.relative_to(root)
    print(f"  - image_path: /{rel_main_root.as_posix()}\n"
          f"    thumb_path: /{rel_thumb_root.as_posix()}\n"
          f"    name: {file.stem}")









