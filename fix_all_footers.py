import os
import re

dir_path = r"c:\Users\moxes\OneDrive\Desktop\Subsidy Mitra"

for filename in os.listdir(dir_path):
    if filename.endswith(".html"):
        filepath = os.path.join(dir_path, filename)
        with open(filepath, 'r', encoding='utf-8', errors='ignore') as f:
            content = f.read()
        
        # Replace the broken characters between the times and days
        # E.g. "10:00 AM Â€“ 7:00 PM" -> "10:00 AM &ndash; 7:00 PM"
        
        # We can use a regex that captures "10:00 AM" and "7:00 PM" and replaces everything in between.
        new_content = re.sub(r'10:00 AM.*?7:00 PM', '10:00 AM &ndash; 7:00 PM', content)
        new_content = re.sub(r'Monday.*?Saturday', 'Monday &ndash; Saturday', new_content)
        
        if content != new_content:
            with open(filepath, 'w', encoding='utf-8') as f:
                f.write(new_content)
            print(f"Fixed footer encoding in {filename}")

print("Done scanning all HTML files.")
