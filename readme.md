This repository contains LaTeX sources and Python scripts described in the following paper

How to effortlessly write a high quality scientific paper in the field of computational engineering and sciences
by Vinh Phu Nguyen, Stephane Bordas and Alban de Vaucorbeil

The Python scripts are in folder 'scripts' where there are scripts to generate high-quality vector images for 2D graphs.
Modify them accordingly to your needs (e.g. you need to change the data file used in these scripts).

To help those new to LaTeX, in what follows, we present how to set up LaTeX using macOS and Linux.

macOS machines:

1. Install macTeX: http://www.tug.org/mactex/ 
2. It comes with TexShop--a LaTeX editor, so you can start using LaTeX immediately.
3. To get the pdf of the mentioned-above paper, open TexShop (in folder /Applications/TeX/), press Command T, and you're done. Press Enter when you see the progress in the console stops (this is because we inserted the command \showthe\textwidth to get the document width).

That's it.


LinuX machines:

1. Install Tex Live: sudo apt-get install texlive-full
2. Install a Tex editor, for example, TexMaker: sudo apt-get install texmaker
3. How to use TexMaker: https://www.xm1math.net/texmaker/

Please refer to folder /thesis for an example on how to write a thesis or a book using LaTeX.

