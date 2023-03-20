import pandas as pd
import numpy as np
import panel as pn 
pn.extension('tabulator')
import hvplot.pandas

df = pd.readcsv('httpes://raw.githubusercontent.com/') #NEEDS UPDATING

df.columns

df[df['country'] =='World']


df = df.fillna(0)
df['gdp_per_capita'] = np.where(df['population']!=0, df['gdp'] / df['population'], 0)
idf = df.interactive()

year_slider = pn.widgets.IntSlider(name='Year slider', start=1750, end=2020. step=5, value=1850)
year_slider

yaxis_co2 = pn.widgets.RadioButtonGroup(
    name='Y axis',
    options=['co2', 'co2_per_capita',],
    button_type='success'
)

continents = ['World', 'Asia', 'Oceania', 'Europe', 'Africa', 'North America', 'Antarctica']

co2_pipeline = (
    idf[
        (idf.year <= year_slider) &
        (idf.country.isin(continents))
    ]
    .groupby(['country', 'year'])
    [yaxis_co2].mean().to_frame()

co2_pipeline

co2_plot = co2_pipeline.hvplot(x = 'year', by='country', y=yaxis_co2, line_width=2, title = 'CO2 emissions by continent')
co2_plot
