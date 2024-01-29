import pandas as pd
import logging

# log file
logging.basicConfig(format='%(asctime)s %(levelname)s:%(message)s', datefmt='%d/%m/%Y %I:%M:%S %p', filename='limpeza.log',level=logging.DEBUG)
logging.info('Limpeza iniciada...')

df = pd.read_csv('dataset/zomato.csv')

COUNTRIES = {
1: "India",
14: "Australia",
30: "Brazil",
37: "Canada",
94: "Indonesia",
148: "New Zeland",
162: "Philippines",
166: "Qatar",
184: "Singapure",
189: "South Africa",
191: "Sri Lanka",
208: "Turkey",
214: "United Arab Emirates",
215: "England",
216: "United States of America",
}

try:
    df.dropna(axis=0, inplace=True, ignore_index=True)
    logging.info('Valores NaN foram removidos.')
except Exception as e:
    logging.error(f'Erro durante remoção dos NaNs: {e}')
    
try:
    for x in list(df.columns):
        command = f"df['{x}'].dtypes"
        if pd.eval(command) == 'object':
            df[x] = df[x].str.strip()
    
    logging.info('Removendo espacos em colunas "object".')
except Exception as e:
    logging.error(f'Erro durante strip(): {e}')

try:
    df["Cuisines"] = df.loc[:, "Cuisines"].apply(lambda x: x.split(",")[0])
    logging.info(f'Pegando apenas 1 valor da col Cuisines.')
except Exception as e:
    logging.error(f'Erro ao filtrar coluna Cuisines: {e}')
    
try:
    df['Country Name'] = df.loc[:,'Country Code'].apply(lambda x: COUNTRIES[x])
    logging.info(f'Gerando coluna "Country Name".')
except Exception as e:
    logging.error(f'Erro durante criação da coluna "Country Name": {e}')

try:
    df.to_csv('dataset/zomato_clean.csv', index=False)
    logging.info(f'Gerado csv com dataset limpo.')
except Exception as e:
    logging.error(f'Erro ao salvar novo dataset: {e}')

logging.info('Fim do script de limpeza!')