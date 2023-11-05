
from PIL import Image
import os
from colorama import init, Fore

# Initialize colorama
init(autoreset=True)

print(Fore.YELLOW + "Running final.py")

# Define the directory where the PNG and TXT files are located
directory = 'dataset/graphs'

# Loop through all the files in the directory
for filename in os.listdir(directory):
    if filename.endswith('.png'):
        # Extract the file name without extension
        file_name_without_ext = os.path.splitext(filename)[0]
        
        # Check if there is a corresponding TXT file
        txt_file_path = os.path.join('dataset/final', file_name_without_ext + '.txt')
        if os.path.exists(txt_file_path):
            # Open and display the PNG file
            png_file_path = os.path.join(directory, filename)
            img = Image.open(png_file_path)
            img.show()
            
            # Read and display the contents of the TXT file along with the file name
            with open(txt_file_path, 'r') as txt_file:
                txt_contents = txt_file.read()
                print(Fore.GREEN + "Most important news of {}:".format(file_name_without_ext))
                print(txt_contents)
                print()
        else:
            print("No corresponding TXT file found for {}".format(filename))
