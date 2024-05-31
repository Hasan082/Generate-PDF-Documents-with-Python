# Generate PDF from CSV with Python

## Overview

This project demonstrates how to generate a PDF document from data stored in a CSV file using Python and the `FPDF` library. The script reads a CSV file containing topics and page numbers, and creates a PDF where each topic is given a specified number of pages, with the topic name as a header on the first page and a footer on each page.

## Prerequisites

- Python 3.x
- `fpdf` library
- `pandas` library

## Installation

1. **Python Installation**: Ensure you have Python 3.x installed on your system. You can download it from [python.org](https://www.python.org/downloads/).

2. **Installing Required Libraries**:
    ```bash
    pip install fpdf pandas
    ```

## CSV File Format

The script expects a CSV file named `topics.csv` in the same directory as the script. The CSV should have the following format:

| Topic       | Pages |
|-------------|-------|
| Topic 1     | 3     |
| Topic 2     | 2     |
| Topic 3     | 5     |

- **Topic**: The topic name to be used as the header and footer in the PDF.
- **Pages**: The number of pages to generate for this topic.

## Script Explanation

The script reads the `topics.csv` file and generates a PDF as follows:

1. **Create FPDF Object**: Initialize the FPDF object with portrait orientation (`P`), millimeter units (`mm`), and A4 page size (`A4`).

2. **Read CSV**: Load the CSV file into a pandas DataFrame.

3. **Iterate Through Rows**: For each row in the DataFrame:
   - Add a new page.
   - Set the font and text color for the header and add the topic name as a header.
   - Draw a line below the header.
   - Add the topic name as a footer on the first page.
   - Add additional pages as needed, each with the topic name as a footer.

4. **Save PDF**: Save the generated PDF as `tuto1.pdf`.

## Usage

1. **Prepare CSV File**: Create a `topics.csv` file with the desired topics and page numbers as described above.

2. **Run the Script**: Execute the script to generate the PDF.
    ```bash
    python main.py
    ```

3. **Output**: The script will produce a file named `tuto1.pdf` in the same directory.

## Notes

- Adjust the `ln` values in the script if the footer or header positioning needs to be changed.
- Ensure the `topics.csv` file is correctly formatted and located in the same directory as the script.