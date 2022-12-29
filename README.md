# 🏉 Rugby Python
This package is used in conjunction with matplotlib to make it easy to plot field lines for both rugby union and rugby league pitches. There are plans for functionality to include adding zones and kick plotting. 

## ⏬ Installation

``` pip install Rugby ```

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
