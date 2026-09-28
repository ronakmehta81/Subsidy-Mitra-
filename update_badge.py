import re

filepath = r"c:\Users\moxes\OneDrive\Desktop\Subsidy Mitra\index.html"
with open(filepath, 'r', encoding='utf-8') as f:
    content = f.read()

# 1. Update CSS for hex-overlay and hex-text
old_css_part = """.hex-overlay {
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

new_css_part = """.hex-overlay {
  position: absolute;
  top: 0; left: 0; width: 100%; height: 100%;
  background: rgba(0,0,0,0.1);
  z-index: 2;
  transition: background 0.3s ease;
}
.hex-item:hover .hex-overlay {
  background: rgba(0,0,0,0.3);
}

.hex-text {
  position: relative;
  z-index: 3;
  color: #ffffff;
  background-color: #0b1c3c;
  border: 1px solid rgba(255,255,255,0.2);
  font-weight: 700;
  font-size: clamp(9px, 1vw, 13px);
  text-align: center;
  text-transform: uppercase;
  letter-spacing: 1.5px;
  padding: 8px 18px;
  border-radius: 30px;
  box-shadow: 0 5px 15px rgba(0,0,0,0.3);
  line-height: 1.2;
  backdrop-filter: blur(4px);
}
.hex-item.text-bottom .hex-text { margin-bottom: 22%; }
.hex-item.text-top .hex-text { margin-top: 22%; }"""

if old_css_part in content:
    content = content.replace(old_css_part, new_css_part)
else:
    print("WARNING: Could not find exact CSS block.")

with open(filepath, 'w', encoding='utf-8') as f:
    f.write(content)
print("Updated CSS to use badge style for text.")
