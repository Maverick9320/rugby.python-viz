## **Functions**:

### *union_pitch()*

```
from Rugby import field
import matplotlib.pyplot as plt

plot=plt.figure(figsize=(10, 7))
ax=plot.add_subplot()

x = field()
x.union_pitch(pitch_color = 'white', line_color = 'Black', poles = False, linestyle = '-', line_alpha=1)
```

![image](https://user-images.githubusercontent.com/99112649/209979622-14bdba74-2b6d-4ba9-b92c-a2c4659f0a00.png)


### *league_pitch()*

```
from Rugby import field
import matplotlib.pyplot as plt

plot=plt.figure(figsize=(10, 7))
ax=plot.add_subplot()

x = field()
x.league_pitch(pitch_color = 'white', line_color = 'Black', poles = False, linestyle = '-', line_alpha=1)
```
![image](https://user-images.githubusercontent.com/99112649/209979786-39f25c05-5089-4348-acb2-1d16d925d7d4.png)
