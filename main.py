from pprint import pprint

from xml.etree import ElementTree

import constant
from services.open import open_file
import xmlschema


def main():
    xsd_file = open_file()
    xml = []
    tree = ElementTree.ElementTree()
    cheque = ElementTree.Element("Cheque")
    for a in xsd_file.elements["Cheque"].attrib.items():
        # match attr.type:
        #     case "load":
        #         load()
        #     case "save":
        #         save()
        #     case _:
        #         default()
        # cheque.attrib[attr] =
        print(a)

    item = ElementTree.Element("Bottle")
    # a.attrib["name"] = "1"
    cheque.append(item)
    tree._setroot(cheque)
    tree.write(constant.FILESDIR + "/output.xml")
    # pprint(dict(xsd_file.types))


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    main()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
