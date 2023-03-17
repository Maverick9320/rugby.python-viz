# 🏉 Rugby Python
[![Python](https://img.shields.io/badge/python-blue.svg)](https://www.python.org/downloads/release/python-360/)
[![Jupyter](https://img.shields.io/badge/jupyter-lab-orange.svg)](https://www.python.org/downloads/release/python-360/)
[![JupyterNbook](https://img.shields.io/badge/jupyter-notebook-orange.svg)](https://www.python.org/downloads/release/python-360/)

This package is used in conjunction with matplotlib to make it easy to plot field lines for both rugby union and rugby league pitches. There are plans for functionality to include adding zones and kick plotting. 

``` This project is a WIP and more stuff will be added through 2023 to offer more functionality. ``` 

## ⏬ Installation

This pip package is obsolete and deprecated. It will soon be updated. 

To install the old package you can use: ``` pip install Rugby ```

## 🛠️ Functionality
#### Field Dimensions: *100x70*
```
import matplotlib.pyplot as plt

plot=plt.figure(figsize=(10, 7))
ax=plot.add_subplot()

x = field()
x.league_pitch(poles=True, pitch_color='white', line_color='black', line_style='-', line_alpha=0.75)  
x.zones()
```
