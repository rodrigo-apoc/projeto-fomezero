import pandas as pd
import numpy as np
from collections import namedtuple

df = pd.read_csv('dataset/zomato_clean.csv')

def geral(opt):
    match opt:
        case 1:
            # 1. Quantos restaurantes únicos estão registrados?
            return df['Restaurant ID'].nunique()
        case 2:
            # 2. Quantos países únicos estão registrados?
            return df['Country Code'].nunique()
        case 3:
            # 3. Quantas cidades únicas estão registradas?
            return df['City'].nunique()
        case 4:
            # 4. Qual o total de avaliações feitas?
            return df['Votes'].sum()
        case 5:
            # 5. Qual o total de tipos de culinária registrados?
            return df['Cuisines'].nunique()

def pais(opt):
    match opt:
        case 1:
            # 1. Qual o nome do país que possui mais cidades registradas?
            return df.loc[:,['City','Country Name']].groupby(['Country Name']).nunique().sort_values(by=['City'], ascending=False).reset_index().iat[0,0]
        case 2:
            # 2. Qual o nome do país que possui mais restaurantes registrados?
            return df.loc[:,['Restaurant ID','Country Name']].groupby(['Country Name']).count().sort_values(by=['Restaurant ID'], ascending=False).reset_index().iat[0,0]
        case 3:
            # 3. Qual o nome do país que possui mais restaurantes com o nível de preço igual a 4 registrados?
            return df.loc[df['Price range'] == 4,['Restaurant ID','Country Name']].groupby(['Country Name']).count().sort_values(by=['Restaurant ID'], ascending=False).reset_index().iat[0,0]
        case 4:
            # 4. Qual o nome do país que possui a maior quantidade de tipos de culinária distintos?
            return df.loc[:,['Cuisines','Country Name']].groupby(['Country Name']).nunique().sort_values(by=['Cuisines'], ascending=False).reset_index().iat[0,0]
        case 5:
            # 5. Qual o nome do país que possui a maior quantidade de avaliações feitas?
            return df.loc[:,['Votes','Country Name']].groupby(['Country Name']).sum().sort_values(by=['Votes'], ascending=False).reset_index().iat[0,0]
        case 6:
            # 6. Qual o nome do país que possui a maior quantidade de restaurantes que fazem entrega?
            return df.loc[df['Is delivering now'] == 1,['Is delivering now','Country Name']].groupby(['Country Name']).count().sort_values(by=['Is delivering now'], ascending=False).reset_index().iat[0,0]
        case 7:
            # 7. Qual o nome do país que possui a maior quantidade de restaurantes que aceitam reservas?
            return df.loc[df['Has Table booking'] == 1,['Has Table booking','Country Name']].groupby(['Country Name']).count().sort_values(by=['Has Table booking'], ascending=False).reset_index().iat[0,0]
        case 8:
            # 8. Qual o nome do país que possui, na média, a maior quantidade de avaliações registrada?
            return df.loc[:,['Votes','Country Name']].groupby(['Country Name']).mean().sort_values(by=['Votes'], ascending=False).reset_index().iat[0,0]
        case 9:
            # 9. Qual o nome do país que possui, na média, a maior nota média registrada?
            return df.loc[:,['Aggregate rating','Country Name']].groupby(['Country Name']).mean().sort_values(by=['Aggregate rating'], ascending=False).reset_index().iat[0,0]
        case 10:
            # 10. Qual o nome do país que possui, na média, a menor nota média registrada?
            return df.loc[:,['Aggregate rating','Country Name']].groupby(['Country Name']).mean().sort_values(by=['Aggregate rating']).reset_index().iat[0,0]
        case 11:
            # 11. Qual a média de preço de um prato para dois por país?
            return np.round(df.loc[:,['Country Name','Average Cost for two']].groupby(['Country Name']).mean(), 2)

