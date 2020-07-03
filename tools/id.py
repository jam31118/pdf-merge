from os.path import isdir, splitext, join, isfile, basename
from os import listdir
import re
import numpy as np

# test_dir_path = r"C:\Users\ahn\Desktop\archive\2020-general-physics-1\class-1-c-assignment-13-and-14-test"
test_dir_path = "."
assert isdir(test_dir_path)


#############################


def seems_pdf(file_name):
    _file_extension = splitext(file_name)[-1]
    _seems_pdf = _file_extension.lower() == '.pdf'
    return _seems_pdf

total_contents_path = [join(test_dir_path, name) for name in listdir(test_dir_path)]
pdf_file_paths = [pdf_path for pdf_path in total_contents_path if seems_pdf(pdf_path) and isfile(pdf_path)]
pdf_file_names = [basename(pdf_path) for pdf_path in pdf_file_paths]


#############################


pattern = re.compile(".*([0-9][0-9][0-9][0-9][0-9][0-9][0-9][0-9]).*")

stud_id_list = []

for pdf_file_name in pdf_file_names:
    mobj = re.search(pattern, pdf_file_name)
    
    id_match = None
    if mobj:
        num_of_match = (mobj.lastindex + 1) - 1
        if num_of_match == 1: 
            id_match_str = mobj.group(1)
            id_match = int(id_match_str)
        else: raise Exception("Uexpected")
    else:
        print("[ LOG ] The student ID cannot be extracted from file: '{:s}'".format(pdf_file_name))
    stud_id_list.append(id_match)

stud_id_arr = np.asarray(stud_id_list)


###########################


has_None_among_id = (stud_id_arr == None).sum() > 0

if has_None_among_id:
    print("[ERROR] There one or more PDF file(s) from which the student ID could not be extracted.")
    exit()
else: print("[ LOG ] The student ID could be extracted from all PDF files.", end='\n\n')

    
###########################    
    
    
unique_val, indices, counts = np.unique(stud_id_list, return_counts=True, return_index=True)

duplicate_values = stud_id_arr[indices[counts > 1]]
print("[ LOG ] The list of student ID with multiple files - - - - START")
for dup_val in duplicate_values:
    print(dup_val)
print("[ LOG ] The list of student ID with multiple files - - - - END")
