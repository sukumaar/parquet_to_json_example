import polars as pl

def parquetToJson(inputPath:str,outputPath:str):
    df=pl.read_parquet(inputPath)
    df.write_json(outputPath)
    print(f"Converted parquet at {inputPath} to json & stored to {outputPath}")
    