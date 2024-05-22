from PIL import Image
import numpy as np

def load_and_process_image(image_path):
    # Load the image
    img = Image.open(image_path).convert('L') # Convert to grayscale
    img = img.resize((500, 500), Image.BICUBIC) # Resize using BICUBIC filter
    img_array = np.array(img)
    
    # Normalize the image to a range suitable for G-code (e.g., 0 to 100)
    normalized_img = (img_array / 255.0) * 100
    
    return normalized_img

# Ensure the image path is correct
image_path = 'img2.png' # Update this path if necessary
image_data = load_and_process_image(image_path)

def image_to_gcode(image_data):
    gcode = []
    for y in range(image_data.shape[0]):
        for x in range(image_data.shape[1]):
            # Assuming a simple engraving pattern where darker pixels are engraved deeper
            depth = image_data[y, x]
            if depth > 0: # Only engrave if the pixel is not black
                gcode.append(f"G1 X{x} Y{y} Z{depth}")
    return gcode

gcode_commands = image_to_gcode(image_data)

def save_gcode_to_file(gcode_commands, file_path):
    try:
        with open(file_path, 'w') as f:
            for command in gcode_commands:
                f.write(command + '\n')
        print(f"G-code saved to {file_path}")
    except Exception as e:
        print(f"Error saving G-code to file: {e}")

# Ensure the file path is correct and you have write permissions
gcode_file_path = 'gcode.gcode' # Update this path if necessary
save_gcode_to_file(gcode_commands, gcode_file_path)
