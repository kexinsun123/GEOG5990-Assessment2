# GEOG5990-Assessment2
This repository is for assessment 2 of the course GEOG5990.

**List of files**
This is README, including drunk.txt file, density.txt file, drunk.py file and two images that respectively show the route of drunks and the density of route.

**Software**
The python file (drunk.py) is finished and tested in "Spyder".

**Running steps**
1.Click "Run file(F5)" on the top of the main window.
2.Note that the Bakend of Graphics is "Inline", which can be found on the top of the window(Tools-References-Ipython console-Graphics-Backend-Inline).

**Running outputs**
1.When the model runs, Console 1/A window firstly originally shows a town map with 26 small rectangles: the one in the middle of the map represents the pub while other 25 rectangles represent homes of the drunks, so there are 25 drunks in need to find their homes.
2.Based on the previous map, each drunk will be given the number (10, 20, ... 250) and arranged in random orders to leave the pub. The map called "The Route of Drunks" shows 25 routes in total to represent moving traces of all drunks from the pub to their homes.
3.After that, the map called "The Density of Route" shows the frequency that drunks pass through each point: the lighter color represents high density.

**Kown issues**
As there are some repeated parts of different routes, so mapping all routes for all drunks makes the map busy and unclear in visual effect. 

**Test**
The model can run regularly to show the town map and step maps and when it finishes the second one with random number begins immediately, which means the loop is valid.

**Roadmap**
For more concise and beautiful outputs, it is important to make an animation to show how one drunk find the home step by step, which is more continuous to show the moving process.

**License**
See the [MIT LICENSE](https://github.com/kexinsun123/GEOG5990-Assessment2/blob/master/LICENSE) here.
