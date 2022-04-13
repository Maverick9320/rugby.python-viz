# RugbyPython
Latest version 0.0.6

pip install RugbyPython --upgrade

---------------------

Functions to make it easy to plot and record rugby analytics.

To use these functions you will have to have python installed and the following packages: Matplotlib, Pandas.

---------------------
You can install this package with the following steps:
Windows: 

1 ~ Open a command prompt, either in anaconda or your usual python command prompt. 

2 ~ Type in: 'pip install RugbyPython'

3 ~ Pip will then automatically install the package where it needs to go.

4 ~ Open a py script and import the package with: 'from RugbyPython import *'

5 ~ Matplotlib may be installed automatically or you may have it installed already. If you don't have it install it with: 'pip install matplotlib'

---------------------

All functions:

-pitch(ax='ax', pitchcolor = 'white', linecolor='Black', poles=False, linestyle='--', labels=False, labelalpha=0.5, shadows=False, linealpha=0.2)
-vertpitch(ax='ax', pitchcolor = 'white', linecolor='Black', poles=False, linestyle='--', labels=False, labelalpha=0.5, shadows=False, linealpha=0.2)
-leaguepitch(ax='ax', pitchcolor = 'white', linecolor='Black', poles=False, linestyle='--', labels=False, labelalpha=0.5, shadows=False, linealpha=0.2)
-zones(data, ax, alpha=0.5, paint1 = '#0384fc', paint2 = '#FF4F3F', legend=False)
-badge(ax='ax', img='none', alpha=1, zorder=99)
