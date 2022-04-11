from pathlib import Path
from PIL import Image

# img_folder = "flash"

orig = Path(f"C:\\Users\\Declan\\Desktop\\Website_Trials\\ankutattoo\\assets\\img")
# orig = Path(f"C:\\Users\\Declan\\Desktop\\Website_Trials\\new_website_photos_2022\\img\\anku")
# thumbs = Path(f"C:\\Users\\Declan\\Desktop\\Website_Trials\\ankutattoo\\assets\\img\\{img_folder}_thumbs")
# root = Path(f"C:\\Users\\Declan\\Desktop\\Website_Trials\\ankutattoo")
# thumbs_sqr = Path(f"C:\\Users\\Declan\\Desktop\\Website_Trials\\ankutattoo\\assets\\img\\{img_folder}_thumbs_sqr")


orig_walk = orig.glob('**/*')
files = [x for x in orig_walk if x.is_file()]
files = [x for x in files if x.suffix.lower() in ['.jpg', '.jpeg']]

base = 3000
for file in files:
    img = Image.open(file)
    w = float(img.size[0])
    h = float(img.size[1])
    print(w, h)
    if w > base or h > base:
        if w >= h:
            hpercent = (base / w)
            hsize = int((h * float(hpercent)))
            img = img.resize((base, hsize), Image.ANTIALIAS)
        elif h > w:
            wpercent = (base / h)
            wsize = int((w * float(wpercent)))
            img = img.resize((wsize, base), Image.ANTIALIAS)
    img.save(file)

