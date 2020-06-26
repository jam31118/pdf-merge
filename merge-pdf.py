
## Configuration
from datetime import datetime
merge_pdf_file_name = "merged_{:s}.pdf".format(datetime.now().strftime("%Y%m%d-%H%M"))
sort_file_list = True
strict_mode = False

## Determine directory
home_dir = '.'

from os.path import isdir
assert isdir(home_dir)


## Get PDF file list
from os import listdir
file_name_list = listdir(home_dir)

if merge_pdf_file_name in file_name_list:
    file_name_list.remove(merge_pdf_file_name)

if sort_file_list:
    file_name_list.sort()

pdf_file_paths = []
excluded_file_names = []
from os.path import splitext, join
for file_name in file_name_list:
    file_extension = splitext(file_name)[-1]
    if file_extension.lower() == '.pdf':
        file_path = join(home_dir, file_name)
        pdf_file_paths.append(file_path)
    else: excluded_file_names.append(file_name)


print("[ LOG ] Following pdf files will be merged: ", end='\n\n')
for pdf_file_index, pdf_file_path in enumerate(pdf_file_paths):
    print("[{0:02d}] {1}".format(pdf_file_index+1, pdf_file_path))
print("")

pdf_files = [open(pdf_file_path, "rb") for pdf_file_path in pdf_file_paths]


## Merge PDF files
from PyPDF2 import PdfFileMerger
merger = PdfFileMerger(strict=strict_mode)
#for pdf_file_path in pdf_file_paths:
for pdf_file, pdf_file_path in zip(pdf_files, pdf_file_paths):
    print("Merging: {0} . . . ".format(pdf_file_path), end='', flush=True)
    merger.append(pdf_file)
    print("done", flush=True)


try: merger.write(merge_pdf_file_name)
except: raise Exception("[ERROR] PDF Merge Failed.")

print("")
print("[ LOG ] If the Merge has been succeeded, the merged PDF file name is : '{:s}'".format(merge_pdf_file_name))

for pdf_file in pdf_files: pdf_file.close()

print("[ LOG ] The number of merged PDF files: {:d}".format(len(pdf_files)))
print("[ LOG ] The following files are excluded from the merge: ", end='\n\n')
print(excluded_file_names)
