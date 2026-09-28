import struct
import os

def get_webp_dimensions(filepath):
    with open(filepath, 'rb') as f:
        data = f.read(30)
        if data[0:4] == b'RIFF' and data[8:12] == b'WEBP':
            if data[12:16] == b'VP8 ':
                width, height = struct.unpack('<HH', data[26:30])
                return width & 0x3fff, height & 0x3fff
            elif data[12:16] == b'VP8L':
                b = data[21:25]
                width = 1 + (((b[1] & 0x3F) << 8) | b[0])
                height = 1 + (((b[3] & 0xF) << 16) | (b[2] << 8) | ((b[1] & 0xC0) >> 6))
                return width, height
            elif data[12:16] == b'VP8X':
                width = 1 + struct.unpack('<I', data[24:27] + b'\x00')[0]
                height = 1 + struct.unpack('<I', data[27:30] + b'\x00')[0]
                return width, height
    return None, None

base_dir = r"c:\Users\moxes\OneDrive\Desktop\Subsidy Mitra\images\banner"
images = ["subsidy-mitra-slider-1.webp", "subsidy-mitra-slider-2.webp", "subsidy-mitra-slider-3.webp"]

for img in images:
    path = os.path.join(base_dir, img)
    if os.path.exists(path):
        w, h = get_webp_dimensions(path)
        print(f"{img}: {w} x {h}")
