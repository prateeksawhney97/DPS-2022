# DPS-2022

## AI Mission For the DPS Program

The code, plots and heroku webapp lineked to this repository provides a method to visualise and predict historically the number of accidents per category and to forecast the values for the future. The method is applied to a data set which contains the monthly values for traffic accidents in Munich until the end of 2020. Forecasting from the Heroku Web Application can be done for each 3 distinct Accident Category i.e. Alcohol, Traffic and Escape.

The Link Of The Heroku Web Application is -> https://accidentdps.herokuapp.com/

Home Page which shows 3 sections for the user to navigate & predict the forecast of accidents for 2021 for each of the 3 categories:

<img width="1440" alt="Screenshot 2022-02-21 at 9 57 45 AM" src="https://user-images.githubusercontent.com/34116562/154889258-69d053a6-5b7e-4106-86e1-93950042cf8f.png">

For example, for the alcohol accidents, the user can enter the month number between 1 and 12 and can click on predict: 

<img width="1440" alt="Screenshot 2022-02-21 at 9 57 52 AM" src="https://user-images.githubusercontent.com/34116562/154889263-d292f79f-6a7a-4413-80e6-ffbdfa47f403.png">

The Result i.e. the number of accidents for the specific category can be seen on the result page & the user can now navigate back to the Home Page for more Predictions: 

<img width="1440" alt="Screenshot 2022-02-21 at 9 57 58 AM" src="https://user-images.githubusercontent.com/34116562/154889264-9f5ff666-b4e9-45d7-ad2a-8ab5d49c9e03.png">

The data set "Monatszahlen Verkehrsunfälle" which can be downloaded from the below link and contains the following topics:
(https://www.opengov-muenchen.de/dataset/monatszahlen-verkehrsunfaelle/resource/40094bd6-f82d-4979-949b-26c8dc00b9a7)

1. Traffic accidents
2. Escape accidents
3. Alcohol accidents

The Models which are used by the web application are developed using Meta's Prophet ML Model (https://facebook.github.io/prophet/docs/quick_start.html#python-api). 
There are 3 distinct models whose source code and development can be found in the "AccidentPrediction.ipynb". I have also included all the 3 forecast models in the repository.

1. Traffic accidents -> forecast_model_traffic.bin
2. Escape accidents -> forecast_model_escape.bin
3. Alcohol accidents -> forecast_model.bin

#### Visualization Using Meta Prophet:

1. For alcohol accidents Forecast :

![alcohol-accidents](https://user-images.githubusercontent.com/34116562/154888954-f781ffb8-ab5e-4c6a-aab1-e919bdf52d47.png)

2. For escape accidents Forecast :

![escape-accidents](https://user-images.githubusercontent.com/34116562/154888959-1950018f-0ac4-4d1f-939f-3a5458185b9e.png)

3. For traffic accidents Forecast :

![traffic-accidents](https://user-images.githubusercontent.com/34116562/154888969-187fc2ce-2cea-476e-8fc0-69d031d9e065.png)


4. Accidents category visualization :

![plot1](https://user-images.githubusercontent.com/34116562/154888975-5a895710-a4fb-441f-bb2f-06cb419c2b16.png)
 
![plot2](https://user-images.githubusercontent.com/34116562/154888985-91ed7450-af92-4189-bf57-5fd4b276c3d1.png)

5. Number of accidents per category :

![plot5](https://user-images.githubusercontent.com/34116562/154888991-1d2387a5-e1d8-4204-a8d1-a7c05a1df59a.png)

6. Number of accidents per accident type :

![plot6](https://user-images.githubusercontent.com/34116562/154888996-a8ed8b61-e43e-4ebf-9652-7e713f1483ef.png)

#### Another Approach:

