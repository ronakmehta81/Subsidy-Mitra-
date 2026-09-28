import re

filepath = r"c:\Users\moxes\OneDrive\Desktop\Subsidy Mitra\index.html"
with open(filepath, 'r', encoding='utf-8', errors='ignore') as f:
    content = f.read()

# Fix dashes in the footer
content = re.sub(r'10:00 AM [^a-zA-Z0-9]+ 7:00 PM', '10:00 AM &ndash; 7:00 PM', content)
content = re.sub(r'Monday [^a-zA-Z0-9]+ Saturday', 'Monday &ndash; Saturday', content)

with open(filepath, 'w', encoding='utf-8') as f:
    f.write(content)
print("Fixed broken dashes in footer.")
