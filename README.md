# GEOG5990-Assessment2
This repository is for assessment 2 of the course GEOG5990.

**List of files**
This is README, including drunk.txt file, density.txt file and drunk.py file.

**Software**
The python file (drunk.py) is finished and tested in "Spyder".

**Running steps**
1.Click "Run file(F5)" on the top of the main window.
2.Note that the Bakend of Graphics is "Inline", which can be found on the top of the window(Tools-References-Ipython console-Graphics-Backend-Inline).

**Running outputs**
1.When reading in data, the background with 26 points: the one in the middle of the map represents the pub while other 25 points represent homes of the drunks, so there are 25 drunks in need to find their homes. Then each drunk will be given the number (10, 20, ... 250) and arranged in random orders to leave the pub and move to their homes. The first map called "The Route of Drunks" is shown under Console 1/A window, but it makes some changes based on the original background, which shows 25 routes in total to represent moving traces of all drunks from the pub to their homes.  
3.After that, the second map called "The Density of Route" is shown under Console 1/A window, which records the frequency that drunks pass through each point: the lighter color represents high density.

**Kown issues**
As there are some repeated parts(high density) of different routes, so mapping all routes for all drunks makes the map busy and unclear in visual effect. 

**Test**
The code "plt.imshow(density)" makes the density of route be shown on the environment of drunk.txt. When it runs, the density map and the route map have the same background, so it proves that the data in drunk.txt has been pulled in.

**Roadmap**
For more concise and beautiful outputs, it is important to make an animation to show how drunks find their homes step by step, which is more continuous to show the moving process.

**License**
See the [MIT LICENSE](https://github.com/kexinsun123/GEOG5990-Assessment2/blob/master/LICENSE) here.
