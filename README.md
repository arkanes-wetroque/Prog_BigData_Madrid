# Project BIG DATA - Group PELEGRINO

This project is an analyze of different open datas about comune of Madrid.
* Analyzes of the Solar Panels (1)
* Analyzes of Energies used by the comune of Madrid (2)
* Analyzes of the consomation and production by the comune of Madrid (3)


### Dependencies 
*We are still working of the project so at the moment we only put the main librairies used (Everything will be translated in spanish before the end of the project*
* Pandas
* Dash
* dash_bootstrap_components 
* dash_core_components
* Numpy
* plotly
* pathlib
* plotly.express

- [x] Importing Datas and pre-traitement into DATAFRAMES
- [x] Ceation of the main functions
- [x] Setting web app shower DASH
- [ ] Main analyses for 1, 2, 3
- [ ] Searching for next analyses


### Organisation
*May change before the end*
The jupyter notbooks aren't the final processing way but only tests.

* main.py : is the starter of app, then only need to browse in a browser.
* datas_.py : are the processing files with functions of getters.
* pages_.py : are the seperate div files for each screens.
* Datas/ : contains all the CSV Files and some PDF about stuctures.
* assets/ : contains the css for the project (based on the shared one from dash).

### Starting
Make sure to have all dependencies
```
pip install -r requierements.txt
Dash is running on http://127.0.0.1:8050/

```
### If the requierements doesn't work, you can install the lib
### manually on ur env:
- pip install dash
- pip install dash-bootstrap-components
- pip install openpyxl
```
python3 main.py
Dash is running on http://127.0.0.1:8050/

```


## Here some screenshots of few charts and tables of the project


![alt text](https://github.com/ArK4nes/Prog_BigData_Dilhan/blob/main/Datas/C1.png?raw=true)
![alt text](https://github.com/ArK4nes/Prog_BigData_Dilhan/blob/main/Datas/C2.png?raw=true)
