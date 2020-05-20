# -*- coding: utf-8 -*-

import argparse
import sys
import pandas as pd

def DeleteLine(InputFile, OutputFile, axis, elements):
  csv = pd.read_csv(InputFile)
  csv = csv.drop(elements, axis, errors='ignore')    
  csv.to_csv(OutputFile, index=False)
  print("Processing is complete.")

if __name__ == '__main__':
  parser = argparse.ArgumentParser(
    prog="DeleteLineCSV",
    usage="削除したい行及び列の要素を指定してください",
    description="CSVファイルの不要な行や列を削除するツール",
    epilog="end",
    add_help=True)

  parser.add_argument('InputFile', help="Input File")
  parser.add_argument('OutputFile', default='./edited.csv', help="Output File")
  parser.add_argument('-a', '--axis', choices=['column', 'c', 'row', 'r'], required=True, help="Column or Row")
  parser.add_argument('-e', '--elements', nargs='*', required=True, help="Delete Elements")

  args = parser.parse_args()

  if args.InputFile.endswith('.csv'):
    if args.axis == 'column' or args.axis == 'c':
      axis = 0
      DeleteLine(args.InputFile, args.OutputFile, axis, args.elements)    
    elif args.axis == 'row' or args.axis == 'r':
      axis = 1
      DeleteLine(args.InputFile, args.OutputFile, axis, args.elements)
  else:
    print("Please Input the CSV file.")