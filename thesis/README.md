A book or thesis consists of the following files:
1. pre_command.tex: where you define shortcuts or commands to be used 
2. preamble.tex: sets the document type (report, book), packages used.
3. main.tex: this is the main tex file for your thesis/book.
4. chapter*.tex: each tex file for each chapter
5. appendix1.tex: for appendix

How to compile?

First time, you need to type the following command in a terminal:

pdflatex -ini -jobname="preamble" "&pdflatex preamble.tex\dump"

Then, open the main.tex with your favorite LaTeX editor, and compile it similar to what you have done for articles.

Whenever you have modified the file 'preamble.tex' (to add a new chapter for example), you have to execute the above command.
You can compile your thesis/book from any tex file (for example, chapter1.tex) following the instruction of your LaTeX editor. Note that at the beginning of all tex files, I added:

%!TEX root = main.tex

This is the way of Sublime Text, so that you can compile the book/thesis from any tex file (not just the main.tex). 