import os
from shutil import rmtree
import xml.etree.ElementTree

from termcolor import colored


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
