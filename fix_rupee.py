import re

filepath = r"c:\Users\moxes\OneDrive\Desktop\Subsidy Mitra\index.html"
with open(filepath, 'r', encoding='utf-8', errors='ignore') as f:
    content = f.read()

# Find the span count line
match = re.search(r'<span class="count">(.{1,10})1000Cr</span>', content)
if match:
    print("Found corrupted string:", repr(match.group(1)))
    content = content.replace(match.group(0), '<span class="count">₹1000</span>Cr')
    
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)
    print("Fixed corrupted string.")
else:
    print("Could not find the 1000Cr string.")
