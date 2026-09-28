from PIL import Image
import os

source_dir = r"C:\Users\moxes\.gemini\antigravity\brain\906e8e26-c7dd-465a-a074-8efc114f28a6"
target_dir = r"c:\Users\moxes\OneDrive\Desktop\Subsidy Mitra\images\about"

mapping = {
    "manufacturing_sector_1790576056239.jpg": "subsidy-mitra-about-1.webp",
    "hospital_sector_1790576067105.jpg": "subsidy-mitra-about-5.webp",
    "it_sector_1790576156336.jpg": "subsidy-mitra-about-4.webp",
    "hotel_resort_1790576171093.jpg": "subsidy-mitra-about-2.webp"
}

for src, dst in mapping.items():
    src_path = os.path.join(source_dir, src)
    dst_path = os.path.join(target_dir, dst)
    if os.path.exists(src_path):
        with Image.open(src_path) as img:
            img.save(dst_path, 'webp', quality=85)
            print(f"Converted and saved {dst}")
    else:
        print(f"File not found: {src_path}")
