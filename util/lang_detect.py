from langdetect import detect, LangDetectException
import unicodedata
import math


def is_meaning_str(
    text,
    languages=["en", "es", "fr", "de", "vi", "zh-tw", "zh-cn", "tl"],
    min_length=5,
    entropy_threshold=4,
):
    # Remove whitespace and punctuation, keep unicode characters
    cleaned_text = "".join(
        ch for ch in text if not unicodedata.category(ch).startswith("P")
    )
    cleaned_text = "".join(cleaned_text.split())

    # Check if the text is too short
    if len(cleaned_text) < min_length:
        return False

    # Try to detect the language
    try:
        detected_lang = detect(text)
        if detected_lang in languages:
            return True
    except LangDetectException:
        pass  # Language detection failed, continue with entropy check

    # Calculate entropy
    char_freq = {}
    for char in cleaned_text:
        char_freq[char] = char_freq.get(char, 0) + 1

    entropy = 0
    for freq in char_freq.values():
        prob = freq / len(cleaned_text)
        entropy -= prob * math.log2(prob)

    # If entropy is below the threshold, consider it random
    return entropy > entropy_threshold
