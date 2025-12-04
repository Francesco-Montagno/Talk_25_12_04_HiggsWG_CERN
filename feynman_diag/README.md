 # 1 - Generate PDF file for the diagrams

 To generate the PDF file containing all the Feynman diagrams, run the following command in your terminal:
 
 ```
pdflatex filename.tex
 ```

 # 2 - Convert PDF to PNG images

 To convert the generated PDF file to PNG images, you can use the `pdftoppm` command-line tool. Run the following command in your terminal:

 ```
pdftoppm -png -r 300 filename.pdf outputname
 ```