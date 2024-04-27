import requests

# insert
def insert_to_queue():
    url = 'https://xxx.com/release/insert/'
    data = {'uid': 'sbsbsb', 'cid':'cid1','inputtext': 'Test message'}
    response = requests.post(url, data={'insertContent':str(data)})
    # response = requests.get(url)
    print(response)
    # print("返回的text:", response.text)
    print("返回的JSON数据:", response.json())

# pop
def pop_from_queue():
    url = 'https://xxx.com/release/pop/'
    response = requests.get(url)
    print("返回的JSON数据:", response.json())

# 执行测试
# insert_to_queue()
pop_from_queue()
