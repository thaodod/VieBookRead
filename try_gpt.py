from openai import OpenAI

client = OpenAI(
    api_key="REPLACEMENT_STRING",
)


prompt = """
Given an html content as below:
<html>
<body>
    <p class="block_29"><span class="calibre2" lang="vi">Ông chánh thấy dân chúng quá tin tưởng dị đoan, thừa dịp nầy ngài muốn làm cho dân chúng bớt mê tín, nên mạnh dạn huơ búa định chém vào cây. Bất thần, trong đám dân làng có một người nhập cốt xưng danh Thất Thánh nương nương, dõng dạc bảo thẳng với chánh tham biện Pháp </span>: </p>
    <p class="block_29" lang="vi">- Ta nói cho nhà ngươi rõ. Nếu ngươi ngang nhiên đốn phá chỗ của ta ở, thì ta sẽ vật mấy đứa con trai của ngươi chết liền trước mắt !</p>
    <p class="block_29" lang="vi">Nói xong thăng ngay. Quan chánh tham biện nổi xung, chém mạnh vào cây đa một nhát búa, song chưa kịp rút ra thì thấy tên bồi giúp việc nhà cho ông sợ hãi chạy tới cấp báo với ông rằng : Mấy đứa con trai nhỏ của ông là cậu Rọt, cậu Chel, câu Jacque đang ngồi chơi bỗng nhiên hộc máu và bất tỉnh.</p>
    <p class="block_29" lang="vi">Ông nghe nói hốt hoảng cấp tốc trở về dinh và cho mời liền bác sĩ đến điều trị. Bác sĩ xem mạch khám bịnh bảo là các em bị té nặng động phổi và cho uống thuốc cầm máu nhưng vô hiệu quả. Cả nhà còn đang lo sợ, lúc ấy có ông chủ quận Trương Công Lành bảo nhỏ với bà chánh tham biện : chắc có lẽ lúc nãy quan lớn khắc búa vào cây đa miếu bà nên bị bà quở hành mấy cậu. Vậy bà lớn nói với quan lớn vái tạ miếu bà thì chắc các cậu mạnh liền. Bà chánh nói lại với ông chánh và có ý phiền trách hành vi của chồng vừa rồi, việc làm đã không có lợi mà còn thêm hại cho con. Bà khuyên chồng mau mau lại miếu bà vái xin lỗi lạy tạ. Ông chánh nghe qua bán tính bán nghi, tuy nhiên phần thì thương con, phần nể vợ, nên chịu ra miếu bà. Ông khấn vái : « Nếu bà linh thiêng xin cho con tôi khỏe mạnh, tôi sẽ cất miếu lại cho bà. » Vái rồi ông về đến dinh thì thấy mấy đứa con ngồi chơi như thường. Cả nhà ông chánh đều vui mừng. Liền đó ông thâu hồi lệnh triệt hạ miếu bà và cây đa, rồi xuất tiền riêng mướn dân làng xây cất miếu lại bằng gạch lợp ngói rất đẹp và nới rộng rãi hơn xưa.</p>
    <p class="block_29" lang="vi">Từ đó ông chánh bà chánh hết lòng tin tưởng sự huyền bí của bà, ông bèn ra lịnh chuyền đèn điện vào miếu đốt sáng đêm, trước điện thờ bà không để cho tối, sự linh hiển của bà vẫn liên tục đến nay, đồng bào liên tỉnh Cà Mau, Sóc Trăng, Cần Thơ mỗi khi đến xin xâm cầu nguyện, được bà mách bảo sự kiết hung rất linh ứng, còn những kẻ ngang ngược khinh khi ngạo nghễ bà sẽ hành cho thấy trước mắt.</p>
    <p class="block_29" lang="vi">Chúng tôi nghe tin đồn sự linh hiển của bà do một ít người thâm niên ở Bạc Liêu lên Sài Gòn kể lại, chúng tôi bán tín bán nghi, muốn rõ hư thật thế nào, đích thân xuống tận Bạc Liêu tìm đến nhà các vị cao niên thân hào nhân sĩ tại đây, hỏi qua sự tích miếu bà Cố do người đồn đãi từ lâu. Quý vị ấy không ngần ngại tường thuật những sự việc mắt thấy tai nghe cho chúng tôi rõ chi tiết, và còn rất nhiều chuyện hiển linh khác nữa, đồng bào quanh vùng chợ Bạc Liêu có dịp chứng kiến.</p>
    <p class="block_29" lang="vi">Nghe qua câu chuyện chúng tôi có cảm nghĩ và băn khoăn : Giữa cái thời đại nguyên tử nầy tại sao có những chuyện thần thoại gieo rắc vào đầu óc con người như thế ? Có phải phản sự tiến bộ của dân tộc không ? Chẳng riêng miếu bà Cố ở Bạc Liêu và còn biết bao nhiêu chuyện huyền bí khác đã xảy ra trên thế giới nói chung và ở xứ ta nói riêng, như miếu Bà Mã Châu ở Cà Mau, miếu bà Chúa Xứ ở núi Sam, Châu Đốc v.v... hằng năm đồng bào lục tỉnh đổ xô đến hằng triệu người để chiêm ngưỡng trong những ngày vía.</p>
    <p class="block_29" lang="vi">Trở lại vấn đề miếu Bà Cố, chúng tôi không thần thánh hóa để gieo sự mê tín cho đồng bào, chỉ thuật lại những lời đồn đã thâu lượm được, cần nêu lên cho độc giả rõ biết với tinh thần hiếu cổ và cũng là một di tích lịch sử ở tỉnh Bạc Liêu ngày nay được đồng bào sùng kính, hầu hết khắp nơi đều nghe biết. Tỉnh Bạc Liêu trải qua bao lần biến cố, cảnh vật tiêu hao, nhưng miếu Bà Cố vẫn được an toàn, lúc nào cũng có người tới lui lễ bái không ngớt.</p>
    <p class="block_29"><span class="calibre2" lang="vi">Trước tòa cổ miếu có một tấm biển sơn son thếp vàng viết trên hiên bằng chữ Hán như sau : </span><b class="calibre3" lang="vi">THẤT THÁNH CHÍ LINH CHƠN TRUYỀN CỔ MIẾU</b></p>
    <p class="block_29" lang="vi">Và hai bên cột có hai câu đối, chúng tôi mạn phép xin ghi nguyên văn :</p>
    <p class="block_34" lang="vi">THÁNH ĐỨC TỪ BI THÔNG DIỆU PHÁP</p>
    <p class="block_35" lang="vi">THẦN LINH PHỔ ĐỘ VẠN THIÊN CƠ</p>
    <p class="block_29" lang="vi">Sau khi ghi chép đầy đủ về sự tích miếu Bà, lòng tôi nao nao, cảm thấy hình như còn thiếu sót một cái gì, nên có cảm tác những vầng thơ dưới đây :</p>
    <p class="block_36" lang="vi">CẢM TÁC</p>
    <p class="block_37" lang="vi">Một giai thoại, nghe qua càng hào hứng</p>
    <p class="block_37" lang="vi">Đề cao câu nên kính Thánh trọng Thần</p>
    <p class="block_37" lang="vi">Ngôi cổ miếu, địa phương đều tôn kính</p>
    <p class="block_37" lang="vi">Bài học hay, cho tham biện Pháp triều.</p>
    <p class="block_37" lang="vi">Để chứng minh, oai linh thiêng Thần Thánh</p>
    <p class="block_37" lang="vi">Cõi hữu hình, đồng nhứt với vô vi</p>
    <p class="block_37" lang="vi">Trơ với non sông tàn cây cổ thụ</p>
    <p class="block_37" lang="vi">Đêm trăng về, tô đậm nét huyền linh.</p>
    <p class="block_37" lang="vi">Ve dế gáy, kết tinh thành nhạc điệu</p>
    <p class="block_37" lang="vi">Gió vờn bay, lá đổ lạnh tê rờn !</p>
    <p class="block_38"><i class="calibre6" lang="vi">Cặp rắn thần </i><sup class="text_8" lang="vi"><a class="noteref" href="index_split_048.html#note_6" title="6"><sup class="calibre7" id="back_note_6">6</sup></a></sup><i class="calibre6" lang="vi">, như đến ngay chầu chực</i></p>
    <p class="block_37" lang="vi">Bóng đèn khuya lả ngọn xé màn đêm,</p>
    <p class="block_37" lang="vi">Chiều về đến, ánh tà dương lổ đổ</p>
    <p class="block_37" lang="vi">Khói hương trầm nghi ngút quyện không gian</p>
    <p class="block_37" lang="vi">Khúc phim đời, chớp nhoáng tuân lệnh gió</p>
    <p class="block_37" lang="vi">Như bức tranh, sống đẹp nét huy hoàng.</p>
    <p class="block_37" lang="vi">Linh Thượng Đế vạn năng quyền tối thượng</p>
    <p class="block_37" lang="vi">Linh Thánh Thần làm tiêu biểu nhơn gian</p>
    <p class="block_37" lang="vi">Để đồ đậm câu « Hữu cầu tất ứng »</p>
    <p class="block_39" lang="vi">Miếu có Bà, chùa điện có Phật Trời.</p>
</body>
</html>

Then providing a text which may need adjustments as it is predicted from imperfect OCR tool. Use html content as reference source to correct below input text if needed:
<input-text>
Tiên Sư Cổ Miếu
</input-text>

Firmly follow orthography and punctuation of the reference, only correct words existed within input text.
Avoid include content from the reference to fill up input but those are not actually existed within input.
First word of the text could also mis-recognized, check all words and letters carefully equally.
Answer corrected text, important: give only the processed result, without any explanations, formatting or tag.
"""


completion = client.chat.completions.create(
    model="gpt-4o-mini",
    messages=[
        {"role": "system", "content": "Assist user to process text"},
        {"role": "user", "content": prompt},
    ],
    temperature=0.0,
)

print(completion.choices[0].message.content)
