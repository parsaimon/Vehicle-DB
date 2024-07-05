import json
import os


def create_individual_json_files(file_path, output_folder):
    # Ensure the output folder exists
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    # Read the JSON data from the provided file path
    with open(file_path, 'r') as file:
        vehicle_brands = json.load(file)

    # Iterate through each vehicle brand object
    for brand in vehicle_brands:
        # Format the file name: lowercase and replace spaces with underscores
        file_name = os.path.join(output_folder, brand["name"].lower().replace(" ", "_") + ".json")

        # Check if the file already exists to avoid overwriting
        if not os.path.exists(file_name):
            # Write the brand object to a new JSON file
            with open(file_name, 'w') as file:
                json.dump(brand, file, indent=4)


# Define the path to the master file and the output folder
master_file_path = '../vehicle_brand_master.json'  # Adjusted path to root folder
output_folder = '../models'  # Output folder within the script directory

# Call the function with the updated paths
create_individual_json_files(master_file_path, output_folder)

#test commit