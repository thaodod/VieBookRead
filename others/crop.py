from thefuzz import fuzz
import re


def custom_split(input_string):
    # Trim spaces from both ends
    trimmed_string = input_string.strip()

    # Replace multiple spaces with a single space
    single_spaced_string = re.sub(r"\s+", " ", trimmed_string)

    # Split only by spaces but keep punctuation attached to words
    words = re.findall(r"\S+|\n", single_spaced_string)

    return words


def find_best_match(short_seq, long_seq):
    short_words = custom_split(short_seq)
    long_words = custom_split(long_seq)
    short_len = len(short_words)
    long_len = len(long_words)

    best_ratio = 0
    best_start = 0
    best_end = short_len

    # Slide a window of size similar to short_seq over long_seq
    for i in range(long_len - short_len + 1):
        end = i + short_len
        candidate = " ".join(long_words[i:end])
        ratio = max(
            fuzz.ratio(short_seq, candidate),
            fuzz.ratio(short_seq.lower(), candidate.lower()),
        )

        if ratio > best_ratio:
            best_ratio = ratio
            best_start = i
            best_end = end

    # Extend the match if possible while maintaining or improving the ratio
    while best_start > 0:
        extended = " ".join(long_words[best_start - 1 : best_end])
        new_ratio = max(
            fuzz.ratio(short_seq, extended),
            fuzz.ratio(short_seq.lower(), extended.lower()),
        )
        if new_ratio >= best_ratio:
            best_start -= 1
            best_ratio = new_ratio
        else:
            break

    while best_end < long_len:
        extended = " ".join(long_words[best_start : best_end + 1])
        new_ratio = max(
            fuzz.ratio(short_seq, extended),
            fuzz.ratio(short_seq.lower(), extended.lower()),
        )
        if new_ratio >= best_ratio:
            best_end += 1
            best_ratio = new_ratio
        else:
            break

    best_match = " ".join(long_words[best_start:best_end])
    if best_ratio == 0:
        best_ratio = max(
            fuzz.ratio(short_seq, best_match),
            fuzz.ratio(short_seq.lower(), best_match.lower()),
        )
    return best_match, best_ratio


# # Example usage
# short_seq = "qulck bruwn fox jnnps"
# long_seq = (
#     "head padding here. The quick brown fox jumps over the lazy dog. tail padding"
# )

# best_match, score = find_best_match_region(short_seq, long_seq)
# print(f"Best matching region: '{best_match}'")
# print(f"Similarity score: {score}")
