# Mblog
🍺 基于Django 3.0和python 3.7的博客系统

## 安装
安装 Django 3.0

```
pip install django==3.0
```
安装 Pillow 
```
pip install Pillow
```

## 数据库
修改项目`Mblog/settings.py`文件中的`DATABASES`
```
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'm_blog',
        'USER': '你的账号',
        'PASSWORD': '你的密码',
        'PORT': 3306,
        'HOST': 'IP'
    }
}
```
创建数据库
```sql
CREATE DATABASE m_blog
```

初始化数据库
```shell script
python manage.py makemigrations
python manage.py migrate
```

创建默认用户,按照提示输入账号密码
```shell script
python manage.py createsuperuser
```

## 运行
```shell script
python manage.py runserver
```
打开浏览器输入 `localhost:8000/admin` 打开后台页面
