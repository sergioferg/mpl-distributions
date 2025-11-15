import matplotlib.pyplot as plt
import numpy as np
from scipy.special import factorial

def poisson_pmf(x, lda):
    return (np.exp(-lda)*lda**x)/factorial(x)

def getarrays_pmf(lda):
    x_arr = np.linspace(0, 150, 151)
    start = 0
    last = 150
    for x in x_arr:
        if(poisson_pmf(x, lda)<10**-3):
            start += 1
        else:
            break
    for i in range(start+1, last):
        if(poisson_pmf(x_arr[i], lda)<10**-3):
            last = i
            break
    x_lins = np.linspace(start, last, last-start+1)
    y_lins = poisson_pmf(x_lins, lda)
    return x_lins, y_lins

def generate_poisson(lda):
    x_4, y_4 = getarrays_pmf(lda)

    max_y = np.max(y_4)

    fig_4 = plt.figure(figsize=(6,4))
    axes_4 = fig_4.add_axes([0,0,1,1])
    axes_4.set_xlabel('x')
    axes_4.set_ylabel('p(x)')
    axes_4.set_title(f'$Poisson(\lambda ={lda})$')
    axes_4.bar(x_4, y_4, width=.45, color='k',zorder=2)

    y_ticks = np.linspace(0, round(max_y*1.1, 1), 6)  # Create 6 evenly spaced ticks from 0 to max_y
    axes_4.set_yticks(y_ticks)
    axes_4.grid(axis='y', color='0.7', dashes=(5,2,1,2), zorder=0)

    fig_4.savefig('images/poisson.svg', bbox_inches='tight')
    plt.close(fig_4)
    
lda = float(input())
generate_poisson(lda)