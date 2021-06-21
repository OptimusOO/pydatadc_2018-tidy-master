import pandas as pd
from pandas.io.clipboards import read_clipboard
from pandas.io.parsers import read_csv

df= pd.read_csv('../data/gapminder.tsv',sep='\t')

df.columns

df.index
df.values
type(df)

df.shape

df.info()


df['country']

country_df=df['country']

print(df.head())
subset=df[['country','year','continent']]
print(subset.head())

# get all rows with specified cols
df.loc[:,['year']]

# get filterd rows with specified cols
df.loc[df['year']==1967,['country','year','continent']]

# get filterd rows with specified cols
df.loc[(df['year']==1967)&(df['pop']>=1_000_000),['pop','year','continent']]

df= pd.read_csv('../data/pew.csv')
print(df.head())

df.melt(id_vars='religion',var_name='Spending Range',value_name='count')

billboard= pd.read_csv('../data/billboard.csv')
print(billboard.head())

billboard_melt=billboard.melt(id_vars=['year','artist','track','time','date.entered'],var_name='Week',value_name='count')

billboard_melt.head()

print(billboard.shape)



print(billboard_melt.shape)

ebola=pd.read_csv('../data/country_timeseries.csv')
print(ebola.head())

ebola_melt=ebola.melt(id_vars=['Date','Day'])
print(ebola_melt.head())
print(type(ebola_melt['variable'].str.split('_')))

# split column values
ebola_melt['status']=ebola_melt['variable'].str.split('_').str.get(0)
ebola_melt['conutry']=ebola_melt['variable'].str.split('_').str.get(1)
print(ebola_melt.head())

ebola_melt[['status','conutry']]=ebola_melt['variable'].str.split('_',expand=True)
print(ebola_melt.head())

weather=pd.read_csv('../data/weather.csv')
weather_melt=weather.melt(id_vars=['id','year','month',	'element'],var_name='day')
weather_tidy=weather_melt.pivot_table(index=['id','year','month','day'],columns='element',values='value')
type(weather_tidy)
weather_tidy.reset_index()

billboard_melt.head()

billboard_song=billboard_melt[['year','artist','track','time']]
billboard_song.loc[billboard_song['track']=='Loser']
billboard_song=billboard_song.drop_duplicates()

print(billboard_melt.shape)
print(billboard_song.shape)

billboard_song['id']=range(len(billboard_song))
billboard_song.head()

billboard_song.to_csv('../data/billboard_song.csv',index=False)

billboard_rating=billboard_melt.merge(
    billboard_song,how='left',on=['year','artist','track','time']
)

billboard_rating=billboard_rating[['id','date.entered','Week','count']]
billboard_rating.drop_duplicates()
billboard_rating.to_csv('../data/billboard_rating.csv',index=False)

billboard_melt.info()
billboard_song.info()
billboard_rating.info()

print(ebola.head())

print(ebola['Date'].max())
print(ebola['Date'].min())
print(ebola.info())


ebola_melt['Date']=pd.to_datetime(ebola_melt['Date'], format="%m/%d/%Y")

print(ebola_melt.head())

print(ebola_melt.groupby([ebola_melt['Date'].dt.year,'status'])['Day'].sum())
