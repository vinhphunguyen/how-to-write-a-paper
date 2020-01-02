import numpy as np
from scipy import math
from numpy.random import random
from scipy.spatial import cKDTree
import matplotlib as mpl
import matplotlib.pyplot as plt
import pylab as pylab
import glob 
import matplotlib.ticker as mtick
import matplotlib.colors as mcol
import time
import argparse
import sys, os 

def set_size(width, fraction=1, subplot=[1, 1]):
    """ Set aesthetic figure dimensions to avoid scaling in latex.

    Parameters
    ----------
    width: float
            Width in pts
    fraction: float
            Fraction of the width which you wish the figure to occupy

    Returns
    -------
    fig_dim: tuple
            Dimensions of figure in inches
    """

    if width == 'elsevier':
        width_pt = 468.
    elif width == 'beamer':
        width_pt = 307.28987
    else:
        width_pt = width

    # Width of figure
    fig_width_pt = width_pt * fraction

    # Convert from pt to inches
    inches_per_pt = 1 / 72.27

    # Golden ratio to set aesthetic figure height
    golden_ratio = 0.75 #(5**.5 - 1) / 2

    # Figure width in inches
    fig_width_in = fig_width_pt * inches_per_pt
    # Figure height in inches
    fig_height_in = fig_width_in * golden_ratio * (subplot[0] / subplot[1])

    fig_dim = (fig_width_in, fig_height_in)

    return fig_dim

parser = argparse.ArgumentParser(description='Plot the evolution of variables.',
                                 add_help=False,
                                 formatter_class=argparse.RawDescriptionHelpFormatter)


parser.add_argument('--quiet', '-q', action='store_const', const=True, default=False,
                    help='do not show plot.')
args = parser.parse_args()

# Using seaborn's style
plt.style.use('seaborn-colorblind') # dark_background, 

nice_fonts = {
        # Use LaTeX to write all text
        "text.usetex": True,
        "pgf.texsystem": "pdflatex",
        "font.family": "serif",
         "font.serif": [],
         "font.sans-serif": [],
         "font.monospace": [],
         "pgf.preamble": [
        # put LaTeX preamble declarations here
        r"\usepackage[utf8x]{inputenc}",
        r"\usepackage[T1]{fontenc}",
        # macros defined here will be available in plots, e.g.:
        r"\newcommand{\vect}[1]{#1}",
        # You can use dummy implementations, since you LaTeX document
        # will render these properly, anyway.
    ],
        # Use 10pt font in plots, to match 10pt font in document
        "axes.labelsize": 10,
        "font.size": 10,
        # Make the legend/label fonts a little smaller
        "legend.fontsize": 8,
        "xtick.labelsize": 8,
        "ytick.labelsize": 8,
}

mpl.use('pgf')
mpl.rcParams.update(nice_fonts)

markersize = 6

#-------- Setup colours
#bgc = [(252./255.)**0.05, (141./255.)**0.05,(98./255.)**0.05]
#colors = brewer2mpl.get_map('Set2', 'qualitative', 8).mpl_colors


#-------------------------------------------------------------
# Dimer 5: Read Data

fnames = ['log.mpm']#, '../cold-spraying-3D/log.mpm']

dat = [pylab.genfromtxt(f,skip_header=1) for f in fnames]

print ('reading files done.')

x=[]
y=[]


fig, (ax1,ax2) = plt.subplots(1, 2, figsize=set_size('elsevier', subplot=[1, 2]))

lw = 1.5
ymax = 0.
xmax = 0.

fac = 0.001 * 1e+9 # to second, then to nano second

for i, f in enumerate(fnames):
    
    if '3D' in f: 
        x = fac*dat[i][:,2]
        y = dat[i][:,3]
        ax1.plot(x, y, color='black', label='3D',linewidth=lw)
        ax2.plot(x, dat[i][:,4], color='black', label='3D',linewidth=lw)
    else:
        x = fac*dat[i][:,2]
        y = dat[i][:,3]
        ax1.plot(x, y, color='red', label='axi-symmetric',linewidth=lw)
        ax2.plot(x, dat[i][:,4], color='red', label='axi-symmetric',linewidth=lw)
   
    xmax = max(xmax, np.max(x))
    ymax = max(ymax, np.max(y))
    #if '460E' in f:
    #    xmax1 = max(xmax1, np.max(x[i]))
    #elif '700E' in f:
    #    xmax2 = max(xmax2, np.max(x[i]))
    #elif '900E' in f:
    #    xmax3 = max(xmax3, np.max(x[i]))

    
ax1.set_xlabel('time [ns]')
ax1.set_ylabel(r'$\varepsilon_p$')

ax2.set_xlabel('time [ns]')
ax2.set_ylabel(r'$T$[K]')

ax1.set_yticks(np.arange(0, 5, 1)) 
ax2.set_yticks(np.arange(0, 601, 150)) 

#ax.set_ylim(1.0, 2.8)
#ax.set_xlim(0, 1.6)

ax1.legend(loc=0)
ax2.legend(loc=0)
plt.tight_layout()
plt.savefig('./cold-spray-plots.pdf', format='pdf',  bbox_inches='tight')
plt.savefig('./cold-spray-plots.pgf', bbox_inches='tight')
command = 'cp ' + 'cold-spray-plots.pdf' + ' /Users/vingu/Dropbox/my-writtings/papers-dropbox/karamelo/figures/'
#os.system( command )

if args.quiet == False:
    plt.show()
