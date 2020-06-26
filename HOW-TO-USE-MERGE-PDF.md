# MERGE-PDF 

## On Windows

### Prerequisites

- One has `python` installed, along with `pip`. The python executable is sometimes named as `py` in Windows.
- One has collected the PDF files into a directory (i.e. folder). In this document, the path is `C:\Users\ahn\pdfs`.
- One has the main script `merge-pdf.py`. in this document, the path is `C:\Users\ahn\merge-pdf.py`.



### Main steps

1. Install the python package `PyPDF2` :

   ``` shell
   pip install pypdf2
   ```

   

2. Open up the Windows default command terminal, e.g.

   `Windows` + `R`

   

3. Change directory (`cd`) to where the collected PDF files:

   ``` shell
   cd C:\Users\ahn\pdfs
   ```

   

4. Run the script with python.

   ``` python
   py C:\Users\ahn\merge-pdf.py
   ```

   

5. Then we get the merged PDF file with name : `merged.pdf` in the same directory of the main script: `C:\Users\ahn`.



### Some technical details

- If one uses a `virtualenv` or `venv`, to install the required package like `PyPDF2`, let's be sure whether one have entered that virtual environment.
- If you did not added your path to the python executable `py` to your `PATH` environment variable, then use absolute path to the python executable, when running the main script.

