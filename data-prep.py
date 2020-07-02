import argparse
import csv
from tqdm import tqdm


def main(csv_file_path, dates, output_file_path):
    kept_rows = []
    with open(csv_file_path) as csv_file:
        reader = csv.reader(csv_file, delimiter=',')
        for idx, row in enumerate(tqdm(reader)):
            if idx == 0:
                kept_rows.append(row)
            elif row[0] in dates:
                kept_rows.append(row)
    with open(output_file_path, 'w', newline='') as new_file:
        writer = csv.writer(new_file, delimiter=",")
        with tqdm(total=len(kept_rows)) as pbar:
            for row in kept_rows:
                writer.writerow(row)
                pbar.update(1)


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("-d", "--dates", nargs='+', help="list of dates in format yyyy-mm-dd yyyy-mm-dd ...",
                        required=True)
    parser.add_argument("-f", "--file", help="Input csv file", required=True)
    parser.add_argument("-o", "--output", help="Output name", required=True)
    args = parser.parse_args()
    print(args.dates)
    main(args.file, args.dates, args.output)
