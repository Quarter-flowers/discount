import qrcode
from PIL import Image, ImageDraw, ImageFont

# Config
urls = {
    "magnolia": ("https://quarter-flowers.github.io/discount/magnolia.html", "magnolia.html"),
    "daisy": ("https://quarter-flowers.github.io/discount/daisy.html", "daisy.html"),
    "window": ("https://quarter-flowers.github.io/discount/window.html", "window.html")
}

# Mac Font
try:
    font = ImageFont.truetype("/System/Library/Fonts/Helvetica.ttc", 20) # Keeping 20, visible but small relative to QR
except:
    font = ImageFont.load_default()

for name, (url, label) in urls.items():
    # Generate QR
    qr = qrcode.QRCode(box_size=10, border=4)
    qr.add_data(url)
    qr.make(fit=True)
    qr_img = qr.make_image(fill_color="black", back_color="white").convert('RGB')

    # Create Background (QR + Text space)
    width, height = qr_img.size
    new_height = height + 40 # Reduced space
    new_img = Image.new('RGB', (width, new_height), 'white')
    
    # Paste QR
    new_img.paste(qr_img, (0, 0))
    
    # Draw Text
    draw = ImageDraw.Draw(new_img)
    
    # Calculate text width
    try:
        text_bbox = draw.textbbox((0, 0), label, font=font)
        text_w = text_bbox[2] - text_bbox[0]
    except AttributeError:
        text_w = draw.textlength(label, font=font)

    text_x = (width - text_w) / 2
    text_y = height + 5
    
    draw.text((text_x, text_y), label, fill="#666666", font=font) # Dark grey for "small/subtle" look
    
    # Save
    filename = f"qr_{name}_link.png"
    new_img.save(filename)
    print(f"Generated {filename}")
