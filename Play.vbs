Set WshShell = CreateObject("WScript.Shell")
Set fso = CreateObject("Scripting.FileSystemObject")

' 1. تحديد مجلد العمل الحالي للملفات
currentDir = fso.GetParentFolderName(WScript.ScriptFullName)
WshShell.CurrentDirectory = currentDir

' 2. تشغيل ملف الباتش بالخلفية
WshShell.Run "Run.bat", 0, False

' 3. كشف لغة النظام واختيار الرسالة
On Error Resume Next
sysLang = Left(WshShell.RegRead("HKCU\Control Panel\International\LocaleName"), 2)
If Err.Number <> 0 Then sysLang = "en"
On Error GoTo 0

If sysLang = "ar" Then
    msg = "تم تشغيل المنصة بنجاح."
    title = "إشعار"
Else
    msg = "The platform has been launched successfully."
    title = "Notice"
End If

' 4. عرض رسالة النجاح
MsgBox msg, 64, title

' 5. فتح صفحة البداية عبر المتصفح الافتراضي لجهازك
WshShell.Run "cmd.exe /c start index.html", 0, False

' تنظيف الذاكرة
Set WshShell = Nothing
Set fso = Nothing