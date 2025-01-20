import requests
import openpyxl

# 配置信息
ACCESS_TOKEN = "eyJ0eXAiOiJKV1QiLCJub25jZSI6ImlWTU1vR3pzYTl3dzhxaGRPR3BvcDhhR3VzcTNhZGtUaU04M19adXBOckEiLCJhbGciOiJSUzI1NiIsIng1dCI6IllUY2VPNUlKeXlxUjZqekRTNWlBYnBlNDJKdyIsImtpZCI6IllUY2VPNUlKeXlxUjZqekRTNWlBYnBlNDJKdyJ9.eyJhdWQiOiJodHRwczovL2dyYXBoLm1pY3Jvc29mdC5jb20iLCJpc3MiOiJodHRwczovL3N0cy53aW5kb3dzLm5ldC83NmVlZWM0Ni1mZTQwLTRlMWItYWI0Mi0xZDZkOWY5MWI4YTkvIiwiaWF0IjoxNzM3MzY4NzcwLCJuYmYiOjE3MzczNjg3NzAsImV4cCI6MTczNzM3MzQwMywiYWNjdCI6MCwiYWNyIjoiMSIsImFpbyI6IkFUUUF5LzhaQUFBQVdiQU9QOGFzVXBaYjRhSWJNeGJPWGpjNkpvWUE5S256eG1iT3ZyOFd4bnBHQmRrREhGZDllQU8vMEtvdkJhd1giLCJhbXIiOlsicHdkIiwicnNhIl0sImFwcF9kaXNwbGF5bmFtZSI6InRlc3QgZm9yIGV4Y2VsIDIwMjUtMS0xOSIsImFwcGlkIjoiODI3NTVkYjUtY2QwMS00OTBjLTg4NGUtYmQ1YjRlMzk0ODBhIiwiYXBwaWRhY3IiOiIxIiwiZGV2aWNlaWQiOiJlN2JlYjRmOC00Yjk4LTQ4YzMtYjI0Ni03M2Q2ZjI1MDk3ZjMiLCJmYW1pbHlfbmFtZSI6Ikd1byBQZW5nemUiLCJnaXZlbl9uYW1lIjoiTGVtb24iLCJpZHR5cCI6InVzZXIiLCJpcGFkZHIiOiIyMDIuMTc1LjY3LjIxNyIsIm5hbWUiOiJMZW1vbiwgR3VvIFBlbmd6ZSIsIm9pZCI6ImQ0ZDhjZWI4LTkyYTEtNDZiNi1hNzI3LTgwNjA1NmU4NGI2NSIsIm9ucHJlbV9zaWQiOiJTLTEtNS0yMS0xNDAxMDU0NzUzLTcxMzk2MDMwMi04MzczMDA4MDUtMTU2MDcxIiwicGxhdGYiOiIzIiwicHVpZCI6IjEwMDMyMDAxNjU4RjE3MTgiLCJyaCI6IjEuQVZNQVJ1enVka0QtRzA2clFoMXRuNUc0cVFNQUFBQUFBQUFBd0FBQUFBQUFBQURGQUZkVEFBLiIsInNjcCI6ImVtYWlsIEZpbGVzLlJlYWRXcml0ZSBGaWxlcy5SZWFkV3JpdGUuQWxsIG9wZW5pZCBwcm9maWxlIFNpdGVzLlJlYWQuQWxsIFNpdGVzLlJlYWRXcml0ZS5BbGwiLCJzaWQiOiI5MDljYzU4YS1kMDZkLTQ4YmQtYWE5Zi00ZGEwN2I0NjFhZDUiLCJzaWduaW5fc3RhdGUiOlsia21zaSJdLCJzdWIiOiJQdkNmblA3cWdKbEFNVGdQVEgwOERhQVhfQklCX3gyR3lVSlpyZ1JQOEhvIiwidGVuYW50X3JlZ2lvbl9zY29wZSI6IkFTIiwidGlkIjoiNzZlZWVjNDYtZmU0MC00ZTFiLWFiNDItMWQ2ZDlmOTFiOGE5IiwidW5pcXVlX25hbWUiOiJkYzEyNzQ2QHVtLmVkdS5tbyIsInVwbiI6ImRjMTI3NDZAdW0uZWR1Lm1vIiwidXRpIjoianNKWVJRcXVaMFd3UEs5UEsybGJBQSIsInZlciI6IjEuMCIsIndpZHMiOlsiYjc5ZmJmNGQtM2VmOS00Njg5LTgxNDMtNzZiMTk0ZTg1NTA5Il0sInhtc19pZHJlbCI6IjEgMTYiLCJ4bXNfc3QiOnsic3ViIjoicVVmekpad2NjLU50X3ZPcFB4SGNGLTBaTWpXdVlocWhRR3psZGhMb3I0byJ9LCJ4bXNfdGNkdCI6MTQwODUyODE3OH0.bjzz6C4w3D2KCRB46sGYcuY4FxmYUBAVOuojcesyyjKznRx-nrW48WdXRpKA6N8etQsubAwCxZ6LolZdU67rDecKW_o275Kj_c1GSgipZui28QdGvaX_fwI0Y4qfQTxRyUVis_JlMS6TXq_CIWF1nmDh9zW2pbMgA9jFvqyCNribjtHsuhSaRLlNmvfvGd2wGZa6PIxv2nrSyHiY4it_zAqIKXctmjcS6xzwHecSG1Cs6kJ24LHk_uLMjZk1TQIWPwkHvehxPAS--WNW9o1xAhnKWVg4qDfPjZhVwykmlds9RIPsLizRp4aYvY7N0tyT8t8SjjjmcjO66NNEsee1IA"
DRIVE_ID = "b!LDBIbCR_YkeeJTnANM_gKWXzvtV4e0RJtUdriN9IejunRy_ANqNUQZVZx-_arhvd"  # 替换为实际的 Drive ID
FILE_ID = "01LWEDPEJZLVSJGXPKQNH2B32G5FFZ442B"  # 替换为实际的文件 ID
FILE_PATH = "downloaded_excel.xlsx"  # 下载后保存的本地文件名

