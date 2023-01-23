## How to use? 

There are two scripts with the same porpuse, `normalize_csv.py` and `normalize_csv_with_libs.py` one uses customs methods and the other uses the csv library:

Examples:

- define automatically the delimiter and quote character
`./normalize_csv.py examples/example_2`

- specify delimiter and quote character
`./normalize_csv.py examples/example_2 -d @ -q "`

Write a function to normalize CSV files by converting a pipe-delimited file 
into a comma-delimited file.
Your original file will look like this:

    Planet|Manufacturer|Model|Type|Passengers
    Yavin|Ubrikkian" Industries|Sail Barge|sailbarge|500
    Bespin|Bespin Motors|Storm IV, Twin-Pod|repulsorcraft|0
    Kuat|Kuat Drive Yards|AT-ST|walker|0

When you run your script, the output should look like this:

    Planet,Manufacturer,Model,Type,Passengers
    Yavin,"Ubrikkian"" Industries",Sail Barge,sailbarge,500
    Bespin,Bespin Motors,"Storm IV, Twin-Pod",repulsorcraft,0
    Kuat,Kuat Drive Yards,AT-ST,walker,0

It's valid for a comma to be in your input data. You'll need to surround 
strings with commas in them with double quotes when writing your output file.

It's also valid for double quote characters to be in your input - you will 
need to double up quotes.

BONUS 1:
    Add in the ability to accept command line parameters for:
        the input delimiter to use ('|' should be the default)
        the quote character to use (" by default)

BONUS 2:
    Try to automatically detect the delimiter and quote character if they are 
    not supplied on the command line.
    If either the delimiter or the quote character are provided, assume the 
    other one is the default. But if both are missing, you should try to 
    automatically detect them.
    NOTE: This may not work for all files.