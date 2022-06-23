import os
import sys
import json
import xml.etree.ElementTree

from termcolor import colored


def main_images():
    """
    Parse the given XML file and find all the tags with attribute TYPE (value:
    image).
    """
    root: xml.etree.ElementTree.Element = parse_xml_file()
    images: tuple = tuple(get_all_images(root, "widget"))
    names: tuple = tuple(get_image_name(images))
    only_images: tuple = tuple(filter_the_files(os.listdir()))
    make_suggestions(names, only_images)


def parse_xml_file() -> xml.etree.ElementTree.Element:
    """
    Find the parse and parse the content.
    """
    tree = xml.etree.ElementTree.parse(sys.argv[1])  # temporarily solution
    return tree.getroot()


def get_all_images(root: xml.etree.ElementTree.Element, tagname: str) -> list:
    """
    Iterate through all tags with the given TAGNAME and attribute TYPE="image".
    """
    return [
        xml_tag
        for xml_tag in root.iter(tagname)
        if xml_tag.get("type") == "image"
    ]


def get_image_name(elements: tuple) -> list:
    """
    Return only the image names.
    """
    return [
        json.loads(image_el.text.strip()).get("src")
        for image_el in elements
    ]


def filter_the_files(all_files: list) -> list:
    """
    Return only the JPG and PNG files.
    """
    return [
        file
        for file in all_files
        if file.endswith(".png") or file.endswith(".jpg")
    ]


def make_suggestions(images: tuple, filetree: tuple) -> None:
    """
    Write sys.stdout if the image exists in the current dir.
    """
    for file in filetree:
        if file in images:
            print(colored(f"CORRECT: '{file}'..", "green"))
        else:
            print(colored(f"REMOVING: '{file}'..", "red"))
