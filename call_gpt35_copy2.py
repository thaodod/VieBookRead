from openai import OpenAI

# Initialize the OpenAI API client
client = OpenAI(
    # This is the default and can be omitted
    api_key="***REMOVED***",
)

# Define the prompt/question you want to ask
prompt = """
Given an html content as below:
<html xmlns="http://www.w3.org/1999/xhtml" lang="fr" xml:lang="fr">
  <head>
    <title>Inconnu(e)</title>
    <meta http-equiv="Content-Type" content="text/html; charset=utf-8"/>
  <link href="stylesheet.css" rel="stylesheet" type="text/css"/>
<link href="page_styles.css" rel="stylesheet" type="text/css"/>
</head>
  <body class="calibre">
<h1 id="id_Toc529041546" class="block_19" lang="vi">NHỮNG BÀI HỌC LỊCH-SỬ : DO NHỮNG NGUYÊN-NHÂN GÌ HỒ-QUÍ-LY THUA GIẶC MINH ?</h1>
	<h2 id="id_Toc529041547" class="block_20" lang="vi">Tổ-chức quốc-phòng của Hồ-Quí-Ly</h2>
	<p class="block_18" lang="vi">Từ khi nước Việt-Nam ta lập quốc đến giờ, có lẽ không thời nào công cuộc quốc-phòng được tổ chức mạnh mẽ, chu-đáo như thời nhà Hồ.</p>
	<p class="block_18" lang="vi">Ngay từ khi lên ngôi vua, trong nước còn thái bình, Hồ-quí-Ly đã lo tổ-chức nhân-dân về mặt quân-sự, và lo tổ-chức binh-bị để phòng giặc ngoại xâm.</p>
	<p class="block_18"><span lang="vi">Hồ-quí-Ly từng nói với triều-thần rằng </span>: « <i lang="vi" class="calibre4">Ta làm thế nào có 100 vạn quân để đánh giặc Bắc </i><i class="calibre4">? »</i></p>
	<p class="block_18" lang="vi">Rồi ra lệnh lập sổ hộ-tịch bắt người trong nước cứ từ hai tuổi trở lên là phải biên tên vào sổ, mục-đích kiểm-soát nhân-số, phòng khi quốc gia hữu sự thì gọi những người đến tuổi ra tòng quân. Do đó mà quân-số tăng lên rất nhiều.</p>
	<p class="block_18" lang="vi">Về thủy-quân, Hồ-quí-Ly sai làm những thuyền lớn trên có sàn lầu, ở dưới thì dành cho người chèo chống, rất tiện cho việc chiến đấu. Có thể nói rằng tới nhà Hồ, nước ta mới chính-thức tổ chức thủy-quân.</p>
	<p class="block_18" lang="vi">Việc phòng ngự trên mặt thủy cũng được tiến hành ráo riết. Ở các cửa biển và những chỗ hiểm yếu trong sông lớn, nhà vua đều sai lấy gỗ đóng cọc để ngăn tàu bè của giặc.</p>
	<p class="block_18" lang="vi">Tại Tây Đô (Thanh-Hóa), họ Hồ đặt ra bốn kho để chứa quân khí và lập binh-công-xưởng, sai những thợ lành nghề vào chế gươm súng.</p>
	<p class="block_18" lang="vi">Về bộ-binh thì chia ra vệ, đội, đại quân, trung quân, rất có kỷ-luật và quy-củ.</p>
	<p class="block_18" lang="vi">Xây thành Tây-Giai tức Tây-đô ở mạn rừng núi tỉnh Thanh-hóa (phủ Quảng Hóa giáp huyện Thạch Thành) qui mô rộng lớn, để thủ hiểm và phòng khi Đông-đô (tức Thăng Long, Hà-nội bây giờ) thất thủ thì dời vào Tây-đô.</p>
	<p class="block_18" lang="vi">Thời bình tổ chức quốc phòng như vậy ; khi có nạn ngoại-xâm đe dọa, công-cuộc phòng ngự tổ chức càng chu-đáo hơn.</p>
	<p class="block_18" lang="vi">Do việc chặn đánh quân Minh và bắt Trần-thiêm-Bình ở cửa Chi-Lăng, Hồ-quí-Ly đoán chắc thế nào rồi giặc Minh cũng sang đánh báo thù, nên ra lệnh chuẩn bị sẵn sàng kháng địch, đồng thời mở cuộc điều đình ngoại-giao với vua Minh.</p>
	<p class="block_18"><span lang="vi">Những phương sách chuẩn bị kháng địch họ Hồ đã áp-dụng là những phương sách sau này </span>:</p>
	<p class="block_18"><b lang="vi" class="calibre2">1)</b><span lang="vi"> Cho các vị công, hầu được quyền mộ lính, đặt những chức thiên-hộ, bá-hộ để cai quản những lính mộ đó.</span></p>
	<p class="block_18"><b lang="vi" class="calibre2">2)</b><span lang="vi"> Các cửa bể, cửa sông đóng cừ án ngữ rất vững. Riêng về phía nam sông Hồng-Hà đóng cừ dài hơn 700 dậm.</span></p>
	<p class="block_18"><b lang="vi" class="calibre2">3)</b><span lang="vi"> Ra lệnh cho dân ở Bắc-giang, Tam-Đái sang làm nhà sẵn ở phía Nam sông lớn, phòng khi giặc đến thì di-cư sang để tránh giặc.</span></p>
	<p class="block_18"><b lang="vi" class="calibre2">4)</b><span lang="vi"> Sai đắp thành Đa-Bang ở xã Cổ-Pháp, huyện Tiên-Phong, tỉnh Sơn-Tây bây giờ.</span></p>
	<p class="block_18"><b lang="vi" class="calibre2">5)</b><span lang="vi"> Ở Đa-Bang, lập đồn ải liên tiếp ở phía Nam sông Thao, sông Cái, và đóng cọc ở giữa sông không cho thuyền bè đi lại.</span></p>
	<p class="block_18" lang="vi">Tổ chức nhân-dân, xây dựng thủy-quân, bộ-quân, chế luyện võ khí và chuẩn bị phòng ngự như vậy, tưởng nước ta chưa bao giờ được phòng-thủ kiên-cố như đời nhà Hồ.</p>
	<h2 id="id_Toc529041548" class="block_20" lang="vi">Đánh nhau với giặc ba trận họ Hồ đã phải bắt</h2>
	<p class="block_18"><span lang="vi">Phòng bị cẩn mật ráo riết như thế, vậy mà đánh nhau với giặc </span><i lang="vi" class="calibre4">Minh</i><span lang="vi"> ba trận, họ Hồ thua cả ba, và rút cuộc, cha con Hồ-quí-Ly bị bắt sống.</span></p>
	<p class="block_18"><i lang="vi" class="calibre4">- Trận thứ nhất</i><span lang="vi"> </span><i lang="vi" class="calibre4">tức trận Đa-Bang</i><span lang="vi"> : Trước sức công phá dữ dội của giặc Minh dưới quyền điều khiển của hai tướng </span>:<span lang="vi"> Mộc Thạnh và Trương Phụ, thành Đa-Bang sau một ngày một đêm cầm cự đã bị thất thủ. Bao nhiêu đồn ải dọc bờ sông bị giặc đốt hết. Giặc thừa thắng kéo về chiếm cứ Đông-đô (Hà-nội). Quân nhà Hồ phải lui về giữ miền Hoàng-Giang tức là miệt huyện Nam-Xang tỉnh Hà-nam bây giờ.</span></p>
	<p class="block_18"><i lang="vi" class="calibre4">- Trận thứ hai</i><span lang="vi"> </span><i lang="vi" class="calibre4">tức trận Mộc-phàm giang</i><span lang="vi"> : Hồ-nguyên-Trừng con trưởng Hồ-quí-Ly thống lĩnh chiến thuyền đánh giặc ở Mộc-phàm giang kết quả bị giặc đánh đại bại.</span></p>
	<p class="block_18"><i lang="vi" class="calibre4">- Trận thứ ba tức trận Hàm-Tử quan </i>:<span lang="vi"> Thủy bộ quân của họ Hồ cộng hơn 7 vạn, giả xưng là 21 vạn, chia ra thủy bộ ba đường tiến đánh giặc Minh ở Hàm-Tử quan. Giặc Minh hai mặt xông lại đánh, quân bộ của họ Hồ thua to. Duy quân thủy là chạy thoát.</span></p>
	<p class="block_18" lang="vi">Sau ba trận đó, Hồ-quí-Ly chạy dài qua Thanh-Hóa vào Nghệ An, không chống với giặc Minh được trận nào, rồi cuối cùng cha con họ Hồ đều bị giặc Minh bắt sống.</p>
	<p class="block_18" lang="vi">Giặc Minh sang xâm lăng năm Bính Tuất (1406) đến năm Đinh Hợi (1407) trải ba trận giao chiến, đã diệt được họ Hồ và cướp được nước ta.</p>
	<p class="block_18" lang="vi">Tính ra cuộc chống giữ của họ Hồ chỉ được có hơn một năm trời, dù rằng công cuộc phòng bị đã tổ-chức cực kỳ chu đáo.</p>
	<h2 id="id_Toc529041549" class="block_20" lang="vi">Vì lẽ gì họ Hồ thua giặc Minh và thua mau như vậy ?</h2>
	<p class="block_18" lang="vi">Đối chiếu công cuộc quốc phòng với kết quả cuộc kháng chiến của họ Hồ, ai cũng muốn đặt câu hỏi như trên.</p>
	<p class="block_18"><span lang="vi">Phải, quân số như vậy, binh bị như vậy và công cuộc phòng thủ chuẩn bị như vậy, sao họ Hồ đánh ba trận lại thua cả ba và sau ba trận đó đã để non nước và chính thân mình lọt vào tay giặc </span>?</p>
	<p class="block_18"><span lang="vi">Chẳng có lẽ bằng ấy sự mưu toan, bằng ấy sự chuẩn bị lại chỉ đưa đến cái kết-quả như thế thôi </span>?<span lang="vi"> Chẳng có lẽ tất cả những công cuộc bố trí phòng ngự của họ Hồ lại chỉ có hình thức trên giấy tờ không có một tác-dụng gì về thực-tế ? Chẳng có lẽ, thật chẳng có lẽ nào </span>!<span lang="vi">… Người ta ai không muốn thở dài mà nói như vậy với một niềm than tiếc bâng khuâng.</span></p>
	<p class="block_18" lang="vi">Song xét ra, họ Hồ thất bại và thất bại mau chóng như vậy là đáng lắm.</p>
	<p class="block_18"><span lang="vi">Có lẽ lúc bị giặc bắt, họ Hồ cũng muốn kêu lên như Hạng-Võ thời xưa : </span>« <i lang="vi" class="calibre4">Thời bất lợi hề</i><i class="calibre4"> »</i><i lang="vi" class="calibre4"> </i><span lang="vi">hay </span>« <i lang="vi" class="calibre4">đó là lỗi ở thời chớ không phải lỗi ở kẻ dùng binh</i> »<span lang="vi">. Giá có kêu lên như vậy, thì họ Hồ cũng không sao đổ lỗi cho chữ </span>« <span lang="vi">Thời</span> »<span lang="vi"> hay chữ </span>« <span lang="vi">Trời</span> »<span lang="vi">. Vì thật ra, ở đây, cuộc thất bại đau đớn của họ Hồ không do </span>« <span lang="vi">Thời</span> »<span lang="vi"> mà cũng không do </span>« <span lang="vi">Trời</span> »<span lang="vi">. Do họ Hồ tự tạo ra cả.</span></p>
	<p class="block_18"><span lang="vi">Chúng ta không muốn trách Hồ-quí-Ly đã tiếm vị nhà Trần như ông Trần-trọng-Kim, tác-giả </span>« <span lang="vi">Việt Nam Sử-lược</span> »<span lang="vi">. Chúng ta cũng không muốn nói « chính sự nhà Hồ phiền hà</span> »<span lang="vi"> như cụ Nguyễn Trãi viết trong bài Bình Ngô Đại Cáo.</span></p>
	<p class="block_18" lang="vi">Buổi ấy, vua Nghệ-Tông nhà Trần thất chính, nếu ngôi vua không về họ Hồ, thì cũng đến về họ khác mà thôi. Và chính-sự nhà Hồ dù có phiền-hà, thì cũng chỉ phiền-hà đến cái mực phiền-hà như chính-sự nhà Lê sau này là cùng : đánh cờ, đánh bạc phải tội chặt ngón tay, chủ khách uống trà hay uống rượu với nhau từ bốn người trở lên bị phạt đánh 100 trượng.</p>
	<p class="block_18"><span lang="vi">Chúng ta chỉ muốn nói rằng họ Hồ sở dĩ thất bại đau đớn như vậy là vì hai cớ chính sau đây </span>:<span lang="vi"> </span><b lang="vi" class="calibre2">1)</b><span lang="vi"> </span><i lang="vi" class="calibre4">Họ Hồ vô chính trị</i><span lang="vi">. </span><b lang="vi" class="calibre2">2)</b><span lang="vi"> </span><i lang="vi" class="calibre4">Họ Hồ quan niệm lầm về việc dùng binh, hay vụng dùng binh.</i></p>
	<h3 id="id_Toc529041550" class="block_21" lang="vi">Họ Hồ vô chính trị như thế nào ?</h3>
	<p class="block_18" lang="vi">Ở đây, xin nhắc lại lần nữa, chúng ta không nói đến việc vô chính trị của họ Hồ đã cướp ngôi họ Trần một cách trâng tráo, thiếu sự vận-động khôn khéo, như kiểu Lê-đại-Hành thời trước hay Lê-Thái-Tổ sau này.</p>
	<p class="block_18" lang="vi">Chúng ta chỉ nói rằng Hồ-quí-Ly là một nhà chính trị quá ư cấp tiến, nên hóa vô chính trị. Thật vậy, bắt dân phải nộp vàng, bạc thật vào kho nhà vua, phát hành giấy bạc con rồng, con phượng, rêu bể, làn sóng buộc dân tiêu, buộc dân khai tên vào sổ hộ tịch, buộc dân nêu tên họ và diện tích từng thửa ruộng, những việc đó đều là những việc mới mẻ, văn minh thật đấy, nhưng xét theo tình-trạng nước nhà thời bấy giờ, thì những việc đó sao khỏi quá trớn, không sát với tình-trạng xã-hội thử thời. Nhất là trước khi thực hành những việc đó, họ Hồ lại không vận-động nhân-dân cho kỹ, cho chín, cho thấm nhuần đường lối chủ-trương của mình.</p>
	<p class="block_18" lang="vi">Thành ra những việc cải-cách quá trớn đó đã làm cho những địa chủ, phú nông, những nhà quyền quí thời ấy, vốn đã không ưa họ Hồ về việc tiếm nghịch, lại càng xa họ Hồ thêm, vì quyền lợi thiết thực của họ bị động chạm. Không vận-động nhân-dân vui lòng tuân theo những việc cải cách cấp tiến của mình, lúc bình thời đã đành, ngay lúc quốc-gia lâm nguy, giặc ngoại xâm thập thò cửa ngõ, Hồ-quí-Ly cũng sao lãng việc vận-động nhân-dân, không biết nêu cao đại-nghĩa bảo vệ Tổ-Quốc.</p>
	<p class="block_18"><span lang="vi">Trong hội-nghị các văn võ triều-thần bàn về việc giặc Minh xâm lấn, ý kiến mọi người không được vận-động từ trước, nên thiếu nhất-</span>tr<span lang="vi">í, kẻ bàn đánh, người bàn hòa, riêng có Quí-Ly nhất quyết định. Đến văn võ triều-thần lòng dạ còn phân chia như vậy, trách chi lòng dân không khảng-tảng ly tán </span>?</p>
	<p class="block_18"><span lang="vi">Nắm được chỗ yếu đó, giặc Minh vừa sang nước ta, đã thảo hịch kể tội họ Hồ và nêu cao việc quân Tàu sang diệt Hồ phù lập nhà Trần, ném tung ra khắp nhân-dân. Những mảnh ván viết hịch theo giòng nước trôi đến đâu quân sĩ nhà Hồ mất tinh-thần đến đấy. Nhiều người không đánh, trở giáo theo giặc Minh. Quân sĩ còn như vậy, huống chi là nhân-dân không thấy lợi gì trực-tiếp đến mình trong việc chống giặc </span>?</p>
	<p class="block_18" lang="vi">Tóm lại, họ Hồ thất bại một phần là do thất nhân tâm. Thất nhân tâm là vì họ Hồ hành động thiếu chính trị, không sát với nguyện vọng nhân-dân.</p>
	</body></html>

Then I provide a text which needs to be corrected as its content predicted from non-perfect OCR tool. Please use html content as reference source to correct below input text:
<input-text>
Dồi ra lệnh lập số hộ-tịch bắt người trong nước cứ từ hai tuổi trỏ lên là phải biên tên vào số, mụ - cđích kiểm-soát nhân - số, phòng khi
</input-text>

Strictly keep the orthography (and punctuation) of the reference, only correct based on what existed on input text carefully.
First word of the text could also be typo too, check all words and letters carefully equally.
Answer corrected text, important: Give only the processed result, without any explanations, formatting or XML-like tag.
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
    temperature=0.0
)

print(response.choices[0].message.content)