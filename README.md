# GEOG5990-Assessment2
This repository is for assessment 2 of the course GEOG5990.

**List of files**
This is README, including drunk.plan file, density file and drunk file.

**Software**
The python file (drunk.py) is finished and tested in "Spyder".

**Running steps**
1.Click "Run file(F5)" on the top of the main window.
2.Note that the Bakend of Graphics is "Inline", which can be found on the top of the window(Tools-References-Ipython console-Graphics-Backend-Inline).

**Running outputs**
1.When the model runs, Console 1/A window firstly shows a town map with 26 small rectangles: the one in the middle of the map represents the pub while other 25 rectangles represent homes of the drunks, SO there are 25 drunks in need to find their homes.
2.After that, each drunk will be given the number (10, 20, ... 250) and arranged in random orders to leave the pub. A moving point is shown on the map with the random direction (left, right, up, down) and each move is recorded on the title. For example, the form of the title to record the moving route is "number 010 drunk, step 00236000".  
3.If the home number is te same as the drunk number, this drunk will successfully find his or her home. Under Console 1/A window, the point stop moving, the title shows the total steps and the text like this: "number 010 drunk use 214670 steps to go home, left drunks: [20 30 ... 250] to show how many steps this drunk uses to go home and how many drunks left.
4.Once the model helps one drunk find his or her home, it means one loop is finished, then the next loop will begin soon.

**Kown issues**
There are two issues. The first one is time consumption: it takes a long time to help one drunk to find the home, not mention to helping all 25 drunks find their homes. The second one is visual effect: there is no need to show each step of the drunk move as a picture, because it will make the Console 1/A window too busy and unclear to show all steps.

**Test**
The model can run regularly to show the town map and step maps and when it finishes the second one with random number begins immediately, which means the loop is valid.

**Roadmap**
For more concise and beautiful outputs, it is important to make an animation to show how one drunk find the home step by step, which is more continuous to show the finding process.

**License**
See the [MIT LICENSE](https://github.com/kexinsun123/GEOG5990-Assessment2/blob/master/LICENSE) here.
