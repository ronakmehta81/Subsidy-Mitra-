import re

filepath = r"c:\Users\moxes\OneDrive\Desktop\Subsidy Mitra\index.html"
with open(filepath, 'r', encoding='utf-8') as f:
    content = f.read()

# 1. Update the CSS block
old_css = """<style>
.about-image-cluster {
  position: relative;
  width: 100%;
  padding-bottom: 100%; /* 1:1 Aspect Ratio */
  margin: 0 auto;
}
.about-image-cluster img {
  position: absolute;
  object-fit: cover;
  transition: transform 0.3s ease;
}
.about-image-cluster img:hover {
  transform: scale(1.05);
  z-index: 20;
}
.hex-shape {
  clip-path: polygon(50% 0%, 100% 25%, 100% 75%, 50% 100%, 0% 75%, 0% 25%);
  width: 45%;
  height: 45%;
}
.circle-shape {
  border-radius: 50%;
  width: 55%;
  height: 55%;
  top: 22.5%;
  left: 22.5%;
  z-index: 10;
  border: 5px solid #fff;
  box-shadow: 0 10px 30px rgba(0,0,0,0.15);
}
.pos-tl { top: 0; left: 0; }
.pos-tr { top: 0; right: 0; }
.pos-bl { bottom: 0; left: 0; }
.pos-br { bottom: 0; right: 0; }
</style>"""

new_css = """<style>
.about-image-cluster {
  position: relative;
  width: 100%;
  padding-bottom: 100%; /* 1:1 Aspect Ratio */
  margin: 0 auto;
}
.about-image-cluster img.circle-shape {
  position: absolute;
  object-fit: cover;
  transition: transform 0.3s ease;
}
.about-image-cluster img.circle-shape:hover {
  transform: scale(1.05);
  z-index: 20;
}
.hex-item {
  position: absolute;
  width: 45%;
  height: 45%;
  clip-path: polygon(50% 0%, 100% 25%, 100% 75%, 50% 100%, 0% 75%, 0% 25%);
  transition: transform 0.3s ease;
  overflow: hidden;
  display: flex;
  align-items: center;
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
  background: rgba(0, 7, 31, 0.65); /* Brand navy blue tint */
  z-index: 2;
  transition: background 0.3s ease;
}
.hex-item:hover .hex-overlay {
  background: rgba(0, 7, 31, 0.3); /* Lightens on hover */
}
.hex-text {
  position: relative;
  z-index: 3;
  color: #fff;
  font-weight: 700;
  font-size: clamp(10px, 1.2vw, 16px);
  text-align: center;
  text-transform: uppercase;
  letter-spacing: 1px;
  padding: 0 10px;
  line-height: 1.2;
}
.circle-shape {
  border-radius: 50%;
  width: 55%;
  height: 55%;
  top: 22.5%;
  left: 22.5%;
  z-index: 10;
  border: 5px solid #fff;
  box-shadow: 0 10px 30px rgba(0,0,0,0.15);
}
.pos-tl { top: 0; left: 0; }
.pos-tr { top: 0; right: 0; }
.pos-bl { bottom: 0; left: 0; }
.pos-br { bottom: 0; right: 0; }
</style>"""

content = content.replace(old_css, new_css)

# 2. Update the HTML block
old_html = """<div class="about-image-cluster">
    <img loading="lazy" class="hex-shape pos-tl" src="images/about/subsidy-mitra-about-1.webp?v=5" alt="Partner 1" style="object-position: center 10%;">
    <img loading="lazy" class="hex-shape pos-tr" src="images/about/subsidy-mitra-about-5.webp?v=5" alt="Meeting" style="object-position: center center;">
    <img loading="lazy" class="hex-shape pos-bl" src="images/about/subsidy-mitra-about-4.webp?v=5" alt="Consulting" style="object-position: center center;">
    <img loading="lazy" class="hex-shape pos-br" src="images/about/subsidy-mitra-about-2.webp?v=5" alt="Partner 2" style="object-position: center 10%;">
    <img loading="lazy" class="circle-shape" src="images/about/subsidy-mitra-about-3.webp?v=5" alt="Partners" style="object-position: center center;">
  </div>"""

new_html = """<div class="about-image-cluster">
    <!-- Manufacturing -->
    <div class="hex-item pos-tl">
      <div class="hex-bg" style="background-image: url('images/about/subsidy-mitra-about-1.webp?v=5');"></div>
      <div class="hex-overlay"></div>
      <span class="hex-text">Manufacturing</span>
    </div>
    <!-- Hospitals -->
    <div class="hex-item pos-tr">
      <div class="hex-bg" style="background-image: url('images/about/subsidy-mitra-about-5.webp?v=5');"></div>
      <div class="hex-overlay"></div>
      <span class="hex-text">Hospitals</span>
    </div>
    <!-- IT Sector -->
    <div class="hex-item pos-bl">
      <div class="hex-bg" style="background-image: url('images/about/subsidy-mitra-about-4.webp?v=5');"></div>
      <div class="hex-overlay"></div>
      <span class="hex-text">IT Sector</span>
    </div>
    <!-- Hotel and Resort -->
    <div class="hex-item pos-br">
      <div class="hex-bg" style="background-image: url('images/about/subsidy-mitra-about-2.webp?v=5');"></div>
      <div class="hex-overlay"></div>
      <span class="hex-text">Hotel &<br>Resort</span>
    </div>
    
    <img loading="lazy" class="circle-shape" src="images/about/subsidy-mitra-about-3.webp?v=5" alt="Our Team" style="object-position: center center;">
  </div>"""

content = content.replace(old_html, new_html)

with open(filepath, 'w', encoding='utf-8') as f:
    f.write(content)
print("Updated HTML and CSS for hex texts.")
