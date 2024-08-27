import re
import Levenshtein
import math

MAX_ATT = 4


def norm_ed(s1, s2):
    distance = Levenshtein.distance(s1, s2)
    max_len = max(len(s1), len(s2))
    return 1 - (distance / max_len)


def find_sub_char(before, after):
    """
    Find the most similar subsequence in the 'before' sequence that matches the 'after' sequence.
    The subsequence with the highest similarity and smallest length gap is chosen.
    """

    def n_e_dist(s1, s2):
        """
        Compute the normalized Levenshtein distance between two strings.
        Normalized Levenshtein distance = Levenshtein distance / max(len(s1), len(s2))
        """
        return Levenshtein.distance(s1, s2) / max(len(s1), len(s2))

    min_dist = float("inf")
    best_subseq = ""
    after_len = len(after)

    for i in range(len(before)):
        for j in range(i + 1, len(before) + 1):
            subsequence = before[i:j]
            distance = n_e_dist(subsequence, after)
            length_gap = abs(len(subsequence) - after_len)

            # Select the subsequence with the smallest distance and the smallest length gap
            if distance < min_dist or (
                distance == min_dist and length_gap < abs(len(best_subseq) - after_len)
            ):
                min_dist = distance
                best_subseq = subsequence

    return best_subseq


def max_ed(s1, s2):
    return max(
        norm_ed(s1, s2),
        norm_ed(s1.lower(), s2.lower()),
    )


def custom_split(input_string):
    # Trim spaces from both ends
    trimmed_string = input_string.strip()

    # Replace multiple spaces with a single space
    single_spaced_string = re.sub(r"\s+", " ", trimmed_string)

    # Split by spaces and keep punctuation together
    # The regex pattern captures sequences of non-space characters (words)
    # and sequences of consecutive punctuations.
    words = re.findall(r"\w+|\s+|[^\w\s]+", single_spaced_string)

    # Filter out any standalone spaces
    words = [word for word in words if not word.isspace()]

    return words


def count_w(text):
    seq = custom_split(text)
    return len([word for word in seq if word])


def custom_join(words_list):
    result = []
    i = 0

    while i < len(words_list):
        if (
            i + 2 < len(words_list)
            and words_list[i + 1] == "-"
            and words_list[i + 2].isalnum()
        ):
            # Handle sequences like ['word', '-', 'word2']
            result.append(words_list[i] + "-" + words_list[i + 2])
            i += 3  # Skip the next two elements
        elif i > 0 and words_list[i] == "-" and words_list[i - 1].isalnum():
            # Handle continuation of hyphenated words
            result[-1] += "-" + words_list[i + 1] if i + 1 < len(words_list) else ""
            i += 2
        elif (
            re.match(r"\W+", words_list[i])
            and i > 0
            and not re.match(r"\W+", words_list[i - 1])
        ):
            # Handle punctuation immediately following a word without adding spaces
            result[-1] += words_list[i]
            i += 1
        elif i + 1 < len(words_list) and re.match(r"\W+", words_list[i + 1]):
            # Handle sequences like ['...', 'I'] to avoid adding spaces within punctuation clusters
            result.append(words_list[i])
            i += 1
        else:
            # General case for merging words with a space
            result.append(words_list[i])
            i += 1

    return " ".join(result).replace("  ", " ").strip()


def find_best_match(short_seq, long_seq):
    short_words = custom_split(short_seq)
    long_words = custom_split(long_seq)
    short_len = len(short_words)
    long_len = len(long_words)

    best_ratio = 0
    window_size = int(min(short_len, long_len) * 0.8)
    best_start = math.ceil(min(short_len, long_len) * 0.15)
    best_end = window_size

    # Slide a window of size similar to short_seq over long_seq
    for i in range(abs(long_len - short_len) + 1):
        end = i + window_size
        candidate = custom_join(long_words[i:end])
        ratio = max_ed(short_seq, candidate)

        if ratio > best_ratio:
            best_ratio = ratio
            best_start = i
            best_end = end

    # Extend the match if possible while maintaining or improving the ratio
    start_attempts = 0
    while best_start > 0 and start_attempts < MAX_ATT:
        if start_attempts == 0:
            extended_start = best_start - 1  # Temporarily extend to the left
        else:
            extended_start -= 1
        extended = custom_join(long_words[extended_start:best_end])
        new_ratio = max_ed(short_seq, extended)

        if new_ratio >= best_ratio:
            best_start = extended_start
            best_ratio = new_ratio
            start_attempts = 0  # Reset attempts since we had an improvement
        else:
            start_attempts += 1

    # Extend the match at the end
    end_attempts = 0
    while best_end < long_len and end_attempts < MAX_ATT:
        if end_attempts == 0:
            extended_end = best_end + 1  # Temporarily extend to the right
        else:
            extended_end += 1
        extended = custom_join(long_words[best_start:extended_end])
        new_ratio = max_ed(short_seq, extended)

        if new_ratio >= best_ratio:
            best_end = extended_end
            best_ratio = new_ratio
            end_attempts = 0  # Reset attempts since we had an improvement
        else:
            end_attempts += 1

    best_match = custom_join(long_words[best_start:best_end])
    best_match = find_sub_char(long_seq, best_match)
    return best_match, best_ratio


