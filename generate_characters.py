from PIL import Image, ImageDraw, ImageFont
import random
import os

CHARACTER_NAMES = [
    "Aether", "Luna", "Zerox", "Nyx", "Orion", "Nova", "Kael", "Sylva", "Thorne", "Eira"
]

def generate_image(name, level, save_dir="images"):
    img = Image.new('RGB', (512, 512), color=(random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)))
    draw = ImageDraw.Draw(img)
    font = ImageFont.load_default()
    draw.text((20, 20), f"Name: {name}", fill=(255, 255, 255), font=font)
    draw.text((20, 40), f"Level: {level}", fill=(255, 255, 255), font=font)
    if not os.path.exists(save_dir):
        os.makedirs(save_dir)
    path = os.path.join(save_dir, f"{name}_NFT.png")
    img.save(path)
    print(f"Saved: {path}")

def generate_characters(n=5):
    selected = random.sample(CHARACTER_NAMES, n)
    for name in selected:
        level = random.randint(1, 10)
        generate_image(name, level)

if __name__ == "__main__":
    generate_characters()
