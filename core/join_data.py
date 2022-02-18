

class JoinPrepper:

    def get_digits(self, item):
        
        txt= str(item)
        
        return ''.join([char for char in txt if char.isdigit()])

    def padronizar_col_id(self, df, col):
        
        df[col] = df[col].apply(self.get_digits)
        
        return df

    def filtrar_col_id(self, df, col):
        
        mask = df[col]==''
        
        return df[~mask].copy().reset_index(drop=True)


    def clean_col_id(self, df, col):
        
        df = self.padronizar_col_id(df, col)
        df = self.filtrar_col_id(df, col)
        
        return df

    def __call__(self, df, col='Número de Controle'):

        return self.clean_col_id(df, col)