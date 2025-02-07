import requests
import openpyxl





def download_file(access_token, drive_id, file_id, file_path):
    try:
        url = f"https://graph.microsoft.com/v1.0/drives/{drive_id}/items/{file_id}"
        headers = {"Authorization": f"Bearer {access_token}"}
        response = requests.get(url, headers=headers)
        response.raise_for_status()
        download_url = response.json().get("@microsoft.graph.downloadUrl")
        if not download_url:
            raise ValueError("fill to get the download link")
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
        
        sheet.cell(row=2, column=1, value="10086")
        wb.save(file_path)
        print("Excel 文件修改完成")
    except Exception as e:
        print(f"Excel sorry fail: {e}")

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
            print("upload success")
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
