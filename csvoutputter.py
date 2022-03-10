from datetime import datetime
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

    if output_path == '-':
        print(result)
    else: 
        now = datetime.now()
        filename = now.strftime("%Y-%m-%d-%H_%M_%S.csv")
        print(filename)
        with open(output_path + '/' + filename, 'w') as fh:
            fh.write(result)

if __name__ == '__main__':
    csv()
