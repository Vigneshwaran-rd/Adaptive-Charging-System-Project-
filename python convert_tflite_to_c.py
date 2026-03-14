# convert_tflite_to_c.py
tflite_file = "battery_model.tflite"
c_file = "model_data.h"

with open(tflite_file, "rb") as f:
    data = f.read()

with open(c_file, "w") as f:
    f.write(f"unsigned char battery_model_tflite[] = {{\n")
    for i, b in enumerate(data):
        f.write(f"0x{b:02x}, ")
        if (i+1) % 12 == 0:
            f.write("\n")
    f.write(f"\n}};\n")
    f.write(f"unsigned int battery_model_tflite_len = {len(data)};\n")

print("C header file generated:", c_file)