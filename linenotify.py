#%%
import requests,time
token = "jNhqz7VGffsQ9LxQv5aBZ2vqIvQ5gPWKc9SpJIyrMZf"
url = "https://notify-api.line.me/api/notify"
headers = {"Authorization": "Bearer " + token}
payload = {"message": "テストメッセージだよ"}
requests.post(url, headers=headers, data=payload)

if True:
    time.sleep(4)
    next

test={"message":"ydy"}
requests.post(url, headers=headers, data=test)

# %%
