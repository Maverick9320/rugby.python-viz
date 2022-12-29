# Rugby Python

### Installation

``` pip install Rugby ```

### Functionality
#### Field Dimensions: *100x70*
```
import matplotlib.pyplot as plt

plot=plt.figure(figsize=(10, 7))
ax=plot.add_subplot()

x = field()
x.league_pitch(poles=True, pitch_color='white', line_color='black', line_style='-', line_alpha=0.75)  
x.zones()
```
