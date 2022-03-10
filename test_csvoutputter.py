from click.testing import CliRunner
from csvoutputter import csv


BASE_ARGS = ['--column', 'id,int', '--column', 'username,string', '--rows', '5']

def test_missing_column_argument():
    runner = CliRunner()
    result = runner.invoke(csv, [])
    assert result.exit_code == 2

def test_rows_argument_default():
    runner = CliRunner()
    result = runner.invoke(csv, ['--column', 'id,int'])
    assert result.exit_code == 0
    assert len(result.output.split('\n'))-1 == 51 # one line for the header

def test_rows_argument_five():
    runner = CliRunner()
    result = runner.invoke(csv, ['--column', 'id,int', '--rows', '5'])
    assert result.exit_code == 0
    assert len(result.output.split('\n'))-1 == 6

def test_column_argument():
    runner = CliRunner()
    result = runner.invoke(csv, BASE_ARGS)
    assert result.exit_code == 0

    header_col = result.output.split('\n')[0]
    assert header_col.strip() == 'id,username'
    first_row = result.output.split('\n')[1]

    splat = first_row.split(',')

    int(splat[0]) # it will fail if not numeric
    assert 1 <= len(splat[1]) <= 10

