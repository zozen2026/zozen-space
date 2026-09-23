import os
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import openai

app = FastAPI(title="Zozen AI Engine")

# ضَع مفتاح قروك الخاص بك هنا أو استدعِه من متغيرات البيئة
XAI_API_KEY = os.getenv("XAI_API_KEY", "ضع_مفتاح_قروك_هنا")

client = openai.OpenAI(
    api_key=XAI_API_KEY,
    base_url="https://api.xai.com/v1",
)

# نظام التوجيه والشخصية الخاصة بـ Zozen AI
ZOZEN_SYSTEM_PROMPT = """
أنت Zozen AI، المساعد الذكي المخصص لمنصة "زوزين".
تتحدث بأسلوب فريد، متزن، ومباشر دون تقليد أي ذكاء اصطناعي آخر.

القواعد الصارمة:
1. التكيف اللغوي: تجيب فوراً بنفس اللغة التي يتحدث بها المستخدم (عربي، إنجليزي، روسي، أو غيرها).
2. حظر تام ومطلق لمواضيع البرمجة والأكواد:
   - يُمنع منعاً باتاً كتابة أي كود برمجي، أو شرح كيفية بناء المواقع، أو تطوير التطبيقات، أو التحدث عن لغات البرمجة والسيرفرات.
   - إذا سألك المستخدم عن البرمجة أو التطوير أو الأكواد، أجب برفض صريح ومؤدب مثل:
     "أنا هنا للمساعدة في المعرفة العامة ومحتوى منصة زوزين فقط، ولا أقدم معلومات أو إرشادات تتعلق بالبرمجة أو تطوير التطبيقات والمواقع."
3. تقديم المعرفة العامة والإجابات بدقة مع الالتزام بقيم المنصة.
"""

class ChatRequest(BaseModel):
    user_id: str
    message: str

@app.post("/api/zozen-ai")
async def chat_with_zozen(request: ChatRequest):
    try:
        response = client.chat.completions.create(
            model="grok-beta",
            messages=[
                {"role": "system", "content": ZOZEN_SYSTEM_PROMPT},
                {"role": "user", "content": request.message}
            ],
            temperature=0.7
        )
        
        reply = response.choices[0].message.content
        return {"status": "success", "reply": reply}
        
    except Exception as e:
        raise HTTPException(status_code=500, detail="حدث خطأ في الاتصال بالنموذج")