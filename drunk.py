import matplotlib.pyplot as plt
import numpy as np
import random

#Read data.
f = open('drunk.txt')
environment = []
for line in f:
    parsed_line = str.split(line,",")
    rowlist = []
    for data in parsed_line:
        rowlist.append(float(data))
        environment.append(rowlist)
f.close()

def find_house_pub(data):
    house_pos = {}
    drunks = []
    for i in range(0, len(data)):
        for j in range(0, len(data[0])):
            if data[i][j] == 1:
                drunks.append([(i, j)])
            elif data[i][j] != 0:
                #Make sure the distribution of houses.
                if data[i][j] not in house_pos:
                    house_pos[data[i][j]] = [(i, j)]
                else:
                    house_pos[data[i][j]].append((i, j))
    #Match each drunk with a house position.
    drunk_pos = {}
    keys = list(house_pos.keys())
    for index in range(len(keys)):
        drunk_pos[keys[index]] = drunks[index]
    return house_pos, drunk_pos

def drunk_move(pos, target):
    x, y = pos
    home_prob = 0.2 # The proportion that drunks move towards houses.
    options = [(x+1, y), (x-1, y), (x, y+1), (x, y-1)]
    if random.random() <= home_prob:
        options = []
        if x < target[0]:
            # If houses are under their current positions.
            options.append((x+1, y))
        else:
            options.append((x-1, y))
        if y < target[1]:
            # If houses is on the left hand of their current position.
            options.append((x, y+1))
        else:
            options.append((x, y-1))
        return random.choice(options)
    else:
        # Move randomly.
        return random.choice(options)

    
# Get the middle position of houses.
def get_middle_of_house(house):
    x, y = 0, 0
    for pos in house:
        x += pos[0]
        y += pos[1]
    return int(x/len(house)), int(y/len(house))

def main():
    file_data = read_file()
    house_pos, drunk_pos = find_house_pub(file_data)
    # Draw the pub and houses.
    plt.figure()
    plt.title('The Route of Drunks')
    plt.imshow(file_data)
    for value in house_pos.values():
        # Draw the position of houses.
        value = np.array(value)
        plt.scatter(value[:, 1], value[:, 0], c = 'w')
    # Draw the position of pubs.
    value = np.array(list(drunk_pos.values()))
    plt.scatter(value[:, 0 ,1], value[:, 0, 0], c = 'r')
    
    density = np.zeros(file_data.shape)
    # Draw the route map. 
    keys = list(house_pos.keys())
    for key in keys:
        house = house_pos[key]
        target = get_middle_of_house(house)
        drunk = drunk_pos[key]
        current_position = drunk[0]
        while True:
            # The drunk move one step.
            density[current_position[0], current_position[1]] += 1
            current_position = drunk_move(current_position, target)
            drunk.append(current_position)
            # Judge whether the drunk reaches home.
            if current_position in house:
                break
        drunk = np.array(drunk)
        plt.plot(drunk[:, 1], drunk[:, 0])
    # Draw the density map.
    plt.savefig('trace.png')
    plt.figure()
    plt.title("The Density of Route")
    plt.imshow(density)
    plt.savefig('density.png')

    # Save density file.
    with open('density.txt', 'w') as f:
        for i in range(len(density)):
            string = ','.join([str(int(x)) for x in density[i]])
            f.write(string + '\n')


    plt.show()

if __name__ == '__main__':
    main()