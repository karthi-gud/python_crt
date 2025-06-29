import json # To handle structured data (like a mini-database)
import qrcode # To create the QR code images
from PIL import Image # Pillow, to work with image files (used by qrcode and pyzbar)
from pyzbar.pyzbar import decode # To read and decode QR codes from images
import os # To help us manage file paths on your computer

# --- 1. Data Setup: What information we want to encode ---
# This is our sample data for a species. You can change these values!
species_name = "Panthera tigris"
dna_sequence = "ATGCGTAATGCGTAATGCGTAATGCGTAATGCGTAATGCGTAATGCGTAATGCGTAA" # A simplified example DNA sequence
sample_id = "Tiger_001"
gene_name = "COI" # Common gene used for DNA barcoding

# We put all our information into a Python dictionary.
# This makes it easy to keep related pieces of data together.
metadata_to_encode = {
    "species": species_name,
    "sample_id": sample_id,
    "gene": gene_name,
    "sequence": dna_sequence
}

# We convert our Python dictionary into a JSON string.
# JSON is a standard text format that computers can easily understand
# and that fits nicely inside a QR code.
json_data_string = json.dumps(metadata_to_encode)
print(f"JSON data prepared for embedding in QR code: {json_data_string}")

# --- 2. QR Code Generation: Turning data into an image ---

# First, we set up the QR code properties:
# 'version' controls size (higher version = more data).
# 'error_correction' makes the QR code scannable even if slightly damaged.
# 'box_size' is how large each small square in the QR code is (in pixels).
# 'border' is the white space around the QR code.
qr_generator = qrcode.QRCode(
    version=1,
    error_correction=qrcode.constants.ERROR_CORRECT_L, # Low error correction
    box_size=10,
    border=4,
)

# We add our JSON data string to the QR code generator.
qr_generator.add_data(json_data_string)
# 'fit=True' tells it to adjust the size if needed for the data.
qr_generator.make(fit=True)

# Now, we create the actual image from the QR code data.
# We choose black squares on a white background.
qr_image = qr_generator.make_image(fill_color="black", back_color="white")

# --- 3. Saving the QR Code Image ---

# This part is crucial for making sure the file is saved and found correctly!
# We get the directory (folder) where this Python script is located.
script_directory = os.path.dirname(os.path.abspath(__file__))

# We create a descriptive filename for our QR code image.
# We replace spaces with underscores to avoid issues in filenames.
qr_image_filename = f"DNA_Barcode_{species_name.replace(' ', '_')}_{sample_id}.png"

# We combine the script's directory with our filename to get the full path
# This ensures the image is saved right next to your script.
full_image_path = os.path.join(script_directory, qr_image_filename)

# Save the QR code image to the determined path.
qr_image.save(full_image_path)
print(f"QR code generated and saved as: '{full_image_path}'")

# --- 4. Decoding the QR Code: Reading information back from the image ---

# Now, we'll try to read the QR code we just saved.
# We use the 'full_image_path' to open the exact file we created.
try:
    # Open the image file using Pillow
    image_to_decode = Image.open(full_image_path)
except FileNotFoundError:
    print(f"Error: The image file was not found at '{full_image_path}'.")
    print("Please make sure the QR code was generated successfully and is in the correct location.")
    exit() # Stop the script if the image isn't found

# Use pyzbar to decode any QR codes found in the image.
decoded_qr_objects = decode(image_to_decode)

# Check if any QR codes were found in the image.
if decoded_qr_objects:
    # If a QR code is found, its data is in the first object.
    # The 'data' is in bytes, so we decode it to a UTF-8 string.
    raw_decoded_string = decoded_qr_objects[0].data.decode('utf-8')
    print(f"\nRaw data string successfully decoded from QR code: {raw_decoded_string}")

    # Now, try to convert the JSON string back into a Python dictionary.
    try:
        extracted_metadata = json.loads(raw_decoded_string)
        print("\nSuccessfully Extracted Metadata from QR Code:")
        # Print each piece of information clearly.
        for key, value in extracted_metadata.items():
            print(f"  - {key.replace('_', ' ').title()}: {value}")
    except json.JSONDecodeError:
        # This catches errors if the data inside the QR code wasn't valid JSON.
        print(f"Error: Could not understand the data inside the QR code (not valid JSON). Raw data was: {raw_decoded_string}")
else:
    print("No QR code could be found in the image. Make sure the QR code is clear and not damaged.")