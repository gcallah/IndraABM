
"""
This script takes an Indra ABM model as input and outputs a notebook.
It writes stdout.
"""

import sys


DOCSTRING_TXT = "A short description about this model."


def read_docstring(curr_line, mdl_lines):
    content = ""
    start_line = curr_line
    
    # Find first """
    while not mdl_lines[start_line].startswith('"""'):
        start_line += 1
    
    # Find second """
    curr_line = start_line + 1
    while not mdl_lines[curr_line].startswith('"""'):
        curr_line += 1
    
    # Concat content
    curr_line += 1
    for line in range(start_line, curr_line):
        content += mdl_lines[line]

    return (curr_line, content.strip())


IMPORT_TXT = "We import all necessary modules and functions from other files."


def read_imports(curr_line, mdl_lines):
    content = ""
    
    while not mdl_lines[curr_line].startswith("from ") \
            and not mdl_lines[curr_line].startswith("import "):
        curr_line += 1

    while mdl_lines[curr_line].startswith("from ") \
            or mdl_lines[curr_line].startswith("import "):
        content += mdl_lines[curr_line]
        curr_line += 1

    return (curr_line, content.strip())


CONSTANT_TXT = "These are the constants and global variables we used in this model."


def read_constants(curr_line, mdl_lines):
    content = ""

    while not mdl_lines[curr_line].startswith("def "):
        content += mdl_lines[curr_line]
        curr_line += 1

    return (curr_line, content.strip())


ACTIONS_CREATORS_TXT = "The following functions define some actions that our agents can make."


def read_actions_creators(curr_line, mdl_lines):
    content = ""

    while not mdl_lines[curr_line].endswith("_grps = {\n"):
        content += mdl_lines[curr_line]
        curr_line += 1

    return (curr_line, content.strip())


GRP_STRUCT_TXT = "This structure defines the groups that characterize our agents."


def read_grp_struct(curr_line, mdl_lines):
    content = ""

    while not mdl_lines[curr_line].startswith("class "):
        content += mdl_lines[curr_line]
        curr_line += 1

    return (curr_line, content.strip())


MODEL_CLASS_TXT = "We subclass `Model` to create our own variant of it."


def read_model_class(curr_line, mdl_lines):
    content = ""

    while not mdl_lines[curr_line].startswith("def create_model"):
        content += mdl_lines[curr_line]
        curr_line += 1

    return (curr_line, content.strip())


CREATE_MODEL_TXT = "Here's where we create the model class."


def read_create_model(curr_line, mdl_lines):
    content = ""

    while not mdl_lines[curr_line].startswith("def main"):
        content += mdl_lines[curr_line]
        curr_line += 1

    return (curr_line, content.strip())


MAIN_TXT = "The main function runs the whole model."


def read_main(curr_line, mdl_lines):
    content = ""

    while not mdl_lines[curr_line].startswith("if __name__"):
        content += mdl_lines[curr_line]
        curr_line += 1

    return (curr_line, content.strip())


NB_STRUCT = [
    {"text": DOCSTRING_TXT, "func": read_docstring},
    {"text": IMPORT_TXT, "func": read_imports},
    {"text": CONSTANT_TXT, "func": read_constants},
    {"text": ACTIONS_CREATORS_TXT, "func": read_actions_creators},
    {"text": GRP_STRUCT_TXT, "func": read_grp_struct},
    {"text": MODEL_CLASS_TXT, "func": read_model_class},
    {"text": CREATE_MODEL_TXT, "func": read_create_model},
    {"text": MAIN_TXT, "func": read_main},
]


def output_md_cell(text):
    print("*********\n", text)


def output_code_cell(code):
    print(code, "\n")


def main():
    if len(sys.argv) != 2:
        print("Usage: PROG [input file]")
        exit(1)
    
    mdl_path = sys.argv[1]
    try:
        infile = open(mdl_path)
        mdl_lines = infile.readlines()
    except:
        print("Unable to handle the given file.")
        exit(1)
    finally:
        infile.close()
    
    curr_line = 0
    for section in NB_STRUCT:
        output_md_cell(section["text"])
        (curr_line, code) = section["func"](curr_line, mdl_lines)
        output_code_cell(code)


if __name__ == "__main__":
    main()
