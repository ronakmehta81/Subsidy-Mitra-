import re

filepath = r"c:\Users\moxes\OneDrive\Desktop\Subsidy Mitra\index.html"
with open(filepath, 'r', encoding='utf-8') as f:
    content = f.read()

# Fix Slide 2 missing subtitle
content = re.sub(
    r'(<div class="inner-column">\s*)<h1 class="title" data-animation="fadeInUp" data-delay="\.5s">Complete',
    r'\1<h6 class="sub-title" data-animation="fadeInUp" data-delay=".3s">EXPERT MSME ADVISORY</h6>\n              <h1 class="title" data-animation="fadeInUp" data-delay=".5s">Complete',
    content
)

# Fix Slide 3 text lines
content = re.sub(
    r'<h1 class="title" data-animation="fadeInUp" data-delay="\.5s">Your Complete\s*<span>Subsidy Solution</span>\s*</h1>',
    r'<h1 class="title" data-animation="fadeInUp" data-delay=".5s">Gujarat\'s Most\n                          <span>Trusted MSME</span>\n                          Subsidy Consultants\n                        </h1>',
    content
)

with open(filepath, 'w', encoding='utf-8') as f:
    f.write(content)
print("Updated successfully via python.")
