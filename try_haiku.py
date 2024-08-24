from anthropic import AnthropicVertex, APIError

prompt = [
    """
Given below sequences:
sequence 1: "Ông ta có ngờ đâu chính nỗi bất công ông phải chịu đã làm thay đổi hẳn một người đồng chủng"
sequence 2: "có ngờ đâu chính nỗi bất công ông phải chịu đã làm thay đổi hẳn một người đồng chủng"
sequence 1 has enough words but it might not accurate at diacritics while sequence 2 has high accuracy in diacritic marks but sometimes missing words.
Please combine them for a fuller sequence with accurate diacritic marks. Answer processed sequence only without format or tag.
""",
    """
Given below sequences:
sequence 1: "Để tiếp tục cuộc chiến đấu sau này, Nasser xin Nga giúp khí giới nữa. Một cầu hàng không cũng lớn lao như cầu hằng không của Mỹ ở Tây Berlin năm 1949, đã đỗ xuống Ai Cập và Syrie vô số phi cơ, chiến xa, đại bắc, thay thế được 80% những tồn thất của Ả Rập. Để thay thế 15000 quân bị giết, bị thương, Nasser gọi những lĩnh từ Yemen về. Thủ đô Le Caire vẫn ở trong tình trạng phòng thủ. Người ta tuyên thêm dân quận, cải to chính phủ. Nasser kiêm luôn chức Thủ tướng, cách chức viên Tổng tham mưu trưởng, tổ chức lại quân đội, phải người qua Nga nghiên cứu bình bị. Nga cũng phái thống chế Zakharov qua Ai Cập để tìm nguyên"
sequence 2: "Để tiếp tục cuộc chiến đấu sau này, Nasser xin Nga giúp đỡ vũ khí nữa. Một cầu hàng không cũng lớn như cầu hàng không của Mĩ ở Tây Berlin năm 1949, đã đổ xuống Ai Cập và Syrie vô số chiến xa, đại bác, thay thế được 80% những tổn thất của Ả Rập. Để thay thế 15.000 quân bị giết, bị thương, Nasser gọi những lính từ Yémen về. Thủ đô Le Caire vẫn ở trong tình trạng phòng thủ. Người ta tuyển thêm dân quân, cải tổ chính phủ. Nasser kiêm luôn chức Thủ tướng, cách chức viên Tổng tham mưu trưởng, tổ chức lại quân đội, phái người qua Nga nghiên cứu binh bị. Nga cũng phái nguyên soái Zakharov qua Ai Cập để tìm nguyên bại"

Now, note that: sequence 1 has enough words but it might not be accurate at diacritic or vowels.
Whereas, sequence 2 has high precision in diacritics but it sometimes misses words or/and contains hallucinated words (which are very visual different with the corresponding in sequence 1).
Please combine them for a fuller sequence with accurate diacritic marks. Answer processed sequence only without format or tag.
""",
    """
Given below sequences:
sequence 1: "Trong doanh-nghiệp, kinh-nghiệm suông chưa đủ ; còn phải có khiếu quan-sát, ham-mê, thích-ứng, rèn-luyện ; nếu không có những khiếu ấy thì kinh-nghiệm chỉ làm cho ta di"
sequence 2: "Trong doanh-nghiệp, kinh-nghiệm suông chưa đủ; còn phải có khiếu quan-sát, ham-mê, thích-ứng, rèn-luyện; nếu không có những khiếu ấy thì kinh-nghiệm chỉ làm cho ta đi"

Now, note that: sequence 1 has enough words but it might not be accurate at diacritic or vowels.
Whereas, sequence 2 has high precision in diacritics but it sometimes misses words or/and contains hallucinated words (which are very visual different with the corresponding in sequence 1).
Please combine them for a fuller sequence with accurate diacritic marks. Answer processed sequence only without format or tag.
""",
    """
Given below sequences:
sequence 1: "Ông Giám đốc một hãng quảng cáo nọ có thói quen ghi tất cả các công việc phải làm. Ông ta có một bảng ghi"
sequence 2: "Ông giám đốc một hãng quảng cáo nọ có thói quen ghi tất cả các công việc phải làm. Ông có tên một"

Now, note that: sequence 1 has enough words but it might not be accurate at diacritic or vowels.
Whereas, sequence 2 has high precision in diacritics but it sometimes misses words or/and contains hallucinated words (which are very visual different with the corresponding in sequence 1).
Please combine them for a fuller sequence with accurate diacritic marks. Answer processed sequence only without format or tag.
""",
]


LOCATION = "us-central1"  # or "europe-west4"

client = AnthropicVertex(region=LOCATION, project_id="***REMOVED***")
m_name = "claude-3-haiku@20240307"

for i in range(len(prompt)):
    try:
        message = client.messages.create(
            messages=[
                {
                    "role": "user",
                    "content": prompt[i],
                }
            ],
            model=m_name,
            max_tokens=2048,
            temperature=0.0,
        )
        print(message.content[0].text)
    except APIError as e:
        if e.status_code == 429:
            print("Rate limit exceeded. Please wait before making more requests.")
        elif e.status_code == 402:
            print("Insufficient funds or quota exceeded.")
        else:
            print(f"API error occurred: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
