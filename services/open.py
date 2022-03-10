import os.path
import constant
import xmlschema


def open_file():
    return xmlschema.XMLSchema(constant.FILESDIR + '/xsd-schema.xsd')
