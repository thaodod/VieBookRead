# first trial, quite okay
"""
Given an html file:
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
Đo ra mới biết núi càng là cao. Đến như duyên-cách thế nào, Diễn ra từng tỉnh chép vào nhời ca. Trong Nam các tỉnh đặt ra,
</input-text>

Please don't add more text, only correct based on what existed on input text. Answer corrected text.
"""


# best trial, so far gpt3.5
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

# another test case for all LLMs
"""
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
Cống (làng) nề, Chiếc (làng) mộc, sao bằng Mậu- Núi thì Tiên, Tuyết, chùa Hương, Lương (làng). Sống Tô, Nhị, Nhuệ khác nhường Kim-Ngưu ( sông).
</input-text>

Strictly keep the orthography (and punctuation) of the reference, only correct based on what existed on input text carefully. Answer corrected text.
"""

# another test case
"""
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
Cốm thơm Dịch-Vọng (làng) đã rành nồi danh. Ghép lông đan chữ Phú-Vinh, (làng). Så-cừ (làng Chuôn) nón-lá (làng Vanh) ra hình khéo thay. Nhị-Khê (làng) thợ tiện đầu tây,
</input-text>

Strictly keep the orthography (and punctuation) of the reference, only correct based on what existed on input text. Answer corrected text only.
"""



