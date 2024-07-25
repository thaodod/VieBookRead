from openai import OpenAI

client = OpenAI(
    api_key="***REMOVED***",
)


PROMPT = """
Given A text as below:
<A-text>
Lâm vua được 3 ngày chưa kịp đổi niên hiện, thì Quảng Trị bị Trịnh duy Đại là anh Trịnh duy Sản bắt vào Tây đồ (Thanh Hóa) rồi mấy ngày sau bị giết chết.
</A-text>

and B text as below:
<B-text>
Quang-Trị làm vua được 3 ngày chưa kịp đổi niên hiệu thì Quang-Trị bị Trịnh-duy-Đại là anh Trịnh-duy-Sản bắt vào Tây-Đô (Thanh-Hóa) rồi mấy ngày sau bị giết chết.
</B-text>

Compare and cut off the B text to have similar length with A text.
Give only the processed result, without any explanations, formatting or tag.
"""


completion = client.chat.completions.create(
    model="gpt-4o-mini",
    messages=[
        {"role": "system", "content": "Assist user to process text"},
        {"role": "user", "content": PROMPT},
    ],
    temperature=0.0,
)

print(completion.choices[0].message.content)
