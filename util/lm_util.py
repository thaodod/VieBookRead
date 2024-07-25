from openai import OpenAI

client = OpenAI(
    api_key="***REMOVED***",
)


def yes_no(answer):
    if answer.lower().startswith("yes"):
        return True
    else:
        return False


def is_relevant(ref, query):
    prompt = f"""
    Given a retrieved html content as below:
    {ref}

    Then providing a text gererated by imperfect OCR tool; important: it might have typo or mis-recognized characters; as below:
    <input-text>
    {query}
    </input-text>

    Check if the input text is relevant (yes) or not (no) within the given retrieved content.
    Answer shortly (yes or no) without any explanations, formatting.
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
