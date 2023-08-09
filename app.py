from flask import Flask, request, jsonify
import requests
import base64

app = Flask(__name__)

GITHUB_TOKEN = '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'
REPO = 'Mr-KID-github/answer.ai'
API_URL_TEMPLATE = 'https://api.github.com/repos/{}/contents/{}'


@app.route('/upload', methods=['POST'])
def upload():
    # 获取图片文件
    image_file = request.files.get('image')
    
    # 将图片转换为 base64
    image_data = base64.b64encode(image_file.read()).decode('utf-8')
    
    # 定义 GitHub API URL
    image_name = image_file.filename
    github_api_url = API_URL_TEMPLATE.format(REPO, f'images/{image_name}')

    # 使用 GitHub API 创建或更新文件
    headers = {
        "Authorization": f"Bearer {GITHUB_TOKEN}",
        "Accept": "application/vnd.github+json",
        "X-GitHub-Api-Version": "2022-11-28"
    }
    data = {
        "message": f"Upload {image_name}",
        "content": image_data
    }
    
    response = requests.put(github_api_url, headers=headers, json=data)
    
    if response.status_code == 200 or response.status_code == 201:
        return jsonify(success=True, url=response.json()['content']['download_url'])
    else:
        return jsonify(success=False, message="Upload failed"), 400


if __name__ == '__main__':
    app.run(debug=True)
