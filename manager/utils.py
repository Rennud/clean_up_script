import xml.etree.ElementTree
import os
import click

from images import get_all_images, get_image_name, filter_the_image_files, delete_unused_images
from exercises import get_exercise_name_and_path, filter_the_exercise_files, delete_unused_exercises

from termcolor import colored


@click.command()
# Which XML we want to parse
@click.argument('xml_file', type=str, required=True)
# s show desired files, d delete desired files
@click.argument('option', type=str, required=True)
# png for images, src for exercises
@click.argument('specified_file', type=str, required=True)
# ?Bad name?
def main_parser(xml_file: str, option: str, specified_file: str):
    """
    Parse the given XML file and find all the tags with attribute TYPE (value:
    image).
    """
    root: xml.etree.ElementTree.Element = parse_xml_file(xml_file)

    # Specific for handling images
    if specified_file == "png":
        images: tuple = tuple(get_all_images(root, "widget"))
        image_names: tuple = tuple(get_image_name(images))
        all_image_files: tuple = tuple(filter_the_image_files(os.listdir()))
        if option == "s":
            print("INFO: Checking the available pictures...")
            make_suggestions(image_names, all_image_files)
        elif option == "d":
            print("INFO: Removing the redundant pictures...")
            delete_unused_images(image_names, all_image_files)
    # Specific for handling exercises
    elif specified_file == "src":
        exercise_names_and_paths: dict = get_exercise_name_and_path(
            root, "solution")
        all_exercise_folders: dict = filter_the_exercise_files()
        if option == "s":
            print("INFO: Checking the available exercises...")
            make_suggestions(exercise_names_and_paths.keys(),
                             all_exercise_folders.keys())
        elif option == "d":
            print("INFO: Removing the redundant exercises...")
            delete_unused_exercises(
                exercise_names_and_paths, all_exercise_folders)


def parse_xml_file(xml_file: str) -> xml.etree.ElementTree.Element:
    """
    Parse the given xml file - xml file all needed information about academy
    """
    tree = xml.etree.ElementTree.parse(xml_file)
    return tree.getroot()


def make_suggestions(used_files: tuple, filetree: tuple) -> None:
    """
    Write sys.stdout if the file exists in the current dir.
    Function works on images and on exercises as well depends on given arguments
    """
    for file in filetree:
        if file in used_files:
            print(colored(f"CORRECT: '{file}'..", "green"))
        else:
            print(colored(f"TO REMOVE: '{file}'..", "red"))


if __name__ == "__main__":
    main_parser()
