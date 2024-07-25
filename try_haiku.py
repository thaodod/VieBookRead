from anthropic import AnthropicVertex

PROMPT = """
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

Then I provide a text which needs to be corrected as it is predicted from imperfect OCR tool. Use html content as reference source to correct below input text:
<input-text>
Dồi ra lệnh lập số hộ-tịch bắt người trong nước cứ từ hai tuổi trở lên là phải biên tên vào số, mụ - cđích kiểm-soát nhân - số, phòng khi
</input-text>

Strictly keep the orthography (and punctuation) of the reference, only correct based on what existed on input text carefully.
First word of the text could also be typo too, check all words and letters carefully equally.
Answer corrected text, important: Give only the processed result, without any explanations, formatting or XML-like tag.
"""

PROMPT = """
Given an retrieved html content as below:
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

Then providing a text gererated by imperfect OCR tool having typo or mis-recognized problems sometimes, as below:
<input-text>
Tiên Sư Cổ Miếu
</input-text>

Please check if the input text is relevant or not in the given retrieved html. Answer shortly (yes/no) without any explanations, formatting.
"""


LOCATION="us-central1" # or "europe-west4"

client = AnthropicVertex(region=LOCATION, project_id="***REMOVED***")

message = client.messages.create(
  messages=[
    {
      "role": "user",
      "content": PROMPT,
    }
  ],
  model="claude-3-haiku@20240307",
  max_tokens=1024,
  temperature=0.0
)
print(message.content[0].text)