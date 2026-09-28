import re

filepath = r"c:\Users\moxes\OneDrive\Desktop\Subsidy Mitra\contact-us.html"
with open(filepath, 'r', encoding='utf-8') as f:
    content = f.read()

# 1. Change "Our Office:" to "Corporate Office:"
content = content.replace('Our Office:</strong>', 'Corporate Office:</strong>')

# 2. Prepare the new Branch Office block
old_block = """<li style="margin-bottom: 25px; display: flex; align-items: flex-start;">
                              <div style="color: #1A4137; font-size: 24px; margin-right: 20px; min-width: 30px; text-align: center;">
                                  <i class="fa-solid fa-location-dot"></i>
                              </div>
                              <div>
                                  <strong style="font-size: 18px; color: #222;">Corporate Office:</strong><br>
                                  <address style="color: #555; line-height: 1.6; display: inline-block; margin-top: 5px; font-style: normal;">120 Feet Ring Rd, Behind Nabard,<br>Shanti Nagar, Usmanpura,<br>Ahmedabad, Gujarat</address>
                              </div>
                          </li>"""

new_branch_block = """<li style="margin-bottom: 25px; display: flex; align-items: flex-start;">
                              <div style="color: #1A4137; font-size: 24px; margin-right: 20px; min-width: 30px; text-align: center;">
                                  <i class="fa-solid fa-building"></i>
                              </div>
                              <div>
                                  <strong style="font-size: 18px; color: #222;">Branch Office:</strong><br>
                                  <address style="color: #555; line-height: 1.6; display: inline-block; margin-top: 5px; font-style: normal;">1, Patel Nagar, 80 Feet Road,<br>Rajkot, Gujarat</address>
                              </div>
                          </li>"""

# Replace old_block with old_block + new_branch_block
if old_block in content:
    content = content.replace(old_block, old_block + '\n                          ' + new_branch_block)
else:
    print("Could not find the exact old_block to append the branch office.")
    # Fallback to regex
    pattern = r'(<strong[^>]*>Corporate Office:</strong><br>\s*<address[^>]*>.*?</address>\s*</div>\s*</li>)'
    match = re.search(pattern, content, re.DOTALL)
    if match:
        full_match = match.group(1)
        print("Used regex to find the block.")
        branch_html = """
                          <li style="margin-bottom: 25px; display: flex; align-items: flex-start;">
                              <div style="color: #1A4137; font-size: 24px; margin-right: 20px; min-width: 30px; text-align: center;">
                                  <i class="fa-solid fa-location-dot"></i>
                              </div>
                              <div>
                                  <strong style="font-size: 18px; color: #222;">Branch Office:</strong><br>
                                  <address style="color: #555; line-height: 1.6; display: inline-block; margin-top: 5px; font-style: normal;">1, Patel Nagar, 80 Feet Road,<br>Rajkot, Gujarat</address>
                              </div>
                          </li>"""
        content = content.replace(full_match, full_match + branch_html)
    else:
        print("Regex also failed.")

with open(filepath, 'w', encoding='utf-8') as f:
    f.write(content)
print("Updated contact-us.html with Branch Office.")
