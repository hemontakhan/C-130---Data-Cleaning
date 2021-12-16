import pandas as pd

data = pd.read_csv('StarBook.csv')

del data['Luminosity']
del data['Ecc.']

data = data.rename({
    'Luminosity' : 'Brightness'
})

data.to_csv('StarData.csv')