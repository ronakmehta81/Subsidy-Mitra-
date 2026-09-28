import re

filepath = r"c:\Users\moxes\OneDrive\Desktop\Subsidy Mitra\index.html"
with open(filepath, 'r', encoding='utf-8') as f:
    content = f.read()

# Fix the whatsapp-float CSS block
old_css = """.whatsapp-float {
      position: fixed;
      width: 60px;
      height: 60px;
      bottom: 30px;
      right: 30px;
      background-color: #25D366;
      color: #fff;
      border-radius: 50px;
      text-align: center;
      font-size: 30px;
      box-shadow: 2px 2px 10px rgba(0,0,0,0.3);
      z-index: 9999;
      display: flex;
    align-items: flex-end;
    justify-content: center;
      text-decoration: none;
      transition: all 0.3s ease;
  }"""

new_css = """.whatsapp-float {
      position: fixed;
      width: 60px;
      height: 60px;
      bottom: 30px;
      right: 30px;
      background-color: #25D366;
      color: #fff;
      border-radius: 50px;
      text-align: center;
      font-size: 35px; /* slightly larger icon looks better */
      box-shadow: 2px 2px 10px rgba(0,0,0,0.3);
      z-index: 9999;
      display: flex;
      align-items: center;
      justify-content: center;
      text-decoration: none;
      transition: all 0.3s ease;
  }"""

if old_css in content:
    content = content.replace(old_css, new_css)
else:
    print("Could not find exact string. Attempting regex.")
    content = re.sub(
        r'(\.whatsapp-float\s*\{[^}]*display:\s*flex;)\s*align-items:\s*flex-end;',
        r'\1\n      align-items: center;',
        content
    )

with open(filepath, 'w', encoding='utf-8') as f:
    f.write(content)
print("Restored WhatsApp icon centering.")
