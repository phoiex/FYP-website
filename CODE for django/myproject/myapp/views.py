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

ACCESS_TOKEN = "eyJ0eXAiOiJKV1QiLCJub25jZSI6IkJrMG9XdXFJS1JTbVJrTVhaTFYwOXdWaS1hTl9SeFlOQlN3a2FuQlJXUjQiLCJhbGciOiJSUzI1NiIsIng1dCI6IllUY2VPNUlKeXlxUjZqekRTNWlBYnBlNDJKdyIsImtpZCI6IllUY2VPNUlKeXlxUjZqekRTNWlBYnBlNDJKdyJ9.eyJhdWQiOiJodHRwczovL2dyYXBoLm1pY3Jvc29mdC5jb20iLCJpc3MiOiJodHRwczovL3N0cy53aW5kb3dzLm5ldC83NmVlZWM0Ni1mZTQwLTRlMWItYWI0Mi0xZDZkOWY5MWI4YTkvIiwiaWF0IjoxNzM4OTIxMjQ1LCJuYmYiOjE3Mzg5MjEyNDUsImV4cCI6MTczODkyNTQ3NiwiYWNjdCI6MCwiYWNyIjoiMSIsImFpbyI6IkFXUUFtLzhaQUFBQU9sUWpXRWZ2QlQ5M1lWYS93aGR0aTRtR2FJMVcyM05PYmVZOHlHQXo1MXNrREVzeHp4S3ZYOGsrMlNLN3g3SGFJMVhxWDVDMkR0L1IxVXdmdTc0Q2xiS0piN2kwT0xET3VHZ2xyRUE4TmxVRUxsODBuVkc1bUNpczdRVmd2K2FwIiwiYW1yIjpbInB3ZCIsInJzYSJdLCJhcHBfZGlzcGxheW5hbWUiOiJ0ZXN0IGZvciBleGNlbCAyMDI1LTEtMTkiLCJhcHBpZCI6IjgyNzU1ZGI1LWNkMDEtNDkwYy04ODRlLWJkNWI0ZTM5NDgwYSIsImFwcGlkYWNyIjoiMSIsImRldmljZWlkIjoiZTdiZWI0ZjgtNGI5OC00OGMzLWIyNDYtNzNkNmYyNTA5N2YzIiwiZmFtaWx5X25hbWUiOiJHdW8gUGVuZ3plIiwiZ2l2ZW5fbmFtZSI6IkxlbW9uIiwiaWR0eXAiOiJ1c2VyIiwiaXBhZGRyIjoiMTQ5LjEwMi45OC4xODIiLCJuYW1lIjoiTGVtb24sIEd1byBQZW5nemUiLCJvaWQiOiJkNGQ4Y2ViOC05MmExLTQ2YjYtYTcyNy04MDYwNTZlODRiNjUiLCJvbnByZW1fc2lkIjoiUy0xLTUtMjEtMTQwMTA1NDc1My03MTM5NjAzMDItODM3MzAwODA1LTE1NjA3MSIsInBsYXRmIjoiMyIsInB1aWQiOiIxMDAzMjAwMTY1OEYxNzE4IiwicmgiOiIxLkFWTUFSdXp1ZGtELUcwNnJRaDF0bjVHNHFRTUFBQUFBQUFBQXdBQUFBQUFBQUFERkFGZFRBQS4iLCJzY3AiOiJlbWFpbCBGaWxlcy5SZWFkV3JpdGUgRmlsZXMuUmVhZFdyaXRlLkFsbCBvcGVuaWQgcHJvZmlsZSBTaXRlcy5SZWFkLkFsbCBTaXRlcy5SZWFkV3JpdGUuQWxsIiwic2lkIjoiOTA5Y2M1OGEtZDA2ZC00OGJkLWFhOWYtNGRhMDdiNDYxYWQ1Iiwic2lnbmluX3N0YXRlIjpbImttc2kiXSwic3ViIjoiUHZDZm5QN3FnSmxBTVRnUFRIMDhEYUFYX0JJQl94Mkd5VUpacmdSUDhIbyIsInRlbmFudF9yZWdpb25fc2NvcGUiOiJBUyIsInRpZCI6Ijc2ZWVlYzQ2LWZlNDAtNGUxYi1hYjQyLTFkNmQ5ZjkxYjhhOSIsInVuaXF1ZV9uYW1lIjoiZGMxMjc0NkB1bS5lZHUubW8iLCJ1cG4iOiJkYzEyNzQ2QHVtLmVkdS5tbyIsInV0aSI6IldJWTY5QXR0clVXQXliWlZteDJiQUEiLCJ2ZXIiOiIxLjAiLCJ3aWRzIjpbImI3OWZiZjRkLTNlZjktNDY4OS04MTQzLTc2YjE5NGU4NTUwOSJdLCJ4bXNfaWRyZWwiOiIxIDI2IiwieG1zX3N0Ijp7InN1YiI6InFVZnpKWndjYy1OdF92T3BQeEhjRi0wWk1qV3VZaHFoUUd6bGRoTG9yNG8ifSwieG1zX3RjZHQiOjE0MDg1MjgxNzh9.RHaZ3Ofu9szqu87J6fP-t0lRGcATd2QbJdE0rmBu7gj8EE2X6eBBDpPWcCv579hVnHnM0mu9EP00rHVQr1BNs5ZKsoR0wh8uLznHAnVEqol2ICLZK-ai9E7NyD766rRfvvj3ioqAup3gxhpOzP4YPbqfKHJd-xs00NrnLl2l7lm84rBT7iGMmEZoL969fOSpkYNHjGuQ_BazVRRKwcQ2ugCu2K9pA1LeH_iqJpgDCVZZ8hkRn6o3DnxIgt5CH4B_JSZU_ax-Ci5yVhoBzfzMuFj7J88T4ADhwDGSdolbI1Qu6NHbn-A8h4BWJLTsEvW-iwBZpd4Zso40JHczMTUOXg"
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
