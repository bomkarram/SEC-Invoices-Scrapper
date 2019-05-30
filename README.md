<div style="direction: rtl; text-align: right">

# SEC Invoices Scrapper
## عن البرنامج
عن طريق اعطاء البرنامج قائمة بارقام حسابات الكهرباء سيتم تفحص كل حساب آلياً و إعداد تقرير إكسل يحتوي قيمة الفاتورة لكل حساب و هل كونه سدد أم لا

## متطلبات التشغيل
Python 3.6 <br>
[Chromedriver](http://chromedriver.chromium.org/downloads) <br>
متصفح كروم <br>

## طريقة عمل البرنامج
 عن طريق سطر الاوامر <br>
`git clone https://github.com/bomkarram/SEC-Invoices-Scrapper.git` <br>
`cd SEC-Invoices-Scrapper` <br>
`python -m venv py` <br>
`source py/bin/activate` <br>
`pip install -r requirements.txt ` <br>
ضع ارقام الحسابات المراد تفحصها في ملف private_data.py <br>
`python main.py` <br>
ملاحظة: كل موقع في الملف سيتم وضعه في sheet مختلف في ملف الاكسل <br>

## صور البرنامج
![](https://github.com/bomkarram/SEC-Invoices-Scrapper/raw/master/Screenshots/Screen%20Shot%202019-05-30%20at%208.27.57%20AM.png)
## صور نتيجة البرنامج
![](https://github.com/bomkarram/SEC-Invoices-Scrapper/raw/master/Screenshots/Screen%20Shot%202019-05-30%20at%208.41.58%20AM.png)

</div>
