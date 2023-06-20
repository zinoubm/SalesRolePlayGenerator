import os
import re
from tqdm import tqdm
import jsonlines


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

    path = "data"
    scripts = os.listdir(path)

    with jsonlines.open("fine_tuning_data.jsonl", mode="w") as writer:
        for script in tqdm(scripts):
            try:
                with open(os.path.join("data", script), "r") as file:
                    script_content = file.read()

                keywords = get_keywords(script)

                if keywords and script_content:
                    example = {
                        "prompt": f"{keywords.strip()} ->",
                        "completion": f" {script_content.strip()} ###",
                    }

                    writer.write(example)

            except Exception as e:
                print(e)
