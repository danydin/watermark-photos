import os
from PIL import Image, ImageDraw, ImageFont


def add_text_watermark_to_folder(
    input_dir, output_dir, watermark_text, font_size=30
):
    # Create output directory if it doesn't exist
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    for filename in os.listdir(input_dir):
        if filename.lower().endswith((".jpg", ".jpeg", ".png", ".bmp")):
            image_path = os.path.join(input_dir, filename)
            original = Image.open(image_path)
            width, height = original.size
            # print(f"width: {width} -- height: {height}")

            # Create ImageDraw object
            draw = ImageDraw.Draw(original)

            # Fonts:
            ## win C:\Windows\Fonts
            ## Mac /Library/Fonts and System/Library/Fonts

            # Get the font
            # arialFont = ImageFont.truetype(os.path.join(fontsFolder, "arial.ttf"), 32)
            # Specify font
            font = ImageFont.truetype("super_nought.ttf", size=font_size)

            # The mask represents the shape of the text characters as a binary image. and reterive the x and y of the watermark text
            text_width = font.getmask(watermark_text).getbbox()[2]
            text_height = font.getmask(watermark_text).getbbox()[3]
            # print(f"text width {text_width}, {text_height}")

            # create space around the watermark
            margin = 0
            # coords to place the watermark in the bottom right corner
            a = width - text_width - margin
            b = height - text_height - margin

            # print(f"text width {a}, {b}")

            # Apply the watermark
            draw.text((a, b), watermark_text, fill="white", font=font)

            # Save the watermarked image in the output directory
            output_path = os.path.join(output_dir, f"watermarked_{filename}")
            original.save(output_path)
            print(f"Watermarked image saved as {output_path}")


# Example usage
# example dir: /Users/mycomputername/Code/vincibits/automation/watermaring-tool/output_dir
input_directory = "./input_dir"  # Replace with your input directory
output_directory = "./output_dir"  # Replace with your output directory
watermark = "github.com/danydin"  # Replace with your watermark text

add_text_watermark_to_folder(
    input_directory, output_directory, watermark, font_size=199
)
