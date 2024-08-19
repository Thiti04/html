#เเก้ในviews
def about(request):
    return render(request,"about.html")
def moblie(request):
    return render(request,"moblie.html")
def  ชื่อที่เราตั้ง(request):
    return render(request,"ชื่อที่เราตั้ง.html")
#เเก้ในurls
    path('', views.index),
    path('about/', views.about),
    path('moblie/', views.moblie),
    path('ใส่ชื่อที่เราตั้ง',views.ชื่อที่เราตั้ง)
#เเก้ในbase
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
     