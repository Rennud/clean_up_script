import os
import json
from shutil import rmtree
import xml.etree.ElementTree

from termcolor import colored

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
        if option == "-s":
            print("INFO: Checking the available pictures...")
            make_suggestions(image_names, all_image_files)
        elif option == "-d":
            print("INFO: Removing the redundant pictures...")
            delete_unused_images(image_names, all_image_files)
    # Specific for handling exercises
    elif specified_file == "src":
        exercise_names_and_paths: dict = get_exercise_name_and_path(root, "solution")
        all_exercise_folders: dict = filter_the_exercise_files()
        if option == "-s":
            print("INFO: Checking the available exercises...")
            make_suggestions(exercise_names_and_paths.keys(), all_exercise_folders.keys())
        elif option == "-d":
            print("INFO: Removing the redundant exercises...")
            delete_unused_exercises(exercise_names_and_paths, all_exercise_folders)


def parse_xml_file(xml_file: str) -> xml.etree.ElementTree.Element:
    """
    Parse the given xml file - xml file all needed information about academy
    """
    tree = xml.etree.ElementTree.parse(xml_file)
    return tree.getroot()


# <---- Functions needed for handling IMAGES ----> START

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

# <---- Functions needed for handling IMAGES ----> END


# <---- Functions needed for handling EXERCISES ----> START

def get_exercise_name_and_path(root: xml.etree.ElementTree.Element, tagname: str) -> dict:
    """
    Return dict with keys as exercise names and values as exercise paths.
    Contains only exercises that are in use. 
    Key:value pair is needed for delete function 
    """
    exercise_names_paths: dict = {}

    for xml_tag in root.iter(tagname):
        exercise_name = xml_tag.get("sourceDir").split("/", 3)[2]
        exercise_path = xml_tag.get("sourceDir").replace("/solution", '')
        exercise_names_paths[exercise_name] = exercise_path

    return exercise_names_paths


def filter_the_exercise_files() -> dict:
    """
    Return dict with keys as exercise names and values as exercise paths.
    Contains all exercises.
    Key:value pair is needed for delete function 
    """
    all_exercise_names_and_paths: dict = {}

    path_to_exercises_dir = os.getcwd() + "/exercises"
    
    for lesson_dir in os.listdir(path_to_exercises_dir):
        lesson_paths = os.path.join(path_to_exercises_dir, lesson_dir)
        for exercise_folder in os.listdir(lesson_paths):
            # Relative path looks like = exercises/L05/count_numbers
            exercise_path = f"{lesson_paths.split('/', 6)[6]}/{exercise_folder}"
            all_exercise_names_and_paths[exercise_folder] = exercise_path
    
    return all_exercise_names_and_paths


def delete_unused_exercises(in_use_exercises: tuple, all_exercises: tuple):
    """
    If exercise is not used(is in file tree of all exercises but isn't in list of used exercises) delete the exercise recursively.
    Delete whole folder with everything in it 
    """
    for folder in all_exercises:
        if folder not in in_use_exercises.keys():
            print(colored(folder + " deleting...", "red"))
            rmtree(all_exercises[folder])

    # ?It's necessary to have a return here? If yes how to build a function properly

# <---- Functions needed for handling EXERCISES ----> END


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



