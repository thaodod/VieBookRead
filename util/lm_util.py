from openai import OpenAI
from count_token import count_words
from thefuzz import fuzz

client = OpenAI(
    api_key="***REMOVED***",
)


def yes_no(answer):
    if answer.lower().startswith("yes"):
        return True
    else:
        return False


def is_relevant(ref, query, score):
    if count_words(query) >= 7 and score >= 86:
        return True

    if count_words(query) >= 10 and score >= 80:
        return True

    if count_words(query) >= 20 and score >= 75:
        return True

    if count_words(query) <= 4 and score < 80:
        return False

    prompt = f"""
    Given a retrieved html content as below:
    {ref}

    Then providing a text generated by imperfect OCR tool; important: it might have typo or mis-recognized characters; as below:
    <input-text>
    {query}
    </input-text>

    Check if the input text is relevant (yes) or not within the given retrieved content.
    Answer briefly (yes or no) without any explanations or formatting.
    """

    answer = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {
                "role": "system",
                "content": "Assist user to evaluate search result relevance",
            },
            {"role": "user", "content": prompt},
        ],
        temperature=0.0,
    )

    return yes_no(answer.choices[0].message.content)


def str_gap(origin, mod):
    gap_c = len(mod.strip()) / len(origin.strip())
    gap_w = abs(count_words(mod) - count_words(origin))
    sim = fuzz.ratio(origin.strip().lower(), mod.strip().lower())
    return gap_c, gap_w, sim
