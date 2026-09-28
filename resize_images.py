try:
    from PIL import Image
    import os

    base_dir = r"c:\Users\moxes\OneDrive\Desktop\Subsidy Mitra\images\banner"
    images = ["subsidy-mitra-slider-2.webp", "subsidy-mitra-slider-3.webp"]
    target_size = (2070, 1380)

    for img_name in images:
        path = os.path.join(base_dir, img_name)
        if os.path.exists(path):
            old_size = os.path.getsize(path) / (1024 * 1024)
            with Image.open(path) as img:
                # Resize using high-quality resampling
                resized_img = img.resize(target_size, Image.Resampling.LANCZOS)
                # Save it back, overwriting the massive file, with good WebP compression
                resized_img.save(path, 'webp', quality=80)
            
            new_size = os.path.getsize(path) / 1024
            print(f"Resized {img_name}: {old_size:.2f} MB -> {new_size:.2f} KB")
except ImportError:
    import subprocess
    import sys
    print("Installing Pillow...")
    subprocess.check_call([sys.executable, "-m", "pip", "install", "Pillow"])
    print("Please re-run the script.")
