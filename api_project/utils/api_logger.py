import allure, json

def log_request(request):
    curl = f"curl -x {request.method} '{request.url}' \\\n"
    for key, value in request.headers.items():
        curl += f" -H '{key}: {value}' \\\n"
    if request.content:
        body = request.content.decode("utf-8")
        curl += f" -d '{body}' \\\n"
    allure.attach(curl, name="Request cURL", attachment_type=allure.attachment_type.TEXT)

def log_response(response):
    response.read()

    try:
        body = response.json()
        formatted_body = json.dumps(body, indent=4, ensure_ascii=False)
    except Exception:
        formatted_body = response.text
    log_info = f"URL: {response.url}\nStatus Code: {response.status_code}\nResponse Body: \n{formatted_body}"
    allure.attach(log_info, name="Response Data", attachment_type=allure.attachment_type.TEXT)
