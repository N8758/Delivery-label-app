import os
from barcode import Code128
from barcode.writer import ImageWriter

def generate_barcode_image(delivery_id, output_dir="output"):
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    barcode_file = os.path.join(output_dir, delivery_id)
    barcode_obj = Code128(delivery_id, writer=ImageWriter())
    full_path = barcode_obj.save(barcode_file)
    return full_path
