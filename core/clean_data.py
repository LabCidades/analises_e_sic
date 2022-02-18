from .get_data import DataLoader
from pprint import pprint

class DataCleaner:

    def drop_all_empty_cols_and_rows(self, df):

        original_cols = df.columns
        num_rows = len(df)
        df = df.copy()
        df = df.dropna(axis = 0, how='all')
        df = df.dropna(axis = 0, how='all')

        deleted_cols = [col for col in original_cols
                        if col not in df.columns]
        deleted_rows = num_rows-len(df)

        if deleted_rows:
            print(f'Droped {deleted_rows} all empty rows')
        if deleted_cols:
            print(f'Droped the following all empty cols: {deleted_cols}')

        return df

    def null_report(self, df):
        
        num_records = len(df)
        result = {}
        for col in df.columns:
            qt_nulls = df[col].isnull().sum()
            result[col] = {
                'qtd_nulos' : qt_nulls,
                'prop_nulos' : qt_nulls/num_records
            }
        
        print('Null report:')
        pprint(result)

        return result

    def drop_nulls(self, df, threshould = 0.9):

        df = df.copy()

        df = self.drop_all_empty_cols_and_rows(df)
        null_report = self.null_report(df)

        cols_to_drop = []
        for col_name, col_data in null_report.items():

            if col_data['prop_nulos'] >= threshould:
                cols_to_drop.append(col_name)

        df = df.drop(cols_to_drop, axis=1)

        print(f'Droped following columns with > {threshould} nuls:')
        print(cols_to_drop)

        return df

    def __call__(self, df, threshould = 0.9):

        return self.drop_nulls(df, threshould)


        
