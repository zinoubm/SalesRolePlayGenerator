import os
from tqdm import tqdm
import re


def get_keywords(script):
    pattern = r"[0-9a-fA-F]{32}\b"  # extract the portion between "quick" and "fox"

    match = re.search(pattern, script)  # search for the pattern in the string

    try:
        id = match.group()  # extract the matching portion

        with open(os.path.join("keywords", f"keyword_{id}.txt"), "r") as file:
            keywords = file.read()

    except Exception as e:
        print(e)

    return keywords


if __name__ == "__main__":
    res = get_keywords("sales_roles_play_0f7b2035b116421182682b6d84b8a8f1.txt")
    print(res)
