import pandas as pd


def clean(input_file_1, input_file_2):
    df1 = pd.read_csv(input_file_1)
    df2 = pd.read_csv(input_file_2)
    df = pd.merge(df1, df2, left_on='respondent_id', right_on='id')
    df = df.drop('id', axis=1)
    df = df.dropna()
    df = df[~df['job'].str.contains('insurance', case=False)]
    return df


if __name__ == '__main__':
    import argparse

    parser = argparse.ArgumentParser()
    parser.add_argument('input1', help='First Data file (CSV)')
    parser.add_argument('input2', help='Second Data file (CSV)')
    parser.add_argument('output', help='Merged & Cleaned data file (CSV)')
    args = parser.parse_args()

    cleaned = clean(args.input1, args.input2)
    cleaned.to_csv(args.output, index=False)
