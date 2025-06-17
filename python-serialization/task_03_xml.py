#!/usr/bin/env python3


"""Module for serializing and deserializing a dictionary to/from XML."""


import xml.etree.ElementTree as ET


def serialize_to_xml(dictionary, filename):
    """Serialize a dictionary to XML and save it to a file."""

    try:

        root = ET.Element("data")


        for key, value in dictionary.items():
            child = ET.SubElement(root, key)
            child.text = str(value)

        tree = ET.ElementTree(root)
        tree.write(filename, encoding="utf-8", xml_declaration=True)

        return True

    except Exception:
        return False

def deserialize_from_xml(filename):

    """Deserialize XML file back into a Python dictionary."""

    try:
        tree = ET.parse(filename)
        root = tree.getroot()


        data = {}
        for child in root:
            data[child.tag] = child.text

        return data

    except Exception:
        return None
