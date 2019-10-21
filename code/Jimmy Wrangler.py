import pandas as pd
import matplotlib.pyplot as plt
df1 = pd.read_csv('https://raw.githubusercontent.com/armangh67/Jimmy-Wrangler-Data-Explorer/master/datasets/cleaned_generation.csv', low_memory = False)
df2 = pd.read_csv('https://raw.githubusercontent.com/armangh67/Jimmy-Wrangler-Data-Explorer/master/datasets/greenhouse_gas_inventory_data_data.csv', low_memory = False)
df1=df1[df1.Year<=2014]
df2=df2[ (df2.Region == "United Kingdom") & (df2.Year>=2003)&(df2.category == "carbon_dioxide_co2_emissions_without_land_use_land_use_change_and_forestry_lulucf_in_kilotonne_co2_equivalent")]
merged=pd.merge(df1,df2,on=['Year','Region'])
merged['Renewable_energy'] = (merged['Total']/100000)*100
merged['CO2_emission'] = (merged['value']/1000000)*100
merged.plot(x='Year', y=['Renewable_energy','CO2_emission'])
