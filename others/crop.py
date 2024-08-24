from thefuzz import fuzz
import re


def fix_punctuation(text):
    # Pattern explanation:
    # (\d+) - Captures one or more digits (the numbering)
    # \s+ - Matches one or more whitespace characters
    # ([.,\-]+) - Captures one or more punctuation marks (period, comma, or hyphen)
    pattern = r"(\d+)\s+([.,\-]+)"

    # Replace with number immediately followed by punctuation
    adjusted_text = re.sub(pattern, r"\1\2", text)

    return adjusted_text


def custom_split(input_string):
    # Trim spaces from both ends
    trimmed_string = input_string.strip()

    # Replace multiple spaces with a single space
    single_spaced_string = re.sub(r"\s+", " ", trimmed_string)

    # Split only by spaces but keep punctuation attached to words
    words = re.findall(r"\S+|\n", single_spaced_string)

    return words


def count_w(text):
    seq = custom_split(text)
    return len([word for word in seq if word])


def find_best_match(short_seq, long_seq):
    short_seq = fix_punctuation(short_seq)
    long_seq = fix_punctuation(long_seq)

    short_words = custom_split(short_seq)
    long_words = custom_split(long_seq)
    short_len = len([word for word in short_words if word])
    long_len = len([word for word in long_words if word])

    best_ratio = 0
    window_size = int(min(short_len, long_len) * 0.8)
    best_start = 1
    best_end = window_size

    # Slide a window of size similar to short_seq over long_seq
    for i in range(abs(long_len - short_len) + 1):
        end = i + window_size
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
    return best_match, best_ratio


# # Example usage
# short_seq = "qulck bruwn fox jnnps"
# long_seq = "head padding here. The quick brown fox jumps over the lazy dog. tail padding"

# short_seq = "Ta cứ xem như dân tộc họ bị phiêu bạt đã hơn hai nghìn năm mà họ vẫn không bị một dân-tộc nào đồng-hóa, họ vẫn giữ được bản-chất Do thái rồi lại ngấm ngầm vận động thu-phục lại nước cũ, thì cdu biết dân-toc họ là một dân-tocodang kính."
# long_seq = "Ta cứ xem như dân tộc họ bị phiêu bạt đã hơn hai nghìn năm mà họ vẫn không bị một dân tộc nào đồng hóa, họ vẫn giữ được bản chất Do-Thái rồi lại ngấm ngầm vận động thu phục lại nước cũ, thì đủ biết dân tộc họ là một dân tộc đáng kính."

# short_seq = "4 .- Nguyên nhân thứ tư là tinh thần quốc gia"
# long_seq = "4. Nguyên nhân thứ tư là tinh thần quốc gia mới Ả Rập"

# short_seq = "Lý tưởng là kim chỉ nam hướng dẫn cuộc đời, là ngôi sao sáng mà chúng ta luôn luôn chiêm ngưỡng. Người không có lý tưởng chẳng khác nào chiếc thuyền ra giữa bề, lênh đếnh không biết nơi nào đề"
# long_seq = "Lý tưởng là kim chỉ nam hướng dẫn cuộc đời, là ngôi sao sáng chúng ta luôn luôn chiêm ngưỡng. Người không có lý tưởng chẳng khác nào chiếc thuyền ra giữa bể, lênh đênh không biết nơi nào để cập bến"

# short_seq = "chắn là từ trước đến nay, phương-pháp ấy đã giúp được nhiều lợi-ích. Từ dây tại Londres co ca mot nhóm người co tỉnh-thần thực-tien và nghiêm-trang làm việc tại « Hội nghiên- cứu thuật Đắc-lực » (Société d'Efficience) và han-hai nghiên- cứu công-việc doanh-nghiệp cũng như nha địa-chat-học nghiên- cứu đá lửa."
# long_seq = "chắc chắn là từ trước đến nay, phương-pháp ấy đã giúp được nhiều lợi-ích. Từ đây tại Londres có cả một nhóm người có tinh-thần thực-tiễn và nghiêm-trang làm việc tại « Hội nghiên-cứu thuật Đắc-lực » (Société d'Effícience) và hăng-hái nghiên-cứu công-việc doanh-nghiệp cũng như nhà địa-chất-học nghiên-cứu đá lửa."

# short_seq = "Để tiếp tục cuộc chiến đấu sau này, Nasser xin Nga giúp khí giới nữa. Một cầu hàng không cũng lớn lao như cầu hằng không của Mỹ ở Tây Berlin năm 1949, đã đỗ xuống Ai Cập và Syrie vô số phi cơ, chiến xa, đại bắc, thay thế được 80% những tồn thất của Ả Rập. Để thay thế 15000 quân bị giết, bị thương, Nasser gọi những lĩnh từ Yemen về. Thủ đô Le Caire vẫn ở trong tình trạng phòng thủ. Người ta tuyên thêm dân quận, cải to chính phủ. Nasser kiêm luôn chức Thủ tướng, cách chức viên Tổng tham mưu trưởng, tổ chức lại quân đội, phải người qua Nga nghiên cứu bình bị. Nga cũng phái thống chế Zakharov qua Ai Cập để tìm nguyên"
# long_seq = "Để tiếp tục cuộc chiến đấu sau này, Nasser xin Nga giúp đỡ vũ khí nữa. Một cầu hàng không cũng lớn như cầu hàng không của Mĩ ở Tây Berlin năm 1949, đã đổ xuống Ai Cập và Syrie vô số chiến xa, đại bác, thay thế được 80% những tổn thất của Ả Rập. Để thay thế 15.000 quân bị giết, bị thương, Nasser gọi những lính từ Yémen về. Thủ đô Le Caire vẫn ở trong tình trạng phòng thủ. Người ta tuyển thêm dân quân, cải tổ chính phủ. Nasser kiêm luôn chức Thủ tướng, cách chức viên Tổng tham mưu trưởng, tổ chức lại quân đội, phái người qua Nga nghiên cứu binh bị. Nga cũng phái nguyên soái Zakharov qua Ai Cập để tìm nguyên bại trận của Ả Rập"

