
"""
This script takes an Indra ABM model as input and outputs a notebook.
It writes stdout.
"""
import sys


def read_docstring(curr_line, mdl_lines):
    pass


def read_imports(curr_line, mdl_lines):
    pass


def read_constants(curr_line, mdl_lines):
    pass


def read_actions_creators(curr_line, mdl_lines):
    pass


GRP_STRUCT_TXT = "This structure defines the groups that characterize our agents."


def read_grp_struct(curr_line, mdl_lines):
    return (0, "the definition of the group structure goes here!")


MODEL_CLASS_TXT = "We subclass `Model` to create our own variant of it."


def read_model_class(curr_line, mdl_lines):
    return (0, "the definition of the model class goes here!")


CREATE_MODEL_TXT = "Here's where we create the model class."


def read_create_model(curr_line, mdl_lines):
    return (0, "model code goes here!")


MAIN_TXT = "The main function runs the whole model."


def read_main(curr_line, mdl_lines):
    return (0, "def main():\n    pass\n")


NB_STRUCT = [
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
    # handle args -- model file in argv[1]
    curr_line = 0
    mdl_lines = []
    # read mdl_file into mdl_lines
    for section in NB_STRUCT:
        output_md_cell(section["text"])
        (curr_line, code) = section["func"](curr_line, mdl_lines)
        output_code_cell(code)


if __name__ == "__main__":
    main()
