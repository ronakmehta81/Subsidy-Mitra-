import re

filepath = r"c:\Users\moxes\OneDrive\Desktop\Subsidy Mitra\index.html"
with open(filepath, 'r', encoding='utf-8') as f:
    content = f.read()

# Replace align-items in hex-item
content = re.sub(
    r'display: flex;\s*align-items: center;\s*justify-content: center;',
    r'display: flex;\n  align-items: flex-end;\n  justify-content: center;',
    content
)

# Replace hex-overlay
content = re.sub(
    r'\.hex-overlay \{\s*position: absolute;\s*top: 0; left: 0; width: 100%; height: 100%;\s*background: rgba\(0, 7, 31, 0\.65\); /\* Brand navy blue tint \*/\s*z-index: 2;\s*transition: background 0\.3s ease;\s*\}',
    r'.hex-overlay {\n  position: absolute;\n  top: 0; left: 0; width: 100%; height: 100%;\n  background: linear-gradient(to bottom, rgba(255,255,255,0.1) 40%, rgba(255,255,255,0.85) 100%);\n  z-index: 2;\n  transition: opacity 0.3s ease;\n}',
    content
)

# Replace hover overlay
content = re.sub(
    r'\.hex-item:hover \.hex-overlay \{\s*background: rgba\(0, 7, 31, 0\.3\); /\* Lightens on hover \*/\s*\}',
    r'.hex-item:hover .hex-overlay {\n  background: linear-gradient(to bottom, rgba(255,255,255,0) 20%, rgba(255,255,255,0.95) 100%);\n}',
    content
)

# Replace hex-text
content = re.sub(
    r'\.hex-text \{\s*position: relative;\s*z-index: 3;\s*color: #fff;\s*font-weight: 700;\s*font-size: clamp\(10px, 1\.2vw, 16px\);\s*text-align: center;\s*text-transform: uppercase;\s*letter-spacing: 1px;\s*padding: 0 10px;\s*line-height: 1\.2;\s*\}',
    r'.hex-text {\n  position: relative;\n  z-index: 3;\n  color: #0b1c3c;\n  font-weight: 800;\n  font-size: clamp(11px, 1.2vw, 16px);\n  text-align: center;\n  text-transform: uppercase;\n  letter-spacing: 1px;\n  padding: 0 5px;\n  margin-bottom: 22%;\n  line-height: 1.2;\n}',
    content
)

with open(filepath, 'w', encoding='utf-8') as f:
    f.write(content)
print("Updated CSS to light white fade and bottom text.")
