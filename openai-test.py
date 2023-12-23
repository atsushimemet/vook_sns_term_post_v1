from openai import OpenAI

from vook_sns_term_post_v1.config.config import *  # noqa

client = OpenAI()

brand = "Levi's"
item = "Denim Pants"
term = "赤耳"
str_limit = 175


role_content = f"あなたは{brand}のヴィンテージに精通している専門家です。"
prompt = f"{brand}のf{item}に関連する{term}という用語について、{str_limit}文字以内かつ日本語で、用語説明テキストを生成してください。生成した文章が{str_limit}を超えている場合は、生成し直してください。"

completion = client.chat.completions.create(
    model="gpt-3.5-turbo",
    messages=[
        {
            "role": "system",
            "content": role_content,
        },
        {
            "role": "user",
            "content": prompt,
        },
    ],
)
content = completion.choices[0].message.content
print(f"以下のテキストが出力されました。文字数は{len(content)}でした。\n{content}")