# failed cases for GPT3.5 but Haiku still makes it. The case first letter of the para is modified.
"""
Given an html content:
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
	<h3 id="id_Toc529041551" class="block_21" lang="vi">Họ Hồ vụng dùng binh như thế nào ?</h3>
	<p class="block_18" lang="vi">Họ Hồ thất bại một phần nữa là vì vụng dùng binh hay là dùng binh không sát hợp với tình-trạng và hoàn-cảnh trong nước.</p>
	<p class="block_18"><span lang="vi">Ta có thể phân tách những vụng về, lầm lỗi trong việc dùng binh của họ Hồ ra như sau này </span>:</p>
	<p class="block_15" lang="vi">1) Quan niệm sai lầm về chiến-lược, chiến-thuật</p>
	<p class="block_18" lang="vi">Địa thế nước nhà đất đai nhỏ hẹp, lại lắm rừng nhiều núi, không thuận tiện cho trận địa chiến (chiến tranh dàn thành mặt trận hẳn hoi) chỉ thuận tiện cho du kích chiến và du kích vận-động chiến cùng phục kích chiến mà thôi.</p>
	<p class="block_18"><span lang="vi">Đời Trần, Hưng-Đạo-Vương sở dĩ thắng được giặc Mông-Cổ là vì Ngài đã biết « </span><i lang="vi" class="calibre4">lấy đoản binh chống với tràng trận</i><span lang="vi"> » tức là lấy nhu thắng cương, lấy nhược thắng cường, lấy du kích chiến chọi với quân giặc ham trận địa chiến, như lời Ngài đã trối lại cho vua Trần-Anh-Tông.</span></p>
	<p class="block_18" lang="vi">Sau nhà Hồ, vua Lê-Thái-Tổ, mười năm chống giặc Minh cũng áp-dụng chiến-lược đánh lâu dài và áp-dụng chiến-thuật du kích, phục kích.</p>
	<p class="block_18"><span lang="vi">Cả đến vua Quang-Trung sau này nữa, sở dĩ đại phá được giặc Thanh cũng là vì áp-dụng được triệt để nguyên-tắc « </span><i lang="vi" class="calibre4">xuất kỳ bất ý, công ký vô bị</i><span lang="vi"> » tức là phép đánh du kích trong binh pháp Tôn Ngô.</span></p>
	<p class="block_18"><span lang="vi">Đầu này Hồ-quí-Ly lại quan niệm lầm rằng phải lấy cương chống với cương, lấy trận địa chiến chống với trận địa chiến. Bởi quan niệm sai lầm về phép dùng binh của nước nhỏ chống với nước mạnh, của dân vắng chống với dân đông, như thế, nên Hồ-quí-Ly mới ngày đêm ước ao có « </span><i lang="vi" class="calibre4">100 vạn quân để chống giặc Bắc</i><span lang="vi"> », không biết rằng Hưng-Đạo-Vương đã nói </span>:<span lang="vi"> « </span><i lang="vi" class="calibre4">Binh cốt giỏi không cốt nhiều, nếu nhiều mà không giỏi thì dù có trăm vạn quân cũng không làm gì</i> »<span lang="vi">.</span></p>
	<p class="block_18" lang="vi">Bởi quan niệm thiên về trận địa chiến, nên họ Hồ mới sai đắp thành Đa-Bang, mới lập đồn ải suốt dọc sông, mới đường hoàng kéo đại đội thủy, lục quân tiến đánh giặc Minh ở Hàm-tử Quan.</p>
	<p class="block_18" lang="vi">Họ Hồ không biết rằng khi giặc cứng như đá, mà mình lại dùng cứng chống lại thì không thể được. Vì nước mình người vắng, quân ít, cái cứng của mình đối với giặc Minh chỉ là cái cứng của trứng chọi với đá mà thôi. Dùng trận địa chiến đánh giặc Tàu bất luận ở thời nào trong lịch-sử đều không thể thủ thắng được.</p>
	<p class="block_18" lang="vi">Chiến-thuật đã quan niệm sai, mà chiến-lược lại quan niệm không đúng.</p>
	<p class="block_18" lang="vi">Thấy giặc Minh ồ-ạt kéo sang định nuốt chửng nước mình ngay, họ Hồ cũng dại dột định dùng chiến-lược đánh chóng thắng chóng, ào-ạt chống lại quân giặc, muốn chỉ một vài trận là đánh bại được giặc thù. Họ Hồ không biết tránh mũi nhọn của kẻ thù, trái lại cả gan xông vào đón lấy mũi nhọn ấy.</p>
	<p class="block_18" lang="vi">Họ Hồ không biết rằng đối với chiến-lược « tốc chiến tốc quyết » của giặc, mình phải dùng chiến-lược « đánh lâu dài » đặng làm tiêu mòn dần quân giặc, nhiên hậu mới có thể tiêu diệt chúng được.</p>
	<p class="block_18" lang="vi">Chiến-thuật, chiến-lược đã sai lầm thì kết-quả không bao giờ là thắng lợi được.</p>
	<p class="block_15" lang="vi">2) Không biết lợi dụng địa lợi và thiên thời</p>
	<p class="block_18"><span lang="vi">Đã hành động nhiều điều vô chính trị, để đến nỗi thất nhân tâm, tức là thiếu mất yếu tố « </span><i lang="vi" class="calibre4">nhân hòa</i><span lang="vi"> » là điều thiệt thòi</span> r<span lang="vi">ất lớn rồi, mà về mặt quân sự, họ Hồ lại không biết lợi dụng triệt để hai yếu tố </span>« <i lang="vi" class="calibre4">Thiên Thời</i><i class="calibre4"> »</i><span lang="vi"> và </span>« <i lang="vi" class="calibre4">Địa Lợi</i><i class="calibre4"> »</i><span lang="vi">.</span></p>
	<p class="block_18" lang="vi">Chủ trương trận địa chiến, lấy trứng chọi với đá, Hồ-quí-Ly không chú trọng đến du kích chiến và phục kích chiến, nên mới bỏ miền rừng núi, về « chọi » nhau với giặc ở mạn đồng bằng. Thành thử trước số đông quân giặc như hùm như beo, quân mình không được địa-hình, địa-vật rất tốt của rừng núi che chở cho.</p>
	<p class="block_18" lang="vi">Họ Hồ không hiểu rằng những trận quyết-định trong lịch sử thắng lợi của quân ta bao giờ cũng diễn ra trên những địa điểm hiểm-yếu như ải Chi-Lăng chẳng hạn. Bởi không hiểu thế cho nên khi lui về Tây-Đô là nơi hiểm yếu giáp rừng núi mạn Thanh-Hóa, mà Hồ-quí-Ly vẫn cứ đường hoàng chống giặc và chạy dài, không biết lui vào núi rừng tổ chức du kích chiến.</p>
	<p class="block_18"><span lang="vi">Đã để mất hai điều lợi lớn là </span><i lang="vi" class="calibre4">Nhân-Hòa</i><span lang="vi">, </span><i lang="vi" class="calibre4">Địa-Lợi</i><span lang="vi">, họ Hồ lại không biết lợi dụng </span><i lang="vi" class="calibre4">Thiên-Thời</i><span lang="vi">.</span></p>
	<p class="block_18" lang="vi">Đời Trần, Hưng-Đạo-Vương sở dĩ thắng giặc Nguyên cũng một phần vì biết chờ tiết mùa hè nóng bức, giặc Nguyên không quen thủy thổ sinh ra đau ốm rất nhiều, bấy giờ mới đánh cho giặc những đòn chí tử.</p>
	<p class="block_18"><span lang="vi">Sao họ Hồ không biết tạm lui để đợi khi quân giặc thủy thổ bất phục, bấy giờ mới tung quân ra phản công ? Xét ra cũng chỉ vì quan-niệm sai lầm về chiến-lược, chiến-thuật nên Hồ mới bỏ nốt cả hai yếu-tố lợi hại vô cùng cho việc dụng binh là </span><i lang="vi" class="calibre4">Thiên thời</i><span lang="vi">, </span><i lang="vi" class="calibre4">Địa lợi</i><span lang="vi">.</span></p>
	<p class="block_15" lang="vi">3) Ỷ vào quân số, võ khí, chiến cụ và công sự phòng ngự</p>
	<p class="block_18" lang="vi">Họ Hồ chỉ lo làm sao có 100 vạn quân. Như thế tức là chủ trương ỷ lại vào quân số, cho rằng hễ có nhiều quân tất nhiên là đánh thắng.</p>
	<p class="block_18" lang="vi">Họ Hồ sai đóng chiến thuyền, lập binh công xưởng chế tạo võ khí, xây đắp thành trì và đóng cừ chống giặc là ỷ-lại vào võ khí, chiến-cụ và công-sự.</p>
	<p class="block_18" lang="vi">Họ Hồ không biết rằng quân số trội, võ khí nhiều, công sự chắc chắn, mà quân sĩ thiếu tinh-thần, nhân-dân không ủng-hộ thì cũng bằng thừa mà thôi.</p>
	<p class="block_18"><span lang="vi">Muốn nhân-dân ủng-hộ thì phải vận-động nhân-dân và áp-dụng một đường lối chính trị khôn khéo, đừng độc-tài, chớ quá trớn. Muốn quân sĩ có tinh-thần, thì như lời Hưng-Đạo-Vương đã nói </span>:<span lang="vi"> </span>« T<span lang="vi">ướng với quân phải như cha con một nhà</span> »<span lang="vi">.</span></p>
	<p class="block_18" lang="vi">Một đạo quân với những vũ-khí đầy đủ, công sự chắc chắn, mà không có tinh-thần, thì cũng như cái xác không hồn, không thể làm nên công chuyện chi hết.</p>
	<p class="block_9" lang="vi">*</p>
	<p class="block_18"><b lang="vi" class="calibre2">TÓM LẠI</b><span lang="vi">, họ Hồ bị thua giặc Minh một cách mau lẹ như vậy là vì họ Hồ vô chính trị đối với nhân-dân lúc bình thời, và không biết dùng binh sát với tình-thế và hoàn-cảnh trong nước.</span></p>
	<p class="block_18" lang="vi">Nói một cách khác, họ Hồ đã khờ khạo không biết rút những kinh-nghiệm kháng địch đời Trần để đem áp-dụng đối với giặc Minh.</p>
	<p class="block_18"><span lang="vi">Và chính bởi thế mà họ Hồ thất bại, chớ họ Hồ không thất bại vì đã cướp ngôi nhà Trần, như ý ông Trần-trọng-Kim muốn nói trong « Việt-Nam Sử-lược</span> »<span lang="vi">.</span></p>
	</body></html>

Then I provide a text which needs to be corrected as its content predicted from non-perfect OCR tool. Please use html content as reference source to correct below input text:
<input-text>
Pồi ra lệnh lập số hộ-tịch bắt người trong nước cứ từ hai tuổi trỏ lên là phải biên tên vào số, mụ - cđích kiểm-soát nhân - số, phòng khi
</input-text>

Strictly keep the orthography (and punctuation) of the reference, only correct based on what existed on input text carefully. Answer corrected text.
"""