# Step 1: 下载文件
def download_file(access_token, drive_id, file_id, file_path):
    try:
        # 获取文件的下载链接
        url = f"https://graph.microsoft.com/v1.0/drives/{drive_id}/items/{file_id}"
        headers = {"Authorization": f"Bearer {access_token}"}
        response = requests.get(url, headers=headers)
        response.raise_for_status()

        # 提取下载链接
        download_url = response.json().get("@microsoft.graph.downloadUrl")
        if not download_url:
            raise ValueError("未能获取文件的下载链接")

        # 下载文件并保存
        file_response = requests.get(download_url)
        file_response.raise_for_status()
        with open(file_path, "wb") as file:
            file.write(file_response.content)
        print(f"文件下载成功，保存为 {file_path}")
    except Exception as e:
        print(f"文件下载失败: {e}")

# Step 2: 修改文件
def modify_excel(file_path):
    try:
        wb = openpyxl.load_workbook(file_path)
        sheet = wb.active
        # 修改第 2 行第 1 列的值
        sheet.cell(row=2, column=1, value="10086")
        wb.save(file_path)
        print("Excel 文件修改完成")
    except Exception as e:
        print(f"Excel 文件修改失败: {e}")

# Step 3: 上传文件
def upload_file(access_token, drive_id, file_id, file_path):
    try:
        url = f"https://graph.microsoft.com/v1.0/drives/{drive_id}/items/{file_id}/content"
        headers = {
            "Authorization": f"Bearer {access_token}",
            "Content-Type": "application/octet-stream",
        }
        with open(file_path, "rb") as file:
            response = requests.put(url, headers=headers, data=file)
        if response.status_code == 200:
            print("文件上传成功")
        else:
            print(f"文件上传失败: {response.status_code}, {response.json()}")
    except Exception as e:
        print(f"文件上传失败: {e}")

# 主程序
if __name__ == "__main__":
    # Step 1: 下载文件
    download_file(ACCESS_TOKEN, DRIVE_ID, FILE_ID, FILE_PATH)

    # Step 2: 修改文件
    modify_excel(FILE_PATH)

    # Step 3: 上传文件
    upload_file(ACCESS_TOKEN, DRIVE_ID, FILE_ID, FILE_PATH)
