import webview
import os
import sys

# كود لجلب المسارات الصحيحة داخل التطبيق المستقل
def get_path(relative_path):
    if hasattr(sys, '_MEIPASS'):
        return os.path.join(sys._MEIPASS, relative_path)
    return os.path.join(os.path.abspath("."), relative_path)

# تحديد مكان ملف الـ HTML
html_path = get_path('index.html')

# تحديد مجلد دائم لحفظ الجلسة والذاكرة المحلية على جهاز المستخدم
storage_folder = os.path.join(os.path.expanduser('~'), '.orange_design_app_storage')

# إنشاء النافذة المستقلة
window = webview.create_window('Orange Design', html_path, width=900, height=800)

# تشغيل النافذة مع ربطها بمسار تخزين دائم لكي لا تضيع البيانات عند الإغلاق
webview.start(storage_path=storage_folder)