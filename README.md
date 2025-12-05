# ISM2411 Data Cleaning with GitHub Copilot

This project shows a Python workflow for cleaning a messy dataset.

The script:
1. Standardizes the column names  
2. Strips whitespace from text fields  
3. Handles the missing values in the dataset 
4. Removes the invalid values which are the negative ones
5. Saves a cleaned excel file

The project also uses GitHub Copilot to generate some of the initial code, which was then tweaked so that it would work how it is supposed to.

## Running the Script
1. Have Python installed
2. Install pandas
3. Run the following command in a terminal from the project root directory:

`python src/data_cleaning.py`