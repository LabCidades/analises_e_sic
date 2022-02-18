from .utils import download_bin_file, full_file_path
import os
import pandas as pd


class DataLoader:
    '''Loads the original data as a pandas dataframe.
    If the file at self.file_name doesn't exists, downloads 
    the data from self.url and creates the file.'''


    def __init__(self, url, file_name, save_dir):
        self.url = url
        self.file_name = file_name
        self.save_dir = save_dir

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


def get_solicitacoes():

    url = ('http://www.arquivoestado.sp.gov.br/uploads/publicacoes/material_apoio/'
    'pedidos_respostas_sic_2012_20211231.xlsx')
    file_name = 'solicitacoes_e_sic_gov_sp.xlsx'
    save_dir = 'original_data'

    load_data = DataLoader(url, file_name, save_dir)

    return load_data()

def get_usuarios():

    #ESSE LINK NAO FUNCIONA PORQUE É DO SLACK, PREICSAVA DE UM LINK GERAL
    url = ('https://files.slack.com/files-pri/T02HCM7A4L8-F032M9HUF34/download/'
    'protocolo_sic_37041221792_-_resposta_1___instancia_-_planilha_bd.xlsx')
    file_name = 'usuarios_e_sic_gov_sp.xlsx'
    save_dir = 'original_data'

    load_data = DataLoader(url, file_name, save_dir)

    return load_data()

    
    
