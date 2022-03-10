from pprint import pprint

from xml.etree import ElementTree

import constant
from services.open import open_file
import xmlschema


def main():
    xsd_file = open_file()
    xml = [] # new xml varible
    tree = ElementTree.ElementTree()
    cheque = ElementTree.Element("Cheque")
    # TODO: get all types from xsd-schema in dict

    for a in xsd_file.elements["Cheque"].attrib.items():
        # TODO: match attributes with dict & write ti this or new dict
        print(a)

    # TODO: create nesting on checque -> item
    item = ElementTree.Element("Bottle")
    # TODO: add nessesary attrinbutes in dict & write new file

    a.attrib["name"] = "1"  # adding attributes
    cheque.append(item)
    tree._setroot(cheque)  # like this
    tree.write(constant.FILESDIR + "/output.xml")


if __name__ == '__main__':
    main()
