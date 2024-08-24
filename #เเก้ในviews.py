#หน้าหลักๆที่เราต้องเข้าไปเช็ค 
myproject 
-setting.py เพื่อให้แอปขึ้น
-urls.py เพื่อให้หน้าเเรกของเราขึ้นที่ไหน ส่วนใหญ่  "home.urls"
home แอปของเรา
urls.py เพื่อให้ลิ้งขึ้น
views.py เพื่อให้เชื่อมไปยังหน้าที่เราสร้าง
#เเก้ในviews อันนี้ ถ้ามีคนเรียกหรือกกดหน้า moblie ให้รีเควสไปที่ที่เราสร้าง เช่น moblie.html
from django.shortcuts import render
from django.http import HttpResponse
def about(request):
    return render(request,"about.html")
def moblie(request):
    return render(request,"moblie.html")
def  ชื่อที่เราตั้ง(request):
    return render(request,"ชื่อที่เราตั้ง.html")
#เเก้ในurls อันนี้คือลิ้ง ถ้ากดmoblie จะให้ไปเรียกหน้าviewเเละให้วิวทำงานต่อ
from django.urls import path
from home import views   
    path('', views.index),
    path('about/', views.about),
    path('moblie/', views.moblie),
    path('ใส่ชื่อที่เราตั้ง/',views.ชื่อที่เราตั้ง)
#เเก้ในbase ตรงนี้คือการเพิ่มปุ่มให้กดเเละเพิ่มลิ้งเช่น ปุ่ม moblie เเละเราสามารถกดเข้าไปได้ อันนี้จะไปลิ้งกัน urls 
<li class="nav-item">
<a class="nav-link" href="moblie/">
<i class="fas fa-fw fa-table"></i>
<span>moblie</span></a
 >
</li> 

<li class="nav-item">
    <a class="nav-link" href="ชื่อที่เราตั้ง/">
      <i class="fas fa-fw fa-table"></i>
     <span>ชื่อที่เราตั้ง</span></a
  >
</li>
#ถ้าสร้างแอปมาเเล้วให้เข้าไป setting ใน setting.py ใน myproject
 ตรง INSTALLED_APS 
 'home'
#ถ้าต้องการให้หน้าเเรกของเราขึ้นมาเลยต้องไป setting ใน urls.py ใน myproject
from django.urls import path,include
path('',include("home.urls")), 
'' คือหน้าเเรกให้ไปที่ home.urlsเลย
หน้า base.html คือพื้นหลัง ไม่ต้องเชื่อมพาส
