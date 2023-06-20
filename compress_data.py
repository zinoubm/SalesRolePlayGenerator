import openai
import os
from tqdm import tqdm
import time


def get_completion(
    prompt,
    model="text-davinci-003",
    max_tokens=128,
    temperature=0,
):

    response = None
    try:
        response = openai.Completion.create(
            prompt=prompt,
            max_tokens=max_tokens,
            model=model,
            temperature=temperature,
        )["choices"][0]["text"]

    except Exception as err:
        print(f"Sorry, There was a problem \n\n {err}")

    return response


if __name__ == "__main__":

    openai.api_key = "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"

    base_prompt = (
        "Compress the following Script into 2-4 keywords."
        "\n"
        "Script:  <<SCRIPT>>"
        "\n\n"
        "Keywords:"
    )

    path = "data"
    scripts = os.listdir(path)

    for script in tqdm(scripts):

        try:
            with open(os.path.join("data", script), "r") as file:
                script_content = file.read()

            prompt = base_prompt.replace("<<SCRIPT>>", script_content)

            keywords = get_completion(prompt, max_tokens=128, temperature=0.2)

            with open(
                os.path.join("keywords", script.replace("sales_roles_play", "keyword")),
                "w",
            ) as file:
                file.write(keywords)

        except Exception as e:
            time.sleep(2)
            print(e)
