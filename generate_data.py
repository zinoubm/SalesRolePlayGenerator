import openai
import itertools
from tqdm import tqdm
from uuid import uuid4


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


INDUSTRIES = [
    "Energy",
    "Healthcare",
    "Technology",
    "Hospitality",
    "Agriculture",
    "Education",
    "Government",
    "Professional Services",
    "Media and Entertainment",
    "Real Estate",
]

PERSONAS = [
    "Young Professional",
    "Senior Citizen",
    "College Student",
    "Single Parent",
    "Working Parent",
    "Stay-at-home Parent",
    "Business Owner",
    "Business Executive",
    "Entrepreneur",
    "High-end Consumer",
]

SENARIOS = [
    "Responding to customer inquiries about product features",
    "Troubleshooting technical issues for customers",
    "Assisting customers with product returns",
    "Answering customer questions about pricing",
    "Processing customer orders",
    "Resolving customer complaints",
    "Addressing customer concerns about delivery times",
    "Explaining product warranties to customers",
    "Upselling additional products or services",
    "Providing product demonstrations to customers",
]


if __name__ == "__main__":

    openai.api_key = "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"

    base_prompt = (
        "Generate a Sales Role Play script for a <<INDUSTRY>> Company. The flow should start with a cold call "
        " and include multiple scenarios that the sales rep may encounter during the call. The scenarios can be introduced "
        "in the middle of the discussion, and the sales rep should handle them appropriately. The call should involve speaking "
        "with a <<PERSONA>>, and the sales rep should aim to connect with the person in charge of <<SENARIO>> at the "
        "company."
        "\n\n"
        "Script: "
    )

    combinations = list(itertools.product(INDUSTRIES, PERSONAS, SENARIOS))

    for industry, persona, senario in tqdm(combinations[216:]):

        prompt = (
            base_prompt.replace("<<INDUSTRY>>", industry)
            .replace("<<PERSONA>>", persona)
            .replace("<<SENARIO>>", senario)
        )

        script = get_completion(prompt, max_tokens=1028, temperature=0.7)
        try:
            with open(f"data/sales_roles_play_{uuid4().hex}.txt", "w") as file:
                file.write(script)

        except Exception as e:
            print(e)
