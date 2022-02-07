from .utils import download_bin_file, full_file_path
import os
import pandas as pd


DATA_URL = 'http://www.arquivoestado.sp.gov.br/uploads/publicacoes/material_apoio/pedidos_respostas_sic_2012_20211231.xlsx'

class DataLoader:
    '''Loads the original data as a pandas dataframe.
    If the file at self.file_name doesn't exists, downloads 
    the data from self.url and creates the file.'''

    url = DATA_URL
    file_name = 'dados_e_sic_gov_sp.xlsx'
    save_dir = 'original_data'

    def download_data(self):
        
        file_path = download_bin_file(self.url,
                            self.file_name,
                            self.save_dir)

        return file_path

    def open_excel_file(self):

        file_path = full_file_path(self.file_name, self.save_dir)

        return pd.read_excel(file_path)

    def load_data(self):

        file_path = full_file_path(self.file_name, self.save_dir)

        if not os.path.exists(file_path):
            print(f'Downloading file at: {self.url}')
            file_path = self.download_data()
        
        return self.open_excel_file()

    def __call__(self):

        return self.load_data()


    
    
