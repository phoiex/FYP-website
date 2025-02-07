import requests
import openpyxl


ACCESS_TOKEN = "eyJ0eXAiOiJKV1QiLCJub25jZSI6InlfTzQxa21NQzczZC1FTkZpZW1ET3NHemU1VDVhd1I2SHZvNzlUWTh3MnMiLCJhbGciOiJSUzI1NiIsIng1dCI6IllUY2VPNUlKeXlxUjZqekRTNWlBYnBlNDJKdyIsImtpZCI6IllUY2VPNUlKeXlxUjZqekRTNWlBYnBlNDJKdyJ9.eyJhdWQiOiJodHRwczovL2dyYXBoLm1pY3Jvc29mdC5jb20iLCJpc3MiOiJodHRwczovL3N0cy53aW5kb3dzLm5ldC83NmVlZWM0Ni1mZTQwLTRlMWItYWI0Mi0xZDZkOWY5MWI4YTkvIiwiaWF0IjoxNzM4MDM2NTI5LCJuYmYiOjE3MzgwMzY1MjksImV4cCI6MTczODA0MTUxNiwiYWNjdCI6MCwiYWNyIjoiMSIsImFpbyI6IkFUUUF5LzhaQUFBQWhkQ05JMzdBbnVtbDlYWGFLZytCZFkyeFAzdTVadVFDZjl5OVQvMXFQVFpsNHFZcWltVHJXZ1VsOG1zaDNSOFAiLCJhbXIiOlsicHdkIiwicnNhIl0sImFwcF9kaXNwbGF5bmFtZSI6InRlc3QgZm9yIGV4Y2VsIDIwMjUtMS0xOSIsImFwcGlkIjoiODI3NTVkYjUtY2QwMS00OTBjLTg4NGUtYmQ1YjRlMzk0ODBhIiwiYXBwaWRhY3IiOiIxIiwiZGV2aWNlaWQiOiJlN2JlYjRmOC00Yjk4LTQ4YzMtYjI0Ni03M2Q2ZjI1MDk3ZjMiLCJmYW1pbHlfbmFtZSI6Ikd1byBQZW5nemUiLCJnaXZlbl9uYW1lIjoiTGVtb24iLCJpZHR5cCI6InVzZXIiLCJpcGFkZHIiOiIxODMuMTk3LjQ2LjQxIiwibmFtZSI6IkxlbW9uLCBHdW8gUGVuZ3plIiwib2lkIjoiZDRkOGNlYjgtOTJhMS00NmI2LWE3MjctODA2MDU2ZTg0YjY1Iiwib25wcmVtX3NpZCI6IlMtMS01LTIxLTE0MDEwNTQ3NTMtNzEzOTYwMzAyLTgzNzMwMDgwNS0xNTYwNzEiLCJwbGF0ZiI6IjMiLCJwdWlkIjoiMTAwMzIwMDE2NThGMTcxOCIsInJoIjoiMS5BVk1BUnV6dWRrRC1HMDZyUWgxdG41RzRxUU1BQUFBQUFBQUF3QUFBQUFBQUFBREZBRmRUQUEuIiwic2NwIjoiZW1haWwgRmlsZXMuUmVhZFdyaXRlIEZpbGVzLlJlYWRXcml0ZS5BbGwgb3BlbmlkIHByb2ZpbGUgU2l0ZXMuUmVhZC5BbGwgU2l0ZXMuUmVhZFdyaXRlLkFsbCIsInNpZCI6IjkwOWNjNThhLWQwNmQtNDhiZC1hYTlmLTRkYTA3YjQ2MWFkNSIsInNpZ25pbl9zdGF0ZSI6WyJrbXNpIl0sInN1YiI6IlB2Q2ZuUDdxZ0psQU1UZ1BUSDA4RGFBWF9CSUJfeDJHeVVKWnJnUlA4SG8iLCJ0ZW5hbnRfcmVnaW9uX3Njb3BlIjoiQVMiLCJ0aWQiOiI3NmVlZWM0Ni1mZTQwLTRlMWItYWI0Mi0xZDZkOWY5MWI4YTkiLCJ1bmlxdWVfbmFtZSI6ImRjMTI3NDZAdW0uZWR1Lm1vIiwidXBuIjoiZGMxMjc0NkB1bS5lZHUubW8iLCJ1dGkiOiJtdHByR3JvVUhrbVRrS3ZoeWlvZ0FBIiwidmVyIjoiMS4wIiwid2lkcyI6WyJiNzlmYmY0ZC0zZWY5LTQ2ODktODE0My03NmIxOTRlODU1MDkiXSwieG1zX2lkcmVsIjoiMSAyNCIsInhtc19zdCI6eyJzdWIiOiJxVWZ6Slp3Y2MtTnRfdk9wUHhIY0YtMFpNald1WWhxaFFHemxkaExvcjRvIn0sInhtc190Y2R0IjoxNDA4NTI4MTc4fQ.NHBaK1CpM2I3v5fARWLECcz8sQR5GaZAbsesfdKte88hEAt80EpH29HtloRBu28qS1JxTq1EMwwmK3oLTcRKudHJjJqCxaMqDnSnAR9oUdij5pRB2lVMWAwp6iG_nJE5esnligVXDYdTkQFvv7UPTDNp9T5Z6xOO4I5eqJ61d05DwV_vWJHE0fPGn6IO-7qyz_8p83KWapwm-CffXj_67kylaeyRkZRNdWunw8uYzn9GWuq3sLAblHkSvoxS11AFW9I3EvpbIMHhmUYQq39To1m0wEZ_nC0IDw4_jpCDSn-DAXDzkEd8HYpwvKkKrzYneJQ_hnNVmrpCPXltwKUxHw"
DRIVE_ID = "b!LDBIbCR_YkeeJTnANM_gKWXzvtV4e0RJtUdriN9IejunRy_ANqNUQZVZx-_arhvd" 
FILE_ID = "01LWEDPEJZLVSJGXPKQNH2B32G5FFZ442B"  
FILE_PATH = "downloaded_excel.xlsx"  


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