def cidade(opt):
    match opt:
        case 1:
            # 1. Qual o nome da cidade que possui mais restaurantes registrados?
            return df.loc[:,['Restaurant ID', 'City']].groupby(['City']).count().sort_values(by=['Restaurant ID'], ascending=False).reset_index().iat[0,0]
        case 2:
            # 2. Qual o nome da cidade que possui mais restaurantes com nota média acima de 4?
            return df.loc[df['Aggregate rating'] >= 4.0, ['City', 'Restaurant ID']].groupby(['City']).count().sort_values(by=['Restaurant ID'], ascending=False).reset_index().iat[0,0]
        case 3:
            # 3. Qual o nome da cidade que possui mais restaurantes com nota média abaixo de 2.5?
            return df.loc[df['Aggregate rating'] <= 2.5, ['City', 'Restaurant ID']].groupby(['City']).count().sort_values(by=['Restaurant ID'], ascending=False).reset_index().iat[0,0]
        case 4:
            # 4. Qual o nome da cidade que possui o maior valor médio de um prato para dois?
            return df.loc[:,['City','Average Cost for two']].groupby(['City']).max().sort_values(by=['Average Cost for two'], ascending=False).reset_index().iat[0,0]
        case 5:
            # 5. Qual o nome da cidade que possui a maior quantidade de tipos de culinária distintas?
            return df.loc[:,['City','Cuisines']].groupby('City').nunique().sort_values(by='Cuisines', ascending=False).reset_index().iat[0,0]
        case 6:
            # 6. Qual o nome da cidade que possui a maior quantidade de restaurantes que fazem reservas?
            return df.loc[df['Has Table booking'] == 1,['City','Restaurant ID']].groupby('City').count().sort_values(by='Restaurant ID', ascending=False).reset_index().iat[0,0]
        case 7:
            # 7. Qual o nome da cidade que possui a maior quantidade de restaurantes que fazem entregas
            return df.loc[df['Is delivering now'] == 1,['Restaurant ID','City']].groupby(['City']).count().sort_values(by=['Restaurant ID'], ascending=False).reset_index().iat[0,0]
        case 8:
            # 8. Qual o nome da cidade que possui a maior quantidade de restaurantes que aceitam pedidos online?
            return df.loc[df['Has Online delivery'] == 1,['Restaurant ID','City']].groupby(['City']).count().sort_values(by=['Restaurant ID'], ascending=False).reset_index().iat[0,0]

def restaurantes(opt):
    match opt:
        case 1:
            # 1. Qual o nome do restaurante que possui a maior quantidade de avaliações?
            return df.loc[:,['Restaurant Name','Votes']].groupby(['Restaurant Name']).sum().sort_values(by='Votes', ascending=False).reset_index().iat[0,0]
        case 2:
            # 2. Qual o nome do restaurante com a maior nota média?
            return df.loc[:,['Restaurant ID','Restaurant Name','Aggregate rating']].groupby(['Restaurant Name','Restaurant ID']).max().sort_values(by=['Aggregate rating','Restaurant ID'], ascending=[False,True]).reset_index().iat[0,0]
        case 3:
            # 3. Qual o nome do restaurante que possui o maior valor de uma prato para duas pessoas?
            return df.loc[:,['Restaurant Name','Average Cost for two']].groupby(['Restaurant Name']).max().sort_values(by=['Average Cost for two'], ascending=False).reset_index().iat[0,0]
        case 4:
            # 4. Qual o nome do restaurante de tipo de culinária brasileira que possui a menor média de avaliação?
            return df.loc[df['Cuisines'] == 'Brazilian',['Restaurant Name','Aggregate rating','Restaurant ID']].groupby(['Restaurant Name','Restaurant ID']).mean().sort_values(by=['Aggregate rating','Restaurant ID']).reset_index().iat[0,0]
        case 5:
            # 5. Qual o nome do restaurante de tipo de culinária brasileira, e que é do Brasil, que possui a maior média de avaliação?
            return df.loc[(df['Cuisines'] == 'Brazilian') & (df['Country Name'] == 'Brazil'),['Restaurant Name','Aggregate rating','Restaurant ID']].groupby(['Restaurant Name','Restaurant ID']).mean().sort_values(by=['Aggregate rating','Restaurant ID'], ascending=[False,True]).reset_index().iat[0,0]
        case 6:
            # 6. Os restaurantes que aceitam pedido online são também, na média, os restaurantes que mais possuem avaliações registradas?
            return np.round(df.loc[:,['Has Online delivery','Votes']].groupby(['Has Online delivery']).mean().reset_index().sort_values(by='Votes', ascending=False),2)
        case 7:
            # 7. Os restaurantes que fazem reservas são também, na média, os restaurantes que possuem o maior valor médio de um prato para duas pessoas?
            return np.round(df.loc[:,['Has Table booking','Average Cost for two']].groupby(['Has Table booking']).mean().reset_index().sort_values(by='Average Cost for two', ascending=False),2)
        case 8:
            # 8. Os restaurantes do tipo de culinária japonesa dos Estados Unidos da América possuem um valor médio de prato para duas pessoas maior que as churrascarias americanas (BBQ)?
            jp = np.round(df.loc[(df['Cuisines'] == 'Japanese') & (df['Country Name'] == 'United States of America'),['Average Cost for two']].mean().iat[0],2)
            bbq = np.round(df.loc[(df['Cuisines'] == 'BBQ') & (df['Country Name'] == 'United States of America'),['Average Cost for two']].mean().iat[0],2)
            res = namedtuple("Result", ['jp','bbq'])
            return res(jp,bbq)

