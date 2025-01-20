import requests
from msal import ConfidentialClientApplication
import json

# Azure 应用配置信息
CLIENT_ID = "82755db5-cd01-490c-884e-bd5b4e39480a"
CLIENT_SECRET = "aoO8Q~_zWiyVIrz5jL~VSt6NFcqa_pCauOC95aqp"
TENANT_ID = "76eeec46-fe40-4e1b-ab42-1d6d9f91b8a9"
AUTHORITY = f"https://login.microsoftonline.com/{TENANT_ID}"
SCOPES = ["https://graph.microsoft.com/.default"]

# 获取访问令牌
def get_access_token():
    app = ConfidentialClientApplication(
        CLIENT_ID,
        authority=AUTHORITY,
        client_credential=CLIENT_SECRET
    )
    token_response = app.acquire_token_for_client(scopes=SCOPES)
    return token_response.get("access_token")

# 获取 SharePoint 文件 ID
def get_file_id(access_token, site_url, file_path):
    headers = {"Authorization": f"Bearer {access_token}"}
    site_response = requests.get(f"https://graph.microsoft.com/v1.0/sites/root:/{site_url}:", headers=headers)
    site_data = site_response.json()

    site_id = site_data["id"]
    drive_response = requests.get(f"https://graph.microsoft.com/v1.0/sites/{site_id}/drive/root:/{file_path}", headers=headers)
    drive_data = drive_response.json()

    return drive_data.get("id")

# 读取第一行第一列的内容
def read_first_cell(access_token, site_url, file_path, sheet_name):
    file_id = get_file_id(access_token, site_url, file_path)
    headers = {"Authorization": f"Bearer {access_token}"}

    # 获取第一行第一列数据 (A1)
    excel_url = f"https://graph.microsoft.com/v1.0/drives/{file_id}/workbook/worksheets('{sheet_name}')/range(address='A1')"
    response = requests.get(excel_url, headers=headers)
    
    if response.status_code == 200:
        data = response.json()
        return data.get("text")
    else:
        print(f"读取 Excel 失败，状态码：{response.status_code}, 错误信息：{response.json()}")
        return None

# 写入第一行第二列
def write_to_second_cell(access_token, site_url, file_path, sheet_name, value):
    file_id = get_file_id(access_token, site_url, file_path)
    headers = {
        "Authorization": f"Bearer {access_token}",
        "Content-Type": "application/json"
    }

    # 写入数据到 B1
    excel_url = f"https://graph.microsoft.com/v1.0/drives/{file_id}/workbook/worksheets('{sheet_name}')/range(address='B1')"
    body = {
        "values": [[value]]
    }
    response = requests.patch(excel_url, headers=headers, json=body)

    if response.status_code == 200:
        print("写入成功")
    else:
        print(f"写入失败，状态码：{response.status_code}, 错误信息：{response.json()}")

# 主函数
if __name__ == "__main__":
    # 配置 SharePoint 的路径
    SHAREPOINT_SITE = "sites/SoftwareProjectDMSystem"  # SharePoint 网站路径
    FILE_PATH = "test for excel connection.xlsx"  # 文件路径
    SHEET_NAME = "Sheet1"  # 工作表名称

    # 获取访问令牌
    token = get_access_token()

    # 读取第一行第一列
    first_cell_value = read_first_cell(token, SHAREPOINT_SITE, FILE_PATH, SHEET_NAME)
    print(f"第一行第一列的值是：{first_cell_value}")

    # 写入第一行第二列
    write_to_second_cell(token, SHAREPOINT_SITE, FILE_PATH, SHEET_NAME, 10086)