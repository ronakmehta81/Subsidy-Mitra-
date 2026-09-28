from PIL import Image
filepath = r"c:\Users\moxes\OneDrive\Desktop\Subsidy Mitra\images\subsidy-mitra-logo.jpg"
try:
    with Image.open(filepath) as img:
        print(f"Logo size: {img.size}")
except Exception as e:
    print(f"Error: {e}")
