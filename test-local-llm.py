# -*- coding: utf-8 -*-
"""
Created on Tue Jun  4 17:23:21 2024

@author: thao
"""

# Example: reuse your existing OpenAI setup
from openai import OpenAI

# Point to the local server
client = OpenAI(base_url="http://localhost:1234/v1", api_key="lm-studio")

completion = client.chat.completions.create(
  model="lmstudio-community/Meta-Llama-3-8B-Instruct-GGUF",
  messages=[
    {"role": "system", "content": "Always answer in short"},
    {"role": "user", "content": 
"""
Find (match) the longest matched part of a given long-text which it is most similar to my modified sequence. Answer only the text (just copy from the long-text)

The given long-text to search on:
<start text>
NHỮNG BÀI HỌC LỊCH-SỬ : DO NHỮNG NGUYÊN-NHÂN GÌ HỒ-QUÍ-LY THUA GIẶC MINH ?

Tổ-chức quốc-phòng của Hồ-Quí-Ly

Từ khi nước Việt-Nam ta lập quốc đến giờ, có lẽ không thời nào công cuộc quốc-phòng được tổ chức mạnh mẽ, chu-đáo như thời nhà Hồ.

Ngay từ khi lên ngôi vua, trong nước còn thái bình, Hồ-quí-Ly đã lo tổ-chức nhân-dân về mặt quân-sự, và lo tổ-chức binh-bị để phòng giặc ngoại xâm.

Hồ-quí-Ly từng nói với triều-thần rằng : « Ta làm thế nào có 100 vạn quân để đánh giặc Bắc ? »

Rồi ra lệnh lập sổ hộ-tịch bắt người trong nước cứ từ hai tuổi trở lên là phải biên tên vào sổ, mục-đích kiểm-soát nhân-số, phòng khi quốc gia hữu sự thì gọi những người đến tuổi ra tòng quân. Do đó mà quân-số tăng lên rất nhiều.

Về thủy-quân, Hồ-quí-Ly sai làm những thuyền lớn trên có sàn lầu, ở dưới thì dành cho người chèo chống, rất tiện cho việc chiến đấu. Có thể nói rằng tới nhà Hồ, nước ta mới chính-thức tổ chức thủy-quân.

Việc phòng ngự trên mặt thủy cũng được tiến hành ráo riết. Ở các cửa biển và những chỗ hiểm yếu trong sông lớn, nhà vua đều sai lấy gỗ đóng cọc để ngăn tàu bè của giặc.
<end text>

Example 1:
The modified:
<start modified>
Ho-qui-Ly ting nói vó'i trieu than räng:
<end modified>

Expected answer:
<start answer>
Hồ-quí-Ly từng nói với triều-thần rằng :
<end answer>

Example 2:
<start modified>
T is den khi nuroc ta lap quoc gio, có le khong tho' não cong cuoc quoc-phong dure to chúrc manh mê, chu-dão nhu thoi nhà Hö. Ngay tir khi len ngoi vua, trong nuro con thái binh, Hö-qui-Ly da lo tö-churc nhan dàn vè mat quan-sir và lo to-chirc binh-bi de phong giãc ngoai xâm,
<end modified>

Expected answer:
<start answer>
Từ khi nước Việt-Nam ta lập quốc đến giờ, có lẽ không thời nào công cuộc quốc-phòng được tổ chức mạnh mẽ, chu-đáo như thời nhà Hồ.

Ngay từ khi lên ngôi vua, trong nước còn thái bình, Hồ-quí-Ly đã lo tổ-chức nhân-dân về mặt quân-sự, và lo tổ-chức binh-bị để phòng giặc ngoại xâm.
<end answer>


Example 3:
<start modified>
Röi ra lênh làp so h - tich bät nguroi trong nuoc cú tür hai tuoi tró lên là phai biên ten vao sö, mu-cdich - kiem-soat nhan - so, - phong khi
<end modified>

Expected answer:
<start answer>
Rồi ra lệnh lập sổ hộ-tịch bắt người trong nước cứ từ hai tuổi trở lên là phải biên tên vào sổ, mục-đích kiểm-soát nhân-số, phòng khi
<end answer>

now do for this modified:
<start modified>
quoc gia hiru su thi goi nhürng nguoi. den tuoi ra tong quin. Db dó m' quan-sô täng len rát nhieu.
<end modified>
"""
     }
  ],
  temperature=0.0,
)

print(completion.choices[0].message)