# # test cases
# test_cases = [
#     (
#         "qulck bruwn fox jnnps",
#         "head padding here. The quick brown fox jumps over the lazy dog. tail padding",
#     ),
#     (
#         "Ta cứ xem như dân tộc họ bị phiêu bạt đã hơn hai nghìn năm mà họ vẫn không bị một dân-tộc nào đồng-hóa, họ vẫn giữ được bản-chất Do thái rồi lại ngấm ngầm vận động thu-phục lại nước cũ, thì cdu biết dân-toc họ là một dân-tocodang kính.",
#         "Ta cứ xem như dân tộc họ bị phiêu bạt đã hơn hai nghìn năm mà họ vẫn không bị một dân tộc nào đồng hóa, họ vẫn giữ được bản chất Do-Thái rồi lại ngấm ngầm vận động thu phục lại nước cũ, thì đủ biết dân tộc họ là một dân tộc đáng kính.",
#     ),
#     (
#         "4 .- Nguyên nhân thứ tư là tinh thần quốc gia",
#         "4. Nguyên nhân thứ tư là tinh thần quốc gia mới Ả Rập",
#     ),
#     (
#         "Lý tưởng là kim chỉ nam hướng dẫn cuộc đời, là ngôi sao sáng mà chúng ta luôn luôn chiêm ngưỡng. Người không có lý tưởng chẳng khác nào chiếc thuyền ra giữa bề, lênh đếnh không biết nơi nào đề",
#         "Lý tưởng là kim chỉ nam hướng dẫn cuộc đời, là ngôi sao sáng chúng ta luôn luôn chiêm ngưỡng. Người không có lý tưởng chẳng khác nào chiếc thuyền ra giữa bể, lênh đênh không biết nơi nào để cập bến",
#     ),
#     (
#         "chắn là từ trước đến nay, phương-pháp ấy đã giúp được nhiều lợi-ích. Từ dây tại Londres co ca mot nhóm người co tỉnh-thần thực-tien và nghiêm-trang làm việc tại « Hội nghiên- cứu thuật Đắc-lực » (Société d'Efficience) và han-hai nghiên- cứu công-việc doanh-nghiệp cũng như nha địa-chat-học nghiên- cứu đá lửa.",
#         "chắc chắn là từ trước đến nay, phương-pháp ấy đã giúp được nhiều lợi-ích. Từ đây tại Londres có cả một nhóm người có tinh-thần thực-tiễn và nghiêm-trang làm việc tại « Hội nghiên-cứu thuật Đắc-lực » (Société d'Effícience) và hăng-hái nghiên-cứu công-việc doanh-nghiệp cũng như nhà địa-chất-học nghiên-cứu đá lửa.",
#     ),
#     (
#         "Để tiếp tục cuộc chiến đấu sau này, Nasser xin Nga giúp khí giới nữa. Một cầu hàng không cũng lớn lao như cầu hằng không của Mỹ ở Tây Berlin năm 1949, đã đỗ xuống Ai Cập và Syrie vô số phi cơ, chiến xa, đại bắc, thay thế được 80% những tồn thất của Ả Rập. Để thay thế 15000 quân bị giết, bị thương, Nasser gọi những lĩnh từ Yemen về. Thủ đô Le Caire vẫn ở trong tình trạng phòng thủ. Người ta tuyên thêm dân quận, cải to chính phủ. Nasser kiêm luôn chức Thủ tướng, cách chức viên Tổng tham mưu trưởng, tổ chức lại quân đội, phải người qua Nga nghiên cứu bình bị. Nga cũng phái thống chế Zakharov qua Ai Cập để tìm nguyên",
#         "Để tiếp tục cuộc chiến đấu sau này, Nasser xin Nga giúp đỡ vũ khí nữa. Một cầu hàng không cũng lớn như cầu hàng không của Mĩ ở Tây Berlin năm 1949, đã đổ xuống Ai Cập và Syrie vô số chiến xa, đại bác, thay thế được 80% những tổn thất của Ả Rập. Để thay thế 15.000 quân bị giết, bị thương, Nasser gọi những lính từ Yémen về. Thủ đô Le Caire vẫn ở trong tình trạng phòng thủ. Người ta tuyển thêm dân quân, cải tổ chính phủ. Nasser kiêm luôn chức Thủ tướng, cách chức viên Tổng tham mưu trưởng, tổ chức lại quân đội, phái người qua Nga nghiên cứu binh bị. Nga cũng phái nguyên soái Zakharov qua Ai Cập để tìm nguyên bại trận của Ả Rập",
#     ),
#     (
#         "Nàng là người làm ruộng và cũng chỉ nghề làm ruộng. Nông nghiệp In cần -bản của nền kinh-tế quốc-gia, bởi vậy, ngày klit dai định, trước khi to-chức thi Hương, vua The-to da ban- hành chính sách nòng-nghiệp, cho thiết-lập điền-hạ, qui-định việc đặc thù công-thổ, còng-điền, truyền cho các trấn, nhất là ở Bắc thành, phải xơi đào sông ngòi, vét các cửa biển, bảo- vệ. thiết lập và tu-hồ các bộ-thống để điều. Chính-sách ruộng dat nhà Nguyễn phá vo chế-đo điền-trang của các triều-đại trước, thiết-lập được chế độ tư-điền, nhờ đó mỗi người dân có lối- thiếu vài ba sảo ruộng tư đề cày-cấy ngoài số còng-điền được hàng-xã cấp-phát. Những thí-nghiệm thành-công của Nguyễn- Công Trú tại Tiền-hải, Kim-sơn, Quảng-yên năm 1828-29, ngoài việc khai-khẩu được hơn 30.000 mẫu ruộng và hoàn-thành kế hoạch di dân, còn giúp triều-đình giải-quyết được nạn đói kèm và giặc cướp (61). Sắc-dụ năm 1830 của vua Minh-mệnh chấp-thuận cấp-phát những ruộng đất bỏ hoang cho bất cứ ai có đơn xin ; Sắc-dụ năm 1864 cho phép được thành-lập một ấp mới, tất cả những ai đã vỡ được 20 mẫu ruộng và tập-trung được 10 dân định. Đặc sắc nhất là Sắc-dụ năm 1840 bắt-buộc các dại tiền-chủ phải cắt 1/3 dien-sản bo vào công-điền ; Sắc- dụ tiến-họ này tiếc thay chỉ được áp dụng một phần ở Gia-định rồi sau tại bị đình-chỉ vì triều đình còn bận đối-phc với những rắc rối chinh -trị về phía Cao-mien. Các lãnh tụ nhỉ Nguyễn đã thay ró những tương-quan hỗ tương giữa kinh tế và xã-hội ; tình trạng bết-an của dân-chúng bắt nguồn từ sự nghèo đói, từ",
#         "Nông là người làm ruộng và cũng chỉ nghề làm ruộng. Nông nghiệp là căn-bản của nền kinh-tế quốc-gia, bởi vậy, ngay khi đại-định, trước khi tổ-chức thi Hương, vua Thế-tổ đã ban-hành chánh-sách nông-nghiệp, cho thiết-lập điền-hạ, qui-định việc đắc-thụ công-thổ, công-điền, truyền cho các trấn, nhất là ở Bắc-thành, phải xoi đào sông ngòi, vét các cửa biển, bảo-vệ, thiết-lập và tu-bổ các hệ-thống đê-điều. Chính-sách ruộng đất nhà Nguyễn phá vỡ chế-độ điền-trang của các triều-đại trước, thiết lập được chế-độ tư-điền, nhờ đó mỗi người dân có tối-thiểu vài ba sào ruộng tư để cày-cấy ngoài số công-điền được hàng-xá cấp-phát. Những thí-nghiệm thành-công của Nguyễn-Công-Trứ tại Tiền-hải, Kim-sơn, Quảng-yên năm 1828-29, ngoài việc khai-khẩn được hơn 30.000 mẫu ruộng và hoàn-thành kế-hoạch di-dân, còn giúp triều-đình giải-quyết được nạn đói kém và giặc cướp. Sắc-dụ năm 1830 của vua Minh-mệnh chấp-thuận cấp-phát những ruộng đất bỏ hoang cho bất cứ ai có đơn xin; Sắc-dụ năm 1864 cho phép được thành-lập một ấp mới, tất cả những ai đã vỡ được 20 mẫu ruộng và tập-trung được 10 dân đinh. Đặc-sắc nhất là Sắc-dụ năm 1840 bắt-buộc các đại-điền-chủ phải cắt 1/3 điền-sản bỏ vào công-điền; Sắc-dụ tiến-bộ này tiếc thay chỉ được áp dụng một phần ở Gia-định rồi sau lại bị đình-chỉ vì triều-đình còn bận đối-phó với những rắc-rối chính-trị phía Cao-miên. Các lãnh-tụ nhà Nguyễn đã thấy rõ những tương-quan hỗ-tương giữa kinh-tế và xã-hội; tình-trạng bất-an của dân-chúng bắt nguồn từ sự nghèo đói, từ việc nông-dân thiếu ruộng cày, từ sự áp-bức của những quan-lại bất-nhân, từ sự bóc-lột dã-man của cường-hào ác-bá",
#     ),
#     (
#         "Mặt trận giải phóng Palestine một mực chống lại đề nghị ấy, âm mưu ám sát Hussein, quốc vương Jordanie, người chủ hòa, và Hussein đem quân đàn áp dữ dội Mặt trận. Vụ này Palestine gọi là vụ Tháng chin đen.",
#         "Tổ chức giải phóng Palestine một mực chống lại đề nghị ấy, âm mưu ám sát Hussein, quốc vương Jordanie, người chủ hòa, và Hussein đem quân đàn áp dữ dội Tổ chức giải phóng Palestine. Vụ này Palestine gọi là vụ Tháng chín đen.",
#     ),
# ]

# for short_seq, long_seq in test_cases:
#     best_match, score = find_best_match(short_seq, long_seq)
#     print(f"Best matching region: '{best_match}'")
#     print(f"Similarity score: {score}")
