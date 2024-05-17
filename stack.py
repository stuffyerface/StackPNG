from PIL import Image
import os

def stack_images_vertically(output_path):
    # Get all PNG images in the current directory
    image_paths = [file for file in os.listdir() if file.endswith('.png') and file != output_path]
    
    if not image_paths:
        print("No PNG images found in the current directory.")
        return

    # Open all images and get their sizes
    images = [Image.open(image_path) for image_path in image_paths]
    widths, heights = zip(*(image.size for image in images))

    # Calculate the total height and maximum width for the new image
    total_height = sum(heights)
    max_width = max(widths)

    # Create a new blank image with the appropriate size
    new_image = Image.new('RGBA', (max_width, total_height))

    # Paste each image into the new image
    y_offset = 0
    for image in images:
        new_image.paste(image, (0, y_offset))
        y_offset += image.height

    # Save the new image
    new_image.save(output_path, 'PNG')

if __name__ == "__main__":
    output_path = "stacked_image.png"  # Default output file name
    stack_images_vertically(output_path)
    print(f"Stacked image saved as {output_path}")