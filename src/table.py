import matplotlib.pyplot as plt
import numpy as np
import pandas

from matplotlib.table import Table

def main():
    data = pandas.DataFrame(np.random.random((12,8)))
                #columns=['A','B','C','D','E','F','G','H'])
    #checkerboard_table(data)
    plt.show()

def checkerboard_table(data, frame, fmt='{:.2f}', bkg_colors=['yellow', 'white', 'red']):
    fig, ax = plt.subplots()
    ax.set_axis_off()
    tb = Table(ax, bbox=[0,0,1,1])

    nrows, ncols = data.shape
    width, height = 1.0 / ncols, 1.0 / nrows

    maximum = max(max(frame))

    # Add cells
    for (i,j), val in np.ndenumerate(data):
        # Index either the first or second item of bkg_colors based on
        # a checker board pattern
        if val == 0:
            color = bkg_colors[0]
        else:
            color = bkg_colors[1]
        if i == j:
            color = bkg_colors[1]

        tb.add_cell(i, j, width, height, text=fmt.format(frame[i][j]), 
                    loc='center', facecolor=color)

    # Row Labels...
    for i, label in enumerate(data.index+1):
        tb.add_cell(i, -1, width, height, text=label, loc='right', 
                    edgecolor='none', facecolor='none')
    # Column Labels...
    for j, label in enumerate(data.columns+1):
        tb.add_cell(-1, j, width, height/2, text=label, loc='center', 
                           edgecolor='none', facecolor='none')
    ax.add_table(tb)
    return fig

if __name__ == '__main__':
    main()
