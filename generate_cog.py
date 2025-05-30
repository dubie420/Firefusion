import subprocess
import sys

def to_cog(input_tif, output_tif):
    command = [
        "gdal_translate", "-of", "COG", "-co", "COMPRESS=LZW",
        input_tif, output_tif
    ]
    subprocess.run(command, check=True)

if __name__ == "__main__":
    if len(sys.argv) < 3:
        print("Usage: python generate_cog.py input.tif output_cog.tif")
        sys.exit(1)
    to_cog(sys.argv[1], sys.argv[2])
