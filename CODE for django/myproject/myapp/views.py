# Create your views here.
from django.shortcuts import render, HttpResponse
from .models import TodoItem



    
def todos(request):
    items = TodoItem.objects.all()
    return render(request, "todos.html", {"todos": items})

from .forms import CustomerInfoForm

from django.shortcuts import render
from .forms import CustomerInfoForm

def home_view(request):
    print("Request method:", request.method)  # 打印请求方法
    if request.method == 'POST':
        print("POST data:", request.POST)  # 打印 POST 提交的数据
        form = CustomerInfoForm(request.POST)
        if form.is_valid():
            print("Form is valid")  # 表单通过验证
            form.save()
            return render(request, 'home.html', {'form': CustomerInfoForm(), 'success': True})
        else:
            print("Form is invalid:", form.errors)  # 表单错误信息
    else:
        print("GET request received")  # 如果是 GET 请求
        form = CustomerInfoForm()

    # 打印表单实例传递前的信息
    print("Form being passed to template:", form)

    return render(request, 'home.html', {'form': form, 'success': False})




import json
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .models import CopilotResponse, CustomerInfo

@csrf_exempt
def receive_input(request):
    if request.method == 'POST':
        try:
            # 解析 JSON 数据
            data = json.loads(request.body.decode('utf-8'))
            user_input = data.get('user_input', '')
        except json.JSONDecodeError:
            return JsonResponse({'error': '无效的 JSON 数据'}, status=400)

        if not user_input:
            return JsonResponse({'error': '输入不能为空'}, status=400)

        
        customer_name = "0"  # 固定客户名称
        try:
            customer_info = CustomerInfo.objects.get(customer_name=customer_name)
        except CustomerInfo.DoesNotExist:
            return JsonResponse({'error': f'客户 "{customer_name}" 不存在'}, status=404)

        # 更新或创建 CopilotResponse 数据
        copilot_response, created = CopilotResponse.objects.get_or_create(customer_info=customer_info)
        copilot_response.response_data = user_input
        copilot_response.save()

        return JsonResponse({'message': f'已存储数据: {copilot_response.response_data}'})

    return JsonResponse({'error': '只支持 POST 请求'}, status=405)

from django.http import JsonResponse

def oauth_callback(request):
    # 从回调中获取授权码
    code = request.GET.get('code')
    state = request.GET.get('state')

    if not code:
        return JsonResponse({'error': 'No authorization code provided'}, status=400)

    # 打印授权码，或者直接返回响应
    return JsonResponse({'code': code, 'state': state})


# views.py

from django.shortcuts import render
from .forms import CustomerInfoForm
from .models import CustomerInfo
from .utils import download_file, update_excel_from_db, upload_file
from django.http import HttpResponse

ACCESS_TOKEN = ""
FILE_ID = "01LWEDPEJZLVSJGXPKQNH2B32G5FFZ442B"  
FILE_PATH = "downloaded_excel.xlsx"  
DRIVE_ID = "b!LDBIbCR_YkeeJTnANM_gKWXzvtV4e0RJtUdriN9IejunRy_ANqNUQZVZx-_arhvd" 
def submit_customer_info(request):
    if request.method == "POST":
        form = CustomerInfoForm(request.POST)
        if form.is_valid():
            # 保存表单数据到数据库
            form.save()

            # 下载最新的 Excel 文件
            download_file(ACCESS_TOKEN, DRIVE_ID, FILE_ID, FILE_PATH)

            # 更新 Excel 文件
            update_excel_from_db(FILE_PATH)

            # 上传更新后的 Excel 文件
            upload_file(ACCESS_TOKEN, DRIVE_ID, FILE_ID, FILE_PATH)

            return HttpResponse("Customer data submitted and Excel updated successfully!")
    else:
        form = CustomerInfoForm()

    return render(request, 'submit_customer_info.html', {'form': form})
