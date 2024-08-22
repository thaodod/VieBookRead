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
    # Allow up to 2 non-improving extensions
    start_attempts = 0
    while best_start > 0 and start_attempts < 3:
        if start_attempts == 0:
            extended_start = best_start - 1  # Temporarily extend to the left
        else:
            extended_start -= 1
        extended = " ".join(long_words[extended_start:best_end])
        new_ratio = max(
            fuzz.ratio(short_seq, extended),
            fuzz.ratio(short_seq.lower(), extended.lower()),
        )

        if new_ratio >= best_ratio:
            best_start = extended_start
            best_ratio = new_ratio
            start_attempts = 0  # Reset attempts since we had an improvement
        else:
            start_attempts += 1

    # Extend the match at the end
    end_attempts = 0
    while best_end < long_len and end_attempts < 3:
        if end_attempts == 0:
            extended_end = best_end + 1  # Temporarily extend to the right
        else:
            extended_end += 1
        extended = " ".join(long_words[best_start:extended_end])
        new_ratio = max(
            fuzz.ratio(short_seq, extended),
            fuzz.ratio(short_seq.lower(), extended.lower()),
        )

        if new_ratio >= best_ratio:
            best_end = extended_end
            best_ratio = new_ratio
            end_attempts = 0  # Reset attempts since we had an improvement
        else:
            end_attempts += 1

    best_match = " ".join(long_words[best_start:best_end])
    if best_ratio == 0:
        best_ratio = max(
            fuzz.ratio(short_seq, best_match),
            fuzz.ratio(short_seq.lower(), best_match.lower()),
        )
    return best_match, best_ratio


# # Example usage
# short_seq = "qulck bruwn fox jnnps"
# long_seq = "head padding here. The quick brown fox jumps over the lazy dog. tail padding"

# short_seq = "Ta cứ xem như dân tộc họ bị phiêu bạt đã hơn hai nghìn năm mà họ vẫn không bị một dân-tộc nào đồng-hóa, họ vẫn giữ được bản-chất Do thái rồi lại ngấm ngầm vận động thu-phục lại nước cũ, thì cdu biết dân-toc họ là một dân-tocodang kính."
# long_seq = "Ta cứ xem như dân tộc họ bị phiêu bạt đã hơn hai nghìn năm mà họ vẫn không bị một dân tộc nào đồng hóa, họ vẫn giữ được bản chất Do-Thái rồi lại ngấm ngầm vận động thu phục lại nước cũ, thì đủ biết dân tộc họ là một dân tộc đáng kính."

# best_match, score = find_best_match(short_seq, long_seq)
# print(f"Best matching region: '{best_match}'")
# print(f"Similarity score: {score}")
