import re

filepath = r"c:\Users\moxes\OneDrive\Desktop\Subsidy Mitra\index.html"
with open(filepath, 'r', encoding='utf-8') as f:
    content = f.read()

old_img = r'<img loading="lazy" class="circle-shape" src="images/about/subsidy-mitra-about-3.webp\?v=5" alt="Our Team" style="object-position: center center;">'
new_img = r'<img loading="lazy" class="circle-shape" src="images/subsidy-mitra-logo.jpg" alt="Subsidy Mitra Logo" style="object-fit: contain !important; background: #ffffff; padding: 15px; object-position: center;">'

content = re.sub(old_img, new_img, content)

with open(filepath, 'w', encoding='utf-8') as f:
    f.write(content)
print("Replaced center image with logo.")
