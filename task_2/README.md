## How to run this file

Example:

`./task_2.py -o output.csv -n 1000000`

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

if I would be able to split the .csv file, I would also split how is being saved, I would do it in batches (_0001.csv, _0002.csv) since it will make it easier to read and write. in this case, to have everything in just one file I will 

If this script had to run in a production environment, what tests would you 
include to ensure it's running correctly? Add the tests.

Answer:

If you were having this code reviewed, what else would you do with your code 
to ensure the code is clean and well-formatted?

Answer: 