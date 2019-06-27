### 创建Django项目名为myweb
`django-admin startproject myweb`

### 启动项目
**eg: cd myweb**
`python manage.py runserver`

### 修改Django语言为汉语
位置：settings.py 文件内部
将**LANGUAGE_CODE**从 en-us 改为 zh-hans

### 创建名为app的应用
`python manage.py startapp app`
在app文件夹中的views.py添加如下内容：
```python
from django.http import HttpResponse


def index(request):
    return HttpResponse('<h3>Day1,Hello Django!</h3>')
```
在项目urls中添加：
```python
from app.views import index

urlpatterns = [
    path('admin/', admin.site.urls),
    path('index/', index),
]
```

在settings.py文件内部的**INSTALLED_APPS** 添加'app'

启动项目访问*http://127.0.0.1:8000/index/*
即可显示：Day1 ,Hello Django