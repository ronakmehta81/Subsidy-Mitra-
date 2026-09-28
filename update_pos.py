import re

filepath = r"c:\Users\moxes\OneDrive\Desktop\Subsidy Mitra\index.html"
with open(filepath, 'r', encoding='utf-8') as f:
    content = f.read()

# 1. Update HTML classes
content = content.replace('<div class="hex-item pos-tl">', '<div class="hex-item pos-tl text-top">')
content = content.replace('<div class="hex-item pos-tr">', '<div class="hex-item pos-tr text-top">')
content = content.replace('<div class="hex-item pos-bl">', '<div class="hex-item pos-bl text-bottom">')
content = content.replace('<div class="hex-item pos-br">', '<div class="hex-item pos-br text-bottom">')

# 2. Update CSS
old_css_part1 = """.hex-item {
  position: absolute;
  width: 45%;
  height: 45%;
  clip-path: polygon(50% 0%, 100% 25%, 100% 75%, 50% 100%, 0% 75%, 0% 25%);
  transition: transform 0.3s ease;
  overflow: hidden;
  display: flex;
  align-items: flex-end;
  justify-content: center;
}
.hex-item:hover {
  transform: scale(1.05);
  z-index: 20;
}
.hex-bg {
  position: absolute;
  top: 0; left: 0; width: 100%; height: 100%;
  background-size: cover;
  background-position: center;
  z-index: 1;
}
.hex-overlay {
  position: absolute;
  top: 0; left: 0; width: 100%; height: 100%;
  background: linear-gradient(to bottom, rgba(255,255,255,0.1) 40%, rgba(255,255,255,0.85) 100%);
  z-index: 2;
  transition: opacity 0.3s ease;
}
.hex-item:hover .hex-overlay {
  background: linear-gradient(to bottom, rgba(255,255,255,0) 20%, rgba(255,255,255,0.95) 100%);
}
.hex-text {
  position: relative;
  z-index: 3;
  color: #0b1c3c;
  font-weight: 800;
  font-size: clamp(11px, 1.2vw, 16px);
  text-align: center;
  text-transform: uppercase;
  letter-spacing: 1px;
  padding: 0 5px;
  margin-bottom: 22%;
  line-height: 1.2;
}"""

new_css_part1 = """.hex-item {
  position: absolute;
  width: 45%;
  height: 45%;
  clip-path: polygon(50% 0%, 100% 25%, 100% 75%, 50% 100%, 0% 75%, 0% 25%);
  transition: transform 0.3s ease;
  overflow: hidden;
  display: flex;
  justify-content: center;
}
.hex-item.text-top { align-items: flex-start; }
.hex-item.text-bottom { align-items: flex-end; }

.hex-item:hover {
  transform: scale(1.05);
  z-index: 20;
}
.hex-bg {
  position: absolute;
  top: 0; left: 0; width: 100%; height: 100%;
  background-size: cover;
  background-position: center;
  z-index: 1;
}
.hex-overlay {
  position: absolute;
  top: 0; left: 0; width: 100%; height: 100%;
  z-index: 2;
  transition: opacity 0.3s ease;
}

/* Bottom Text Overlay Fade */
.hex-item.text-bottom .hex-overlay {
  background: linear-gradient(to bottom, rgba(255,255,255,0.0) 40%, rgba(255,255,255,0.85) 100%);
}
.hex-item.text-bottom:hover .hex-overlay {
  background: linear-gradient(to bottom, rgba(255,255,255,0.0) 20%, rgba(255,255,255,0.95) 100%);
}

/* Top Text Overlay Fade */
.hex-item.text-top .hex-overlay {
  background: linear-gradient(to top, rgba(255,255,255,0.0) 40%, rgba(255,255,255,0.85) 100%);
}
.hex-item.text-top:hover .hex-overlay {
  background: linear-gradient(to top, rgba(255,255,255,0.0) 20%, rgba(255,255,255,0.95) 100%);
}

.hex-text {
  position: relative;
  z-index: 3;
  color: #0b1c3c;
  font-weight: 800;
  font-size: clamp(11px, 1.2vw, 16px);
  text-align: center;
  text-transform: uppercase;
  letter-spacing: 1px;
  padding: 0 5px;
  line-height: 1.2;
}
.hex-item.text-bottom .hex-text { margin-bottom: 22%; }
.hex-item.text-top .hex-text { margin-top: 22%; }"""

if old_css_part1 in content:
    content = content.replace(old_css_part1, new_css_part1)
else:
    print("WARNING: Could not find exact CSS block.")

with open(filepath, 'w', encoding='utf-8') as f:
    f.write(content)
print("Updated CSS and HTML for top and bottom text positioning.")
