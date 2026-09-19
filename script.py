import tkinter as tk
from tkinter import messagebox
import locale

def run_app():
    # كشف لغة الجهاز
    lang = locale.getdefaultlocale()[0]
    is_arabic = lang and lang.startswith('ar')

    # النصوص
    title = "إشعار" if is_arabic else "Notice"
    msg = "تم تشغيل التطبيق بنجاح." if is_arabic else "The application has been launched successfully."

    # عرض الرسالة
    root = tk.Tk()
    root.withdraw()
    messagebox.showinfo(title, msg)
    root.destroy()