# short_seq = "Nàng là người làm ruộng và cũng chỉ nghề làm ruộng. Nông nghiệp In cần -bản của nền kinh-tế quốc-gia, bởi vậy, ngày klit dai định, trước khi to-chức thi Hương, vua The-to da ban- hành chính sách nòng-nghiệp, cho thiết-lập điền-hạ, qui-định việc đặc thù công-thổ, còng-điền, truyền cho các trấn, nhất là ở Bắc thành, phải xơi đào sông ngòi, vét các cửa biển, bảo- vệ. thiết lập và tu-hồ các bộ-thống để điều. Chính-sách ruộng dat nhà Nguyễn phá vo chế-đo điền-trang của các triều-đại trước, thiết-lập được chế độ tư-điền, nhờ đó mỗi người dân có lối- thiếu vài ba sảo ruộng tư đề cày-cấy ngoài số còng-điền được hàng-xã cấp-phát. Những thí-nghiệm thành-công của Nguyễn- Công Trú tại Tiền-hải, Kim-sơn, Quảng-yên năm 1828-29, ngoài việc khai-khẩu được hơn 30.000 mẫu ruộng và hoàn-thành kế hoạch di dân, còn giúp triều-đình giải-quyết được nạn đói kèm và giặc cướp (61). Sắc-dụ năm 1830 của vua Minh-mệnh chấp-thuận cấp-phát những ruộng đất bỏ hoang cho bất cứ ai có đơn xin ; Sắc-dụ năm 1864 cho phép được thành-lập một ấp mới, tất cả những ai đã vỡ được 20 mẫu ruộng và tập-trung được 10 dân định. Đặc sắc nhất là Sắc-dụ năm 1840 bắt-buộc các dại tiền-chủ phải cắt 1/3 dien-sản bo vào công-điền ; Sắc- dụ tiến-họ này tiếc thay chỉ được áp dụng một phần ở Gia-định rồi sau tại bị đình-chỉ vì triều đình còn bận đối-phc với những rắc rối chinh -trị về phía Cao-mien. Các lãnh tụ nhỉ Nguyễn đã thay ró những tương-quan hỗ tương giữa kinh tế và xã-hội ; tình trạng bết-an của dân-chúng bắt nguồn từ sự nghèo đói, từ"
# long_seq = "Nông là người làm ruộng và cũng chỉ nghề làm ruộng. Nông nghiệp là căn-bản của nền kinh-tế quốc-gia, bởi vậy, ngay khi đại-định, trước khi tổ-chức thi Hương, vua Thế-tổ đã ban-hành chánh-sách nông-nghiệp, cho thiết-lập điền-hạ, qui-định việc đắc-thụ công-thổ, công-điền, truyền cho các trấn, nhất là ở Bắc-thành, phải xoi đào sông ngòi, vét các cửa biển, bảo-vệ, thiết-lập và tu-bổ các hệ-thống đê-điều. Chính-sách ruộng đất nhà Nguyễn phá vỡ chế-độ điền-trang của các triều-đại trước, thiết lập được chế-độ tư-điền, nhờ đó mỗi người dân có tối-thiểu vài ba sào ruộng tư để cày-cấy ngoài số công-điền được hàng-xá cấp-phát. Những thí-nghiệm thành-công của Nguyễn-Công-Trứ tại Tiền-hải, Kim-sơn, Quảng-yên năm 1828-29, ngoài việc khai-khẩn được hơn 30.000 mẫu ruộng và hoàn-thành kế-hoạch di-dân, còn giúp triều-đình giải-quyết được nạn đói kém và giặc cướp. Sắc-dụ năm 1830 của vua Minh-mệnh chấp-thuận cấp-phát những ruộng đất bỏ hoang cho bất cứ ai có đơn xin; Sắc-dụ năm 1864 cho phép được thành-lập một ấp mới, tất cả những ai đã vỡ được 20 mẫu ruộng và tập-trung được 10 dân đinh. Đặc-sắc nhất là Sắc-dụ năm 1840 bắt-buộc các đại-điền-chủ phải cắt 1/3 điền-sản bỏ vào công-điền; Sắc-dụ tiến-bộ này tiếc thay chỉ được áp dụng một phần ở Gia-định rồi sau lại bị đình-chỉ vì triều-đình còn bận đối-phó với những rắc-rối chính-trị phía Cao-miên. Các lãnh-tụ nhà Nguyễn đã thấy rõ những tương-quan hỗ-tương giữa kinh-tế và xã-hội; tình-trạng bất-an của dân-chúng bắt nguồn từ sự nghèo đói, từ việc nông-dân thiếu ruộng cày, từ sự áp-bức của những quan-lại bất-nhân, từ sự bóc-lột dã-man của cường-hào ác-bá"

# best_match, score = find_best_match(short_seq, long_seq)
# print(f"Best matching region: '{best_match}'")
# print(f"Similarity score: {score}")
