The folder titled "Fifa" contains all the python programs used to run data-cleaning.
When provided with the original FIFA player files from 2015 to 2020, run the python programs in the following order:

1. Scout.py 
Used to search through the files and single out possible useful columns

2. Join.py 
Calculates the actual growth for each year and combines all csv files together

3. Normalize.py 
Applies feature normalization to appropriate categories. We used Z-score normalization

4. Refine.py 
Selects all features used for the machine learning model

5. ML.py 
Applies machine learning and makes predictions about a player

A sample of our visualization of the average growth per club can be found in the Visual.pdf file.

The Soccer_Club.ipynb file that can be found in the Repo folder is where we did the bulk of our machine learning. We did most of our prototyping and testing there.