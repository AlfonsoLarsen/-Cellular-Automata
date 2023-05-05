import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Grid Size
n = 200

# Grid Initialization
grid = np.zeros((n, n))

# Randomly assign values to some cells in the grid
for i in range(n):
    for j in range(n):
        if np.random.random() < 0.3:
            grid[i, j] = 1

# Cellular Automaton Rules Definition
def update(frameNum, img, grid, n):
    newGrid = np.zeros((n, n))
    for i in range(n):
        for j in range(n):
            # Count the number of live neighbors
            neighbors = (
                grid[(i-1)%n, (j-1)%n] + grid[(i-1)%n, j%n] + grid[(i-1)%n, (j+1)%n] +
                grid[i%n, (j-1)%n] + grid[i%n, (j+1)%n] +
                grid[(i+1)%n, (j-1)%n] + grid[(i+1)%n, j%n] + grid[(i+1)%n, (j+1)%n]
            )
            # Apply rules
            if grid[i, j] == 1:
                if neighbors < 2 or neighbors > 3:
                    newGrid[i, j] = 0
                else:
                    newGrid[i, j] = 1
            else:
                if neighbors == 3:
                    newGrid[i, j] = 1
                else:
                    newGrid[i, j] = 0
    # Update the grid
    img.set_data(newGrid)
    grid[:] = newGrid[:]
    return img,

# Animation Creation
fig, ax = plt.subplots()
img = ax.imshow(grid, interpolation='nearest', cmap='viridis')
ani = animation.FuncAnimation(fig, update, fargs=(img, grid, n), frames=100, interval=50, save_count=50)

plt.show()
