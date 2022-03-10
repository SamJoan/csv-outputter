"""
Create a python3 script, that when executed from
the command line can accept up to three named options and output a csv file in a local directory of the server we execute it from.

The
second named option `output_path`  can only be specified once and is optional, this is to specify where we want the file to be saved. If not specified, the file will be saved in the current directory.

The
third named option is `column` and MUST be specified at least once but can be specified multiple times. The form of the argument must be: column_name,type. Type of the argument can be `integer` or `string`.


If
a required option is missing or is invalid you MUST show a message on how to use the program.


The
program must output a csv of n rows specified via the `rows` argument, the header specified in the `column` option via the column_name must appear in the csv file. We will generate different random data for each columns and rows of type integer (eg: 1,2,3000,
…) or string (alpha strings with a length between 1 and 10 characters)


The
csv filename must be of the form YYYY-MM-DD-HH_MM_SS.csv (eg: 2018-04-27-6_50_55), using the time at which we are executing the program.
"""
from random import randint
import click
import random
import string

@click.command()
@click.option('--rows', default=50, help='This will dictate the number of rows in the output csv file.')
@click.option('--output-path', default='./', help='This is to specify where we want the file to be saved. If not specified, the file will be saved in the current directory.')
@click.option('--column', '-c', 'columns', required=True, multiple=True,
        help='The form of the argument must be: column_name,type. Type of the argument can be `integer` or `string`.')
def csv(rows, output_path, columns):
    result = ""

    row = ""
    for nb, column in enumerate(columns):
        name, _ = column.split(',')
        row += name
        if nb != len(columns) -1:
            row += ","

    result += row + "\n"

    for nb_row, x in enumerate(range(rows)):
        row = ""
        for nb, column in enumerate(columns):
            _, type = column.split(',')

            if type == 'int':
                row += str(randint(1, 10000))
            elif type == 'string':
                row += ''.join(random.choices(string.ascii_letters + string.digits, k=randint(1,10)))
            else:
                raise Exception("Unsupported column type")

            if nb != len(columns) - 1:
                row += ','
        
        result += row 
        if nb_row != rows - 1:
            result += '\n'

    print(result)

if __name__ == '__main__':
    csv()
