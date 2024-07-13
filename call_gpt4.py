from openai import OpenAI

# Initialize the OpenAI API client
client = OpenAI(
    # This is the default and can be omitted
    api_key="***REMOVED***",
)

# Define the prompt/question you want to ask
prompt = """
Given an html file:

<html xmlns="http://www.w3.org/1999/xhtml" lang="en" xml:lang="en">
  <head>
    <title>Inconnu(e)</title>
    <meta http-equiv="Content-Type" content="text/html; charset=utf-8"/>
  <link href="stylesheet.css" rel="stylesheet" type="text/css"/>
<link href="page_styles.css" rel="stylesheet" type="text/css"/>
</head>
  <body class="calibre">
<h2 id="id_Toc498587536" class="block_17" lang="vi">TỈNH HÀ-ĐÔNG</h2>
	<p class="block_18" lang="vi">Hà-Đông riêng ở một phương,</p>
	<p class="block_18" lang="vi">Ki-lô mười một kể đường gần ghê.</p>
	<p class="block_18"><span lang="vi" class="calibre2">Từ-Liêm </span><i lang="vi" class="calibre6">(huyện)</i><span lang="vi" class="calibre2">, Hoài-Đức </span><i lang="vi" class="calibre6">(phủ)</i><span lang="vi" class="calibre2"> liền kề,</span></p>
	<p class="block_18"><span lang="vi" class="calibre2">Còn như Đan-Phượng </span><i lang="vi" class="calibre6">(huyện)</i><span lang="vi" class="calibre2"> trước về Quốc-Uy </span><i lang="vi" class="calibre6">(phủ)</i><span lang="vi" class="calibre2">.</span></p>
	<p class="block_18"><span lang="vi" class="calibre2">Phú-xuyên </span><i lang="vi" class="calibre6">(huyện)</i><span lang="vi" class="calibre2"> Thường-Tín </span><i lang="vi" class="calibre6">(phủ) </i><sup lang="vi" class="calibre4"><a href="index_split_071.html#note_15" title="15" class="noteref"><sup id="back_note_15" class="calibre5">15</sup></a></sup><span lang="vi" class="calibre2"> Thanh-Trì, </span><i lang="vi" class="calibre6">(huyện, thuộc Sơn-tây)</i></p>
	<p class="block_18"><span lang="vi" class="calibre2">Ứng-Hòa </span><i lang="vi" class="calibre6">(phủ)</i><span lang="vi" class="calibre2"> Sơn-Lãng </span><i lang="vi" class="calibre6">(huyện) </i><sup lang="vi" class="calibre4"><a href="index_split_072.html#note_16" title="16" class="noteref"><sup id="back_note_16" class="calibre5">16</sup></a></sup><span lang="vi" class="calibre2"> nữa thì Thanh-Oai.</span></p>
	<p class="block_18"><span lang="vi" class="calibre2">Mỹ-Đức </span><i lang="vi" class="calibre6">(phủ)</i><span lang="vi" class="calibre2"> kiêm An-Đức </span><i lang="vi" class="calibre6">(huyện)</i><span lang="vi" class="calibre2"> kia,</span></p>
	<p class="block_18"><span lang="vi" class="calibre2">Lại còn Trương-Mỹ </span><i lang="vi" class="calibre6">(huyện)</i><span lang="vi" class="calibre2"> chi chi đó mà.</span></p>
	<p class="block_18"><span lang="vi" class="calibre2">Lĩnh, the, Bưởi, Phúc, Mỗ, La </span><i lang="vi" class="calibre6">(làng làm cửi)</i><span lang="vi" class="calibre2">.</span></p>
	<p class="block_18"><span lang="vi" class="calibre2">Tơ Bùng, lụa Giá, nữa là vải Canh. </span><i lang="vi" class="calibre6">(3 làng làm tơ lụa vải có tiếng)</i></p>
	<p class="block_18" lang="vi">Làng Quang trái vải ngon lành,</p>
	<p class="block_18"><span lang="vi" class="calibre2">Cốm thơm Dịch-Vong </span><i lang="vi" class="calibre6">(làng)</i><span lang="vi" class="calibre2"> đã rành nổi danh.</span></p>
	<p class="block_18"><span lang="vi" class="calibre2">Ghép lông đan chữ Phú-Vinh, </span><i lang="vi" class="calibre6">(làng)</i><span lang="vi" class="calibre2">.</span></p>
	<p class="block_18"><span lang="vi" class="calibre2">Sá-cừ </span><i lang="vi" class="calibre6">(làng Chuôn)</i><span lang="vi" class="calibre2"> nón-lá </span><i lang="vi" class="calibre6">(làng Vanh)</i><span lang="vi" class="calibre2"> ra hình khéo thay.</span></p>
	<p class="block_18"><span lang="vi" class="calibre2">Nhị-Khê </span><i lang="vi" class="calibre6">(làng)</i><span lang="vi" class="calibre2"> thợ tiện đâu tầy,</span></p>
	<p class="block_18"><span lang="vi" class="calibre2">Thợ thêu Tam-Xá </span><i lang="vi" class="calibre6">(làng)</i><span lang="vi" class="calibre2"> võng này Võ-Lăng </span><i lang="vi" class="calibre6">(làng)</i><span lang="vi" class="calibre2">.</span></p>
	<p class="block_18"><span lang="vi" class="calibre2">Đồ sơn Hà-Vĩ </span><i lang="vi" class="calibre6">(làng)</i><span lang="vi" class="calibre2"> thực rằng,</span></p>
	<p class="block_18"><span lang="vi" class="calibre2">Cống </span><i lang="vi" class="calibre6">(làng)</i><span lang="vi" class="calibre2"> nề, Chiếc </span><i lang="vi" class="calibre6">(làng)</i><span lang="vi" class="calibre2"> mộc, sao bằng Mậu-Lương </span><i lang="vi" class="calibre6">(làng)</i><span lang="vi" class="calibre2">.</span></p>
	<p class="block_18" lang="vi">Núi thì Tiên, Tuyết, chùa Hương,</p>
	<p class="block_18"><span lang="vi" class="calibre2">Sông Tô, Nhị, Nhuệ khác nhường Kim-Ngưu </span><i lang="vi" class="calibre6">(sông)</i><span lang="vi" class="calibre2">.</span></p>
	</body></html>


Then I provide a text which needs to be corrected as its content predicted from non-perfect OCR tool. Please use html content as reference source to correct below input text:
<input-text>
*Cốm thơm Dịch-Vọng (làng) đã rành nồi danh. Ghép lông đan chữ Phú-Vinh, (làng). Så-cừ (làng Chuôn) nón-lá (làng Vanh) ra hình khéo thay. Nhị-Khê (làng) thợ tiện đầu tây,
</input-text>

Strictly keep the orthography (and punctuation) of the reference, only correct based on what existed on input text. Answer corrected text.
"""

# Call the OpenAI API to generate the corrected text
response = client.chat.completions.create(
    model="gpt-4o",
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
