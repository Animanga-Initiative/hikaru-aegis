"""This module contains functions for setting up folders."""

import os
from platform import system

def get_hikaru_root() -> str:
    """
    Get the root directory of hikaruaegis.

    On Windows, it should be %USERPROFILE%\\\\.hikaruaegis, but on POSIX, it should be ~/.hikaruaegis.
    However, on CI/CD (GitHub Actions), it should be current repo directory.

    :return: The path to the root directory.
    :rtype: str
    """
    # check if the program runs on Windows
    if system() == "Windows":
        # get the user profile directory
        user_profile = os.getenv("USERPROFILE")
        # check if the user profile directory exists
        if user_profile:
            # return the path to the root directory
            return os.path.join(user_profile, ".hikaruaegis")
        else:
            # return the path to the root directory
            return os.path.join(os.getcwd(), ".hikaruaegis")
    else:
        if os.getenv("GITHUB_ACTIONS"):
            return os.getcwd()
        else:
            # resolve the home directory
            home = os.path.expanduser("~")
            # return the path to the root directory
            return os.path.join(home, ".hikaruaegis")

def add_directory(*path: str, name: str | None = None) -> str:
    """
    Creates a directory if it doesn't exist.

    :param path: The path(s) to the directory.
    :type path: tuple[str]
    :param name: The name of the directory. Defaults to None.
    :type name: str | None
    :return: Should return the path to the directory.
    :rtype: str
    """
    target = os.path.join(get_hikaru_root(), *path)
    if name:
        print(f"Creating directory for {name} on {target}...")
    else:
        print(f"Creating directory on {target}...")

    if not os.path.exists(target):
        os.makedirs(target)

    if name and not os.path.exists(os.path.join(target, name)):
        os.makedirs(os.path.join(target, name))
        return os.path.join(target, name)
    else:
        return target
