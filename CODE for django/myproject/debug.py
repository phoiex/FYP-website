import os
import django

# 设置 Django 环境
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'myproject.settings')
django.setup()

# 导入你需要调试的模块
from myapp.forms import CustomerInfoForm

# 测试代码
form = CustomerInfoForm()
print(form)
