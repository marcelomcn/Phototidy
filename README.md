
PhotoTidy: Efficient Photo Organization and Metadata Extraction


Overview
PhotoTidy is a high-performance application designed to quickly organize and manage your photo collection by extracting and sorting metadata from your images. With its efficient processing capabilities, PhotoTidy helps streamline your photo organization tasks, making it easier to sort and catalog your pictures.

Features
Fast Photo Organization: Quickly sorts and organizes photos based on extracted metadata.
Metadata Extraction: Extracts relevant metadata from image files, such as EXIF data, to categorize and organize photos.
User-Friendly Operation: Simple and intuitive to use with minimal setup required.

Installation
Prerequisites
Python 3.7+: Ensure Python is installed on your system.
Required Python Packages: PhotoTidy relies on specific Python libraries for its functionality.
Installing Dependencies
Clone the Repository:

Open a terminal and clone the repository:

bash

git clone https://github.com/marcelomcn/phototidy.git
cd phototidy
Install Required Python Packages:

Install the necessary Python libraries using pip:

bash
pip install pillow exifread
Running PhotoTidy
Execute the Application
To run PhotoTidy, you need to execute the run_script.sh file. Follow these steps:

Navigate to the Directory:

Open a terminal and go to the directory where run_script.sh is located:

bash

cd /home/m/Downloads/phototidy

give permission to the Script:
chmod +x run_script.sh

Execute the script to launch the PhotoTidy application:

bash

./run_script.sh

This command will start PhotoTidy, which will begin processing your photo collection to extract metadata and organize your pictures.

What the Program Does
Organizes Photos: PhotoTidy scans your image directory, extracts metadata from each photo, and sorts them based on this information.
Metadata Sorting: Uses extracted metadata (such as date, location, and camera settings) to categorize and organize your photos, making them easier to browse and manage.
Efficient Processing: Designed to handle large photo collections quickly and efficiently, ensuring minimal waiting time.
Troubleshooting
Script Not Executing: If you encounter issues running the script, ensure it has executable permissions:

bash


Missing Dependencies: Ensure all required Python packages are installed. If you receive errors related to missing packages, install them using:

bash

pip install pillow exifread
Path Issues: Verify that the paths and filenames in the run_script.sh file are correct and match your setup.

Support
For further assistance or to report any issues, please contact us at support@aurawave.eu.

License
PhotoTidy is licensed under the MIT License.
