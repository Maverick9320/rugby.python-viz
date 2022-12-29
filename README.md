# Rugby Python

The dimensions of both pitch styles are 100x70. The pitches can be plotted onto a matplotlib.pyplot figure or ax with the following code. 
```
import matplotlib.pyplot as plt

plot=plt.figure(figsize=(10, 7))
ax=plot.add_subplot()

x = field()
x.league_pitch(poles=True, pitch_color='white', line_color='black', line_style='-', line_alpha=0.75)  
x.zones()
```
