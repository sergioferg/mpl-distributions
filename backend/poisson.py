import io
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

def generate_poisson_svg(lda):
    x_4, y_4 = getarrays_pmf(lda)

    fig_4 = plt.figure(figsize=(6,4))
    axes_4 = fig_4.add_axes([0,0,1,1])
    axes_4.set_xlabel('x')
    axes_4.set_ylabel('p(x)')
    axes_4.set_title(f'$Poisson(\lambda ={lda})$')
    axes_4.bar(x_4, y_4, width=.45, color='k')

    buf = io.BytesIO()
    fig_4.savefig(buf, format='svg', bbox_inches='tight')
    plt.close(fig_4)
    buf.seek(0)
    svg_text = buf.getvalue().decode('utf-8')
    buf.close()
    return svg_text