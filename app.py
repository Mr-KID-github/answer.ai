from flask import Flask, request, jsonify
import requests
import base64
import time
import uuid

app = Flask(__name__)

GITHUB_TOKEN = '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'
REPO = 'Mr-KID-github/answer.ai'
API_URL_TEMPLATE = 'https://api.github.com/repos/{}/contents/{}'

def generate_unique_filename(original_filename):
    ext = original_filename.split('.')[-1]
    timestamp = str(int(time.time()))
    unique_id = uuid.uuid4().hex
    return f"{timestamp}-{unique_id}.{ext}"

def use_mathAPI(image_url):
    print("调用Math API")
    MATH_API_URL = "https://math.rockeyops.com/api/v1/math/solve"
    MATH_API_HEADERS = {
        "x-app-id": "math-app",
        "x-app-key": "7a6c508f25324c3d36c46c409c4f7f2b",
        "Content-Type": "application/json"
    }
    # 调用数学 API
    math_api_data = {
        "stream": False,
        "url": image_url
    }
    math_response = requests.post(MATH_API_URL, headers=MATH_API_HEADERS, json=math_api_data)
    print(math_response)
    return math_response


@app.route('/upload', methods=['POST'])
def upload():
    print("调用upload方法")
    # 获取图片文件
    image_file = request.files.get('image')
    if not image_file:
        print ("not image_file")
        return jsonify(success=False, message="No image provided"), 400
    print ("get image_file")

    unique_filename = generate_unique_filename(image_file.filename)
    
    # 将图片转换为 base64
    image_data = base64.b64encode(image_file.read()).decode('utf-8')
    
    # 定义 GitHub API URL
    github_api_url = API_URL_TEMPLATE.format(REPO, f'images/{unique_filename}')


    # 使用 GitHub API 创建或更新文件
    headers = {
        "Authorization": f"Bearer {GITHUB_TOKEN}",
        "Accept": "application/vnd.github+json",
        "X-GitHub-Api-Version": "2022-11-28"
    }
    data = {
        "message": f"Upload {unique_filename}",
        "content": image_data
    }
    
    github_response = requests.put(github_api_url, headers=headers, json=data)
    
    if github_response.status_code not in [200, 201]:
        return jsonify(success=False, message="Upload to GitHub failed"), 400

    # 获取 GitHub 图片 URL
    image_url = github_response.json()['content']['download_url']

    return image_url

    # math_response = use_mathAPI(image_url)
    # if math_response.status_code == 200:
    #     return jsonify(success=True, result=math_response.json())
    # else:
    #     return jsonify(success=False, message="Math API call failed", error=math_response.text), 500


if __name__ == '__main__':
    print("Hello flask")
    app.run(debug=True)
