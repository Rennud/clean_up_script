import os
import json
import xml.etree.ElementTree

from termcolor import colored


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


def filter_the_image_files(all_files: list) -> list:
    """
    Return only the JPG and PNG files.
    """
    return [
        file
        for file in all_files
        if file.endswith(".png") or file.endswith(".jpg")
    ]


def delete_unused_images(images: tuple, filetree: tuple):
    """
    If image is not used(is in file tree but isn't in list of used images) delete the image.
    """
    for image in filetree:
        if image not in images:
            print(colored(image + " deleting...", "red"))
            os.remove(image)

    # ?It's necessary to have a return here? If yes how to build a function properly
