## How to use it?

`csv_generator.py` the final step of the script which uses a Process pool to generate the data 

Example:

`./csv_generator.py -n 1000000 -o output.csv -n 1000000`

To run tests use:

`python3 -m unittest test_csv_generator.py`

## Create a script to generate a CSV file with random data.

Example output:
```
1234, randomstring
```

Add the ability to pass in command line parameters. Use an argument to pass 
in the number of rows to generate. 
Add another argument for the filename to use for the CSV file.

If you had to generate a large number of rows (millions or more), is there 
anything you would do differently to handle this?
Modify your script to handle this requirement.

Answer: Yes, I would handle the generation of the data, on separate cores

if I would be able to split the .csv file, I would also split how is being saved, I would do it in batches (file_0001.csv, file_0002.csv) since it will make it easier to read and write in the files. in this case, to have everything in just one file I would just handle separately how the data is being generated.

If this script had to run in a production environment, what tests would you 
include to ensure it's running correctly? Add the tests.

Answer: I would test the common route, assuring that the file is being generated with the desired number of rows and data content, without undesired characters

If you were having this code reviewed, what else would you do with your code 
to ensure the code is clean and well-formatted?

Answer: follow the pep8 guidelines, significant variable names and an easy to follow flow