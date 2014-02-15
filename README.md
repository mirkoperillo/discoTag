discoTag
========

This is a easy python script to extract a set of instances of a given TAG from a file.

DEPENDENCIES
---

this script uses xmllint to format the result.

USAGE
---

Sample:

	python discoTag.py --file <INPUT_FILE> --tag div

Options:
- --file: path of input file (mandatory)
- --tag: name of the tag to discover  (mandatory)
- --startdoc: first istance of tag to extract (default 0)
- --lastdoc: last instance of tag to extract (default 50)
- --output: path of file where save results (default input file name'.extract')
- --pretty: format the output (it uses xmllint)
- -h --help: to view options


