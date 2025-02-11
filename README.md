# CSV Comparison Tool

## Overview

The CSV Comparison Tool is a desktop application designed to compare two CSV files and identify
rows from the first file that are not present in the second file, based on the first column.
This tool is particularly useful for managing translation files, where you need to ensure
that all necessary translation keys are present across different language versions.

## Features

Compare two CSV files based on the first column of each.
Easily select files through a graphical user interface.
Automatically handles quoted and comma-containing entries in CSV files.
Outputs a new CSV file containing the missing rows from the first file.

## Prerequisites
To run this application, you will need:

Python installed on your machine (Python 3.7 or newer recommended).
Pandas library installed for handling CSV files.
Tkinter library installed for the GUI (usually included with Python).

## Installation

Install Python Ensure that Python is installed on your system. You can download it from python.org.

Install Required Python Libraries Open a terminal or command prompt and install the necessary Python libraries using pip:

    pip install pandas

Download the Application Download the script provided above, and save it to a known directory on your computer.

## Usage
Run the Application

Navigate to the directory where the script is saved.
Open a terminal or command prompt in this directory.
Run the script with the following command:

    python csv_comparison_tool.py

## Using the Application

Upon launching, the application will display a window with buttons to browse and select two CSV files.
Select CSV File 1: This is the primary file that you want to check for missing entries.
Select CSV File 2: This file is used as the reference to check against.
After selecting both files, click the "Compare CSVs" button to start the comparison.
The application will process the files and output a new file named missing_entries.csv in the same directory as the script, containing any rows from File 1 that do not have a matching first column in File 2.

## Troubleshooting
CSV Format Issues: Ensure that your CSV files do not contain inconsistent row formats. Each row should consistently use commas to delimit fields, and text should be appropriately quoted if it contains commas.
Python or Library Issues: Ensure Python and all required libraries are correctly installed. Errors during execution may be related to missing or outdated libraries.

## License
This software is provided "as is", without warranty of any kind.