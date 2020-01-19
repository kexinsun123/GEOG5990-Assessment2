import matplotlib.pyplot as plt 
import numpy as np 
import random
import pandas as pd
import warnings
warnings.filterwarnings("ignore")


class WayHome():
    def __init__(self, if_goback=False):
        # load town map
        self.town = pd.read_csv('./drunk.plan', header=None)
        self.if_goback = if_goback
        self.base_data()
        self.plot_town(if_save=True, title='town map')
        self.help_alldrunk()
    def plot_town(self, if_drunk=False, if_drunkP=False, if_save=False, title=''):
        # plot map of town
        plt.figure(figsize=(7, 7))
        for num in self.nums:
            if num != 0:
                _ = self.spots[self.spots['num']==num]
                plt.scatter(_['x'], _['y'], color=tuple(self.colors.loc[num]), label=num)
        if if_drunk:
            plt.scatter([self.drunk_pos[0]], [self.drunk_pos[1]], marker='<', color=tuple(self.colors.loc[self.drunk_num]))
        if if_drunkP:
            for num in self.drunkD:
                p = self.drunkD[num]
                for j, (net1, net2) in enumerate(zip(p[:-1], p[1:])):
                    plt.plot([net1[0], net2[0]], [net1[1], net2[1]], color=tuple(self.colors.loc[self.drunk_num]))
        plt.title(title, fontsize=20)
        plt.legend(bbox_to_anchor=(1.15, 1), fontsize=10)
        plt.xlim(0, 300)
        plt.ylim(0, 300)
        plt.xlabel('Y')
        plt.ylabel('X')
        if if_save:
            plt.savefig('town_map.png', dpi=500)
        plt.show()
        plt.close()
    def base_data(self):
        # all spots
        self.spots = self.town.stack().reset_index()
        self.spots.columns = ['x', 'y', 'num']
        # pub spots
        self.spots_pub = self.spots[self.spots['num']==1]
        # random direction,  left/right/up/down         
        self.dirD = {
                'left': np.array((-1, 0)),
                'right': np.array((1, 0)),
                'up': np.array((0, 1)),
                'down': np.array((0, -1)),
                }
        # drunk numbers
        self.drunkS = set(range(1, 26))
        # density map
        self.density_map = pd.DataFrame(0, index=self.town.index, columns=self.town.columns)
        # numbers of drunk, pub, background
        self.nums = self.spots['num'].drop_duplicates().sort_values().tolist()
        # color of numbers
        self.colors = pd.DataFrame(np.random.sample((27, 3)), index=self.nums)
        # path of all drunks
        self.drunkD = {}
    def random_move(self):
        return self.dirD[random.sample(['left', 'right', 'up', 'down'], 1)[0]]
    def random_num(self):
        # for each drunk (who will have numbers between 10 and 250 assigned before leaving the pub)
        newdrunk_num = random.sample(self.drunkS, 1)[0]
        self.drunkS = self.drunkS - set([newdrunk_num])
        return newdrunk_num
    def leave_pub(self):
        # Random selection of a boundary point of pub
        x, y = self.spots_pub.iloc[np.random.randint(0, len(self.spots_pub), 1)[0]][['x', 'y']]
        spot_ = np.array([x, y])
        move_dir = self.random_move()
        # Randomly enter town from some point of pub
        while True:
            spot_ += move_dir
            num = self.town.loc[spot_[0], spot_[1]]
            if num == 0:
                break
        # mark the position, number, path of this drunk
        self.drunk_pos = spot_
        self.drunk_num = self.random_num() * 10
        self.drunk_path = [self.drunk_pos]
    def help_onedrunk(self):
        # a new drunk leave the pub
        self.leave_pub()
        i = 0
        last_move = np.array([0, 0])
        while True:
            _move = self.random_move()
            _ = self.drunk_pos + _move
            # make sure that next move is in the boundary
            # if Stopping the drunks from retracing their steps, then new move is not contract to the last move
            if self.if_goback:
                cond = _[0] < 0 or _[1] < 0 or _[0] >= 300 or _[1] >= 300 or \
                        (last_move[0] + _move[0] == 0 and last_move[1] + _move[1] == 0)
            else:
                cond = _[0] < 0 or _[1] < 0 or _[0] >= 300 or _[1] >= 300
            if cond:
                continue
            else:
                next_num = self.town.loc[_[0], _[1]] 
                if next_num == self.drunk_num:
                    #  When the drunk hits the correctly numbered house, stop the process
                    self.plot_town(if_drunk=True, title='_%10d'%i)
                    self.density_map.loc[_[0], _[1]] += 1
                    self.drunk_path.append(_)
                    self.drunkD[self.drunk_num] = self.drunk_path
                    print('number %02d drunk use %d steps to go home'% (self.drunk_num, len(self.drunk_path)))
                    print('left drunks: ', np.array(list(self.drunkS)) *10)
                    # save the density map
                    self.density_map.to_csv('density_map.txt', index=None, header=None, sep=',')
                    break
                elif next_num == 0:
                    self.drunk_pos = _
                    self.density_map.loc[_[0], _[1]] += 1
                    self.drunk_path.append(_)
                    last_move = _move
                    i += 1
                else:
                    #  if the drunk doesnt hits correctly numbered house, continue
                    continue
                if i % 1000 == 0:
                    self.plot_town(if_drunk=True, title='number %03d drunk, step %08d'%(self.drunk_num, i))
    def help_alldrunk(self):
        # loop to help all 25 drunks go home
        while True:
            if len(self.drunkS) == 0:
                break
            self.help_onedrunk()

# if_goback = True, Stopping the drunks from retracing their steps
WayHome(if_goback=False)


