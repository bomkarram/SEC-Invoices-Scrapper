# SEC Invoices Scrapper
## عن البرنامج
عن طريق اعطاء البرنامج قائمة بارقام حسابات الكهرباء سيتم تفحص كل حساب آلياً و إعداد تقرير إكسل يحتوي قيمة الفاتورة لكل حساب و هل كونه سدد أم لا

## متطلبات التشغيل
Python 3.6
(Chromedriver)[http://chromedriver.chromium.org/downloads]
متصفح كروم

## طريقة عمل البرنامج
عن طريق سطر الاوامر
`git clone `
`cd SEC-Invoices-Scrapper`
`python -m venv py`
`source py/bin/activate`
`pip install -r requirements.txt `
ضع ارقام الحسابات المراد تفحصها في ملف private_data.py
ملاحظة: كل موقع في الملف سيتم وضعه في sheet مختلف في ملف الاكسل
`python main.py`

## صور البرنامج

## صور نتيجة البرنامج