def culinaria(opt):
    match opt:
        case 1:
            # 1. Dos restaurantes que possuem o tipo de culinária italiana, qual o nome do restaurante com a maior média de avaliação?
            return df.loc[df['Cuisines'] == 'Italian',['Restaurant ID','Restaurant Name','Aggregate rating']].groupby(['Restaurant Name','Restaurant ID']).max().sort_values(by=['Aggregate rating','Restaurant ID'], ascending=[False,True]).reset_index().iat[0,0]
        case 2:
            # 2. Dos restaurantes que possuem o tipo de culinária italiana, qual o nome do restaurante com a menor média de avaliação?
            return df.loc[df['Cuisines'] == 'Italian',['Restaurant ID','Restaurant Name','Aggregate rating']].groupby(['Restaurant Name','Restaurant ID']).min().sort_values(by=['Aggregate rating','Restaurant ID']).reset_index().iat[0,0]
        case 3:
            # 3. Dos restaurantes que possuem o tipo de culinária americana, qual o nome do restaurante com a maior média de avaliação?
            return df.loc[df['Cuisines'] == 'American',['Restaurant ID','Restaurant Name','Aggregate rating']].groupby(['Restaurant Name','Restaurant ID']).max().sort_values(by=['Aggregate rating','Restaurant ID'], ascending=[False,True]).reset_index().iat[0,0]
        case 4:
            # 4. Dos restaurantes que possuem o tipo de culinária americana, qual o nome do restaurante com a menor média de avaliação?
            return df.loc[df['Cuisines'] == 'American',['Restaurant Name','Aggregate rating']].groupby(['Restaurant Name']).min().sort_values(by=['Aggregate rating']).reset_index().iat[0,0]
        case 5:
            # 5. Dos restaurantes que possuem o tipo de culinária árabe, qual o nome do restaurante com a maior média de avaliação?
            return df.loc[df['Cuisines'] == 'Arabian',['Restaurant Name','Aggregate rating']].groupby(['Restaurant Name']).max().sort_values(by=['Aggregate rating'], ascending=[False]).reset_index().iat[0,0]
        case 6:
            # 6. Dos restaurantes que possuem o tipo de culinária árabe, qual o nome do restaurante com a menor média de avaliação?
            return df.loc[df['Cuisines'] == 'Arabian',['Restaurant Name','Aggregate rating']].groupby(['Restaurant Name']).min().sort_values(by=['Aggregate rating']).reset_index().iat[0,0]
        case 7:
            # 7. Dos restaurantes que possuem o tipo de culinária japonesa, qual o nome do restaurante com a maior média de avaliação?
            return df.loc[df['Cuisines'] == 'Japanese',['Restaurant ID','Restaurant Name','Aggregate rating']].groupby(['Restaurant Name','Restaurant ID']).max().sort_values(by=['Aggregate rating','Restaurant ID'], ascending=[False,True]).reset_index().iat[0,0]
        case 8:
            # 8. Dos restaurantes que possuem o tipo de culinária japonesa, qual o nome do restaurante com a menor média de avaliação?
            return df.loc[df['Cuisines'] == 'Japanese',['Restaurant Name','Aggregate rating']].groupby(['Restaurant Name']).min().sort_values(by=['Aggregate rating']).reset_index().iat[0,0]
        case 9:
            # 9. Dos restaurantes que possuem o tipo de culinária caseira, qual o nome do restaurante com a maior média de avaliação?
            return df.loc[df['Cuisines'] == 'Home-made',['Restaurant Name','Aggregate rating']].groupby(['Restaurant Name']).max().sort_values(by=['Aggregate rating'], ascending=[False]).reset_index().iat[0,0]
        case 10:
            # 10. Dos restaurantes que possuem o tipo de culinária caseira, qual o nome do restaurante com a menor média de avaliação?
            return df.loc[df['Cuisines'] == 'Home-made',['Restaurant Name','Aggregate rating']].groupby(['Restaurant Name']).max().sort_values(by=['Aggregate rating']).reset_index().iat[0,0]
        case 11:
            # 11. Qual o tipo de culinária que possui o maior valor médio de um prato para duas pessoas?
            return df.loc[:,['Cuisines','Average Cost for two']].groupby(['Cuisines']).max().reset_index().sort_values(by=['Average Cost for two'], ascending=False).iat[0,0]
        case 12:
            # 12. Qual o tipo de culinária que possui a maior nota média?
            return df.loc[:,['Cuisines','Aggregate rating','Restaurant ID']].groupby(['Cuisines','Restaurant ID']).max().reset_index().sort_values(by=['Aggregate rating','Restaurant ID'], ascending=[False,True]).iat[0,0]
        case 13:
            # 13. Qual o tipo de culinária que possui mais restaurantes que aceitam pedidos online e fazem entregas?
            return df.loc[(df['Has Online delivery'] == 1) & (df['Is delivering now'] == 1),['Cuisines','Restaurant ID']].groupby('Cuisines').nunique().reset_index().sort_values(by='Restaurant ID', ascending=False).iat[0,0]
