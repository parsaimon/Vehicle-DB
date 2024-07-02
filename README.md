# vehicle-master
 
# Vehicle Brands JSON Generator

This Python script generates individual JSON files for each vehicle brand listed in a master JSON file. The script is designed to run within a specific folder structure, ensuring that generated files are neatly organized and existing files are not overwritten.

## Folder Structure

- **Root Directory**: Contains the master JSON file (`vehicle_brand_master.json`) with a list of vehicle brands.
- **Script Folder**: Contains the Python script (`generate_json.py`) that processes the master list and generates individual JSON files.
- **Models Folder**: Located within the Script Folder, this is where all generated JSON files are stored.

## How It Works

The script reads the master JSON file from the root directory, iterates through each vehicle brand object, and creates an individual JSON file for each brand in the Models folder. The name of each generated file is the lowercase version of the brand name, with spaces replaced by underscores.

## Running the Script

To run the script, ensure you have Python installed on your system and follow these steps:

1. Place the `vehicle_brand_master.json` file in the root directory.
2. Navigate to the Script Folder in your terminal or command prompt.
3. Run the script using the command: `python generate_json.py`

## Important Notes

- The script checks if a JSON file for a brand already exists in the Models folder and will not overwrite existing files. This prevents loss of any modifications to the generated files.
- If the Models folder does not exist, the script will automatically create it.

## Requirements

- Python 3.x

## License

This project is open-source and available under the MIT License.
