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
<h2 id="id_Toc498587537" class="block_17" lang="vi">ĐẠO HÀ-GIANG</h2>
	<p class="block_18" lang="vi">Hà-Giang một đạo kể đầu,</p>
	<p class="block_18" lang="vi">Ba trăm mười bẩy một mầu lâm loan.</p>
	<p class="block_18" lang="vi">Trước về ba đạo binh quan,</p>
	<p class="block_18" lang="vi">Thành-Thái thập bát văn-quan thay quyền.</p>
	<p class="block_18"><span lang="vi" class="calibre2">Vĩnh-Điện, Để-Định, Tương-An, </span><i lang="vi" class="calibre6">(ba phủ)</i><span lang="vi" class="calibre2">.</span></p>
	<p class="block_18" lang="vi">Bạc, vàng, thiếc, sắt, ở miền núi kia.</p>
	<p class="block_18"><span lang="vi" class="calibre2">Giới bia Đổ-Úm </span><i lang="vi" class="calibre6">(sông)</i><span lang="vi" class="calibre2"> phân chia,</span></p>
	<p class="block_18"><span lang="vi" class="calibre2">Tụ-Long </span><i lang="vi" class="calibre6">(đất)</i><span lang="vi" class="calibre2"> hai mỏ mất về nước Thanh.</span></p>
	<p class="block_18" lang="vi">Sông Ngâm, sông Chẩy rạo quanh,</p>
	<p class="block_18" lang="vi">Đến Đoan-Hùng phủ hợp ngành sông Lô.</p>
	<p class="block_18" lang="vi">Bảo-Lạc cũng một đất to.</p>
	<p class="block_18" lang="vi">Núi hoang rừng rậm tít mù viễn biên.</p>
	<p class="block_18"><span lang="vi" class="calibre2">Bắc-Quang </span><i lang="vi" class="calibre6">(đất)</i><span lang="vi" class="calibre2"> với huyện Vị-Xuyên,</span></p>
	<p class="block_18" lang="vi">An-Minh tổng mới và miền Đông-Ninh.</p>
	<p class="block_18" lang="vi">Tụ-Nhân tổng ở một mình,</p>
	<p class="block_18"><span lang="vi" class="calibre2">Thụ-Bờ </span><i lang="vi" class="calibre6">(đất)</i><span lang="vi" class="calibre2"> đại-lý có dinh đó mà.</span></p>
	<p class="block_18" lang="vi">Mỏ vàng, thiếc, bạc, thực là,</p>
	<p class="block_18" lang="vi">Sông Chòi, sông Chẩy lại hòa sông Sanh.</p>
	<p class="block_18" lang="vi">Phát nguyên cùng ở Đại-Thanh,</p>
	<p class="block_18" lang="vi">Hợp về cạnh tỉnh chẩy quanh bên ngoài.</p>
	</body></html>

Then I provide a text which needs to be corrected as its content predicted from non-perfect OCR tool. Please use html content as reference source to correct below input text:
<input-text>
Mỏ vàng, thiếc, bạc, thực là, Sòng Chòi, sòng Chảy lại hòa sông Sanh. Phát nguyên cùng ở Đại-Thanh, ·Hợp về cạnh tỉnh chảy quanh bên ngoài.
</input-text>

Strictly keep the orthography (and punctuation) of the reference, only correct based on what existed on input text carefully. Answer corrected text.
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