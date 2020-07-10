import argparse
import csv
from tqdm import tqdm

cols = ['ind_ahor_fin_ult1', 'ind_aval_fin_ult1', 'ind_cco_fin_ult1', 'ind_cder_fin_ult1', 'ind_cno_fin_ult1',
        'ind_ctju_fin_ult1', 'ind_ctma_fin_ult1',
        'ind_ctop_fin_ult1', 'ind_ctpp_fin_ult1', 'ind_deco_fin_ult1', 'ind_deme_fin_ult1', 'ind_dela_fin_ult1',
        'ind_ecue_fin_ult1', 'ind_fond_fin_ult1',
        'ind_hip_fin_ult1', 'ind_plan_fin_ult1', 'ind_pres_fin_ult1', 'ind_reca_fin_ult1', 'ind_tjcr_fin_ult1',
        'ind_valo_fin_ult1', 'ind_viv_fin_ult1',
        'ind_nomina_ult1', 'ind_nom_pens_ult1', 'ind_recibo_ult1']


def main(csv_file_path, output_file_path):
    with open(csv_file_path) as csv_file:
        reader = csv.reader(csv_file, delimiter=',')
        next(reader)
        with open(output_file_path, 'w', newline='') as new_file:
            writer = csv.writer(new_file, delimiter=",")
            for idx, row in enumerate(tqdm(reader)):

                selected_cels = row[24:]
                for i, cel in enumerate(selected_cels):
                    tmp_row = []
                    tmp_row.append(row[1])
                    tmp_row.append(i)
                    tmp_row.append(cel)
                    writer.writerow(tmp_row)


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("-f", "--file", help="Input csv file", required=True)
    parser.add_argument("-o", "--output", help="Output name", required=True)
    args = parser.parse_args()
    main(args.file, args.output)
