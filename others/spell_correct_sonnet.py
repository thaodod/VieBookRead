from anthropic import AnthropicVertex, APIError
from thefuzz import fuzz
import re

LOCATION = "us-east5"  # or "europe-west4"

client = AnthropicVertex(region=LOCATION, project_id="***REMOVED***")
m_name = "claude-3-5-sonnet@20240620"


def contains_tag(input_string):
    # Define the regex pattern for single-word XML tags with end tags
    pattern = r"<(\w+)>(.*?)</\1>"

    # Search for the pattern in the input string
    match = re.search(pattern, input_string)

    # Return True if a match is found, otherwise False
    return bool(match)


def spell_correct(prompt):
    try:
        message = client.messages.create(
            messages=[
                {
                    "role": "user",
                    "content": prompt,
                },
            ],
            model=m_name,
            max_tokens=2048,
            temperature=0.0,
        )
        return message.content[0].text
    except APIError as e:
        if e.status_code == 429:
            print("Rate limit exceeded. Please wait before making more requests.")
            raise
        elif e.status_code == 402:
            print("Insufficient funds or quota exceeded.")
            raise
        else:
            print(f"API error occurred: {e}")
            raise
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        raise


def correct(text):
    prompt = f"""
Given a sequence as within the tag:
<sequence>{text}</sequence>

The sequence might not be meaningful as characters might be misrecognized by other visually similar characters because it is generated from an OCR process. The sequence content is mainly in Vietnamese, sometimes English or French or Chinese or mixed.
If the sequence is already good or purely random, please answer 'OKAY' shortly!
Otherwise, please make spelling corrections if really needed (just a minimal change),
And answer processed text only without tag or explanations.
"""
    try:
        answer = spell_correct(prompt)
        if answer == "OKAY":
            return False
        elif contains_tag(answer):
            return False
        elif "processed" in answer:
            return False
        elif fuzz.ratio(text, answer) >= 50:
            return answer
        else:
            return False
    except Exception:
        return False
