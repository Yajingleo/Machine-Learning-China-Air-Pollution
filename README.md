# Machine-Learning-Project-China-Air-Pollution
This hub is for a UCLA machine learning Math 285J course project on China air pollution PM 2.5, including research references, data sources, and a list of our codes and results. 

Nowadays, China air pollution is a pressing issue in the China society, since it might be the cause of the recent dramastic inceases of lung cancers.

##Background reading:
- [Fine particulate matter (PM2.5) in China at a city level](http://www.nature.com/articles/srep14884)
- [PM2.5 in China: Measurements, sources, visibility and health effects, and mitigation](http://www.sciencedirect.com/science/article/pii/S1674200113002228)
- [Spatiotemporal variations of PM2.5 and PM10 concentrations between 31 Chinese cities and their relationships with SO2, NO2, CO and O3](https://www.researchgate.net/profile/Bin_Zhao/publication/275257816_Spatiotemporal_variations_of_PM25_and_PM10_concentrations_between_31_Chinese_cities_and_their_relationships_with_SO2_NO2_CO_and_O3/links/554086f30cf2736761c27c70.pdf)
- Other studies in Chinese: [1](http://www.sescn.org.cn/zyxx/2015dxsjmgs/sdj/C04.pdf), [2](https://www.google.com/url?sa=t&rct=j&q=&esrc=s&source=web&cd=1&cad=rja&uact=8&ved=0ahUKEwjQjMCw7a3MAhVC3mMKHTAGBiMQFggcMAA&url=http%3A%2F%2Fmanu36.magtech.com.cn%2FJweb_zghjkx%2FCN%2Farticle%2FdownloadArticleFile.do%3FattachType%3DPDF%26id%3D14294&usg=AFQjCNHpNgg7ZM9_cyHokQATSYgWKXhvSw&sig2=geHoF0Fy4G_h9hKag5GrZQ&bvm=bv.120853415,d.cGc)

## Machine Learning research on pollution prediction
- [Evolving the neural network model for forecasting air pollution time series](http://www.sciencedirect.com/science/article/pii/S0952197604000119)
- [Intercomparison of air quality data using principal component analysis, and forecasting of PM10 and PM2.5 concentrations using artificial neural networks](http://www.sciencedirect.com/science/article/pii/S0048969711000052)
- [Machine learning in geosciences and remote sensing](http://www.sciencedirect.com/science/article/pii/S1674987115000821)

## Data Source on weather and pollution
- [Weather data on NOAA](http://www7.ncdc.noaa.gov/CDO/cdoselect.cmd?datasetabbv=GSOD&countryabbv=&georegionabbv=)
- Air pollution data sources: [1] (http://aqi.cga.harvard.edu/china/), [2] (https://dataverse.harvard.edu/dataset.xhtml?persistentId=doi:10.7910/DVN/24826)

## Model Assumptions 
After plotting the time series at various stations in Beijing, there is a clear intraday seasonality, every 8 hours there is a peak of pollution. However, no significant short-term trends are identified. Based on these observations, the following are assumed:
- The PM 2.5 pollutants index is driven by the previous 8 hours weather conditions and the pollution status. 

## Model Formulation
Suppose the time series for different pollutants are denoted by *P_i(t)*, where *i* denotes the i-th pollutant and t denotes the time in hour. Suppose the time series for different weather conditions such as wind speed, temperature, humidity, and air pressure, are denoted by *W_j(t)*. 

Then,  
    *PM2.5(t) = F(PM2.5(t-8), P_1(t-8), ..., P_n(t-8), W_1(t-8), ..., W_m(t-8))*
    
The project is going to learn *F* using various machine learning methods, linear models (Lasso, Ridge), Random Forest, Extra-Trees, and Neural Networks. 

## Codes
- [This](https://github.com/Yajingleo/Machine-Learning-China-Air-Pollution/blob/master/Codes/DataPrep.sql) is a SQL codes for preprocessing data. 
- [This](https://github.com/Yajingleo/Machine-Learning-China-Air-Pollution/blob/master/Codes/FeedForwardNeuralNetwork.py) is a python codes for vanilla nerual networks of arbitrary number of layers, using mini-batch SGD.
- [This](https://github.com/Yajingleo/Machine-Learning-China-Air-Pollution/blob/master/Codes/LinearModels.py) is a python codes for model selections among various methods, Ridge, Lasso, Random Forest, Extra-Tree, and M-regression.

