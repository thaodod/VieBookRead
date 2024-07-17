# using gpt-3.5/ gpt-4o/ haiku 3
# input: 1 para from processed json, 1 html content as reference.
# note: 1 html content must have <html><body> tag around as usual.
from requests import RequestException
from openai import OpenAI, OpenAIError
from anthropic import AnthropicVertex, APIError

claude_client = AnthropicVertex(region="us-central1", project_id="***REMOVED***")

open_client = OpenAI(api_key="***REMOVED***",)

def text_correct(ref_html, para, mode='gpt3'):
    prompt = f"""
    Given an html content as below:
    {ref_html}

    Then I provide a text which needs to be corrected as it is predicted from imperfect OCR tool. Use html content as reference source to correct below input text:
    <input-text>
    {para}
    </input-text>

    Strictly keep the orthography (and punctuation) of the reference, only correct based on what existed on input text carefully.
    First word of the text could also be typo too, check all words and letters carefully equally.
    Answer corrected text, important: Give only the processed result, without any explanations, formatting or XML-like tag.
    """
    
    if mode == 'gpt3' or mode == 'gpt4':
        client = open_client
        m_name = "gpt-3.5-turbo" if mode == 'gpt3' else "gpt-4o"
        
        try:
            response = client.chat.completions.create(
                model=m_name,
                messages=[
                    {"role": "system", "content": "You are an assistant."},
                    {
                        "role": "user",
                        "content": prompt,
                    },
                ],
                temperature=0.0
            )
            return response.choices[0].message.content
        except OpenAIError as e:
            print(f"OpenAI API returned an error: {e}")
            return None

        except RequestException as e:
            print(f"A network error occurred: {e}")
            return None

    elif mode == 'haiku':
        client = claude_client
        m_name = "claude-3-haiku@20240307"

        try:
            message = client.messages.create(
                messages=[
                    {
                    "role": "user",
                    "content": prompt,
                    }
                ],
                model=m_name,
                max_tokens=2048,
                temperature=0.0
            )
            return message.content[0].text
        except APIError as e:
            if e.status_code == 429:
                print("Rate limit exceeded. Please wait before making more requests.")
            elif e.status_code == 402:
                print("Insufficient funds or quota exceeded.")
            else:
                print(f"API error occurred: {e}")
            return None
        except Exception as e:
            print(f"An unexpected error occurred: {e}")
            return None
        
    else:
        raise ValueError("invalid mode, only gpt3 gpt4 or haiku")