#!/usr/bin/env python 
import argparse
import sys
from .converter.parquet_to_json import parquetToJson


parser = argparse.ArgumentParser(description='Reads parquet file and write as json')
parser.add_argument("--input_path","--i",type=str,help="absolute input path for parquet file")
parser.add_argument("--output_path","--o",type=str,help="absolute output path for json file")

def main():
    args=parser.parse_args(args=(sys.argv[1:] or ['--help']))
    parquetToJson(args.input_path,args.output_path)
    
if __name__=="__main__":
    main()