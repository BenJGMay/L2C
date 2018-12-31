def next_gen:():
    global grid_model
    for i in range (0, height):
        for j in range (0, width):
            cell = 0
            count = count_neighbours(grid_model, i, j)
            if grid_model[i][j] == 0:
                if count == 3:
                    cell = 1
            elif grid_model[i][j] == 1:
                if count == 2 or count == 3:
                    cell = 1
