import re

filepath = r"c:\Users\moxes\OneDrive\Desktop\Subsidy Mitra\index.html"
with open(filepath, 'r', encoding='utf-8', errors='ignore') as f:
    content = f.read()

# Replace any broken rupee with the HTML entity
content = re.sub(
    r'<span class="count">[^<]*1000</span>Cr',
    r'<span class="count">&#8377; 1000</span>Cr',
    content
)

# Also check for other occurrences of 1000Cr just in case
content = re.sub(
    r'<span class="count">[^<]*1000Cr</span>',
    r'<span class="count">&#8377; 1000</span>Cr',
    content
)

with open(filepath, 'w', encoding='utf-8') as f:
    f.write(content)
print("Replaced with HTML entity.")
