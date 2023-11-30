from PIL import Image, ImageDraw

base = Image.new("RGBA", (1024, 1024), 'purple')

# Create a mask for rounded corners
mask = Image.new('L', (1024, 1024), 0)
draw = ImageDraw.Draw(mask)
draw.rounded_rectangle([(0, 0), (1024, 1024)], 160, fill=255)

# Apply the mask
base.putalpha(mask)

# Save the image
base.save('images/formatted/rounded_purple_icon.png')
