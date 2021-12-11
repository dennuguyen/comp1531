"""
Converts json and yaml files.

Running json_yaml.py in the command line requires one .json and one.yaml
arguments in the order 'in file' and 'out file'. If the 'out file' does not
exist then one will be created.

json2yaml and yaml2json functions take textIOwrappers as parameters and allows
import of the functions for external use.
"""
import sys
import json
import yaml


def json2yaml(_in_file, _out_file):
    """
    Takes textIOwrappers as parameters and converts .json to .yaml
    """
    yaml.dump(yaml.load(json.dumps(json.loads(_in_file.read()))),
              open(_out_file.name, "w"),
              default_flow_style=False)


def yaml2json(_in_file, _out_file):
    """
    Takes textIOwrappers as parameters and converts .yaml to .json
    """
    json.dump(yaml.load(_in_file), open(_out_file.name, "w"))


if __name__ == '__main__':
    # Assert the number of files
    assert len(sys.argv) == 3, "Incorrect number of files"

    # Assert the correct filetypes
    _IN, _OUT = sys.argv[1].lower(), sys.argv[2].lower()
    assert ((_IN.endswith(".json") and _OUT.endswith(".yaml"))
            or (_IN.endswith(".yaml") and _OUT.endswith(".json")))

    # "with" is safe to open "_IN_FILE" as it raises FileNotFoundError
    with open(sys.argv[1], "r") as _IN_FILE:
        # Check if _OUT_FILE exists. If not, handle Exception and create a file
        try:
            _OUT_FILE = open(sys.argv[2], "r")
            _OUT_FILE.close()
        except FileNotFoundError:
            _OUT_FILE = open(sys.argv[2], "w")
            print(f"Creating new file: '{sys.argv[2]}'")

        # If arg order .json, .yaml. Converts .json file to .yaml file
        if _IN_FILE.name.lower().endswith(".json"):
            json2yaml(_IN_FILE, _OUT_FILE)

        # If arg order .yaml, .json. Converts .yaml file to .json file
        if _IN_FILE.name.lower().endswith(".yaml"):
            yaml2json(_IN_FILE, _OUT_FILE)
