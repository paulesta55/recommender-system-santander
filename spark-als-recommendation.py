import argparse
import pandas as pd
from tqdm import tqdm
import implicit
import numpy as np
import scipy.sparse as sparse


def main(input_file, output_file):
    df = pd.read_csv(input_file)
    # initialize a model
    model = implicit.als.AlternatingLeastSquares(factors=50)

    model.fit()

    return None


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("-f", "--file", help="Input csv file", required=True)
    parser.add_argument("-o", "--output", help="Output name", required=True)
    args = parser.parse_args()
    main(args.file, args.output)
