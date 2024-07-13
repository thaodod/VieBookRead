from openai import OpenAI

# Initialize the OpenAI API client
client = OpenAI(
    # This is the default and can be omitted
    api_key="***REMOVED***",
)

# Define the prompt/question you want to ask
prompt = """
Given an html file.
<html xmlns="http://www.w3.org/1999/xhtml" lang="en" xml:lang="en">
  <head>
    <title>Inconnu(e)</title>
    <meta http-equiv="Content-Type" content="text/html; charset=utf-8"/>
  <link href="stylesheet.css" rel="stylesheet" type="text/css"/>
<link href="page_styles.css" rel="stylesheet" type="text/css"/>
</head>
  <body class="calibre">
<h1 id="id_Toc498587533" class="block_17" lang="vi">MẤY CÂU CA TOÀN THỂ CẢ NƯỚC</h1>
	<p class="block_18" lang="vi">Nước ta hình thế bốn phương,</p>
	<p class="block_18" lang="vi">Ba mươi vạn lẻ dậm vuông quy vào.</p>
	<p class="block_18" lang="vi">Bắc thời giáp đất nước Tầu,</p>
	<p class="block_18" lang="vi">Đông, Nam, giáp bể, Tây, Lào với Man.</p>
	<p class="block_18" lang="vi">Cứ trong các tỉnh mà bàn,</p>
	<p class="block_18" lang="vi">Bắc hai mươi ba giang san chuyên thành.</p>
	<p class="block_18" lang="vi">Đôi nơi thành-phố đã đành,</p>
	<p class="block_18" lang="vi">Lại thêm ba đạo ở vành xa kia.</p>
	<p class="block_18"><span lang="vi" class="calibre2">Núi Phan-Păng </span><sup lang="vi" class="calibre4"><a href="index_split_057.html#note_1" title="1" class="noteref"><sup id="back_note_1" class="calibre5">1</sup></a></sup><span lang="vi" class="calibre2"> nhất Bắc-Kỳ,</span></p>
	<p class="block_18" lang="vi">Hơn ba nghìn thước đâu bì được cao.</p>
	<p class="block_18" lang="vi">Tản-Viên, Tam-Đảo thế nào,</p>
	<p class="block_18" lang="vi">Ngoài một nghìn thước cũng vào bực hơn.</p>
	<p class="block_18" lang="vi">Biết bao các ngả sông con,</p>
	<p class="block_18" lang="vi">Thái-Bình, Nhị-Thủy đại xuyên hai giòng,</p>
	<p class="block_18" lang="vi">Trung-Kỳ thành-phố một vùng,</p>
	<p class="block_18" lang="vi">Mười hai tỉnh lỵ ở cùng cong cong.</p>
	<p class="block_18" lang="vi">Mã-giang giài nhất các sông,</p>
	<p class="block_18" lang="vi">Linh-giang thời rộng và cùng Lam-giang.</p>
	<p class="block_18" lang="vi">Tam-phong ở đất Nha-Trang,</p>
	<p class="block_18" lang="vi">Đo ra mới biết núi càng là cao.</p>
	<p class="block_18" lang="vi">Đến như duyên-cách thế nào,</p>
	<p class="block_18" lang="vi">Diễn ra từng tỉnh chép vào nhời ca.</p>
	<p class="block_18" lang="vi">Trong Nam các tỉnh đặt ra,</p>
	<p class="block_18"><span lang="vi" class="calibre2">Đời vua Minh-Mệnh mười ba đó mà. </span><sup lang="vi" class="calibre4"><a href="index_split_058.html#note_2" title="2" class="noteref"><sup id="back_note_2" class="calibre5">2</sup></a></sup></p>
	<p class="block_18" lang="vi">Còn như các tỉnh Bắc-hà,</p>
	<p class="block_18" lang="vi">Chừng năm thập nhị ấy là kỷ-niên.</p>
	<p class="block_18" lang="vi">Dẫu rằng thành quách biến thiên,</p>
	<p class="block_18" lang="vi">Vẫn là Hồng-Lạc dõi truyền đến nay.</p>
	<p class="block_18" lang="vi">Rõ ràng tổ-quốc là đây,</p>
	<p class="block_18" lang="vi">Người ta nên biết sự này trước tiên.</p>
	</body>
</html>

Then I provide a text which needs to be corrected as its content predicted from non-perfect OCR tool. Please use html content as reference source to correct below input text:
<input-text>
Chừng năm thập nhị ấy là kỷ-nièn. Dầu rằng thành quách biến thiên, Vẫn là Hồng-Lạc dõi truyền đến nay. Rõ ràng tổ-quốc là dây,
</input-text>

Please don't add more text, strictly follow the orthography of the reference, only correct based on what existed on input text. Answer corrected text.
"""

# Call the OpenAI API to generate the corrected text
response = client.chat.completions.create(
    model="gpt-3.5-turbo",
    messages=[
        {"role": "system", "content": "You are an assistant."},
        {
            "role": "user",
            "content": prompt,
        },
    ],
    temperature=0
)

print(response.choices[0].message)
