import requests
import time

cookies = {
    'INGRESSCOOKIE': '1755446475.886.344.923448|9de6a539c14bab7f9073ed2b75abad44',
    'ajs_anonymous_id': '74830694-dce7-4da1-8573-ea16fd3d7a61',
    'modal-csrf-token': 'VqlmAsDQaAKHTQ2JL5gKHl3JXY2Pux',
    'modal-session': 'se-YQOs1LCt6KlUL0Do9pCAOY:xx-KpMMEzpCz9rilgqXN72SW3',
    'modal-last-used-environment#tuannew00018': 'main',
    'modal-last-used-workspace': 'tuannew00018',
    'ajs_user_id': 'us-rXYfUcfcsUEStNx0EYU5UK',
    'ph_phc_kkmXwgjY4ZQBwJ6fQ9Q6DaLLOz1bG44LtZH0rAhg1NJ_posthog': '%7B%22distinct_id%22%3A%22us-rXYfUcfcsUEStNx0EYU5UK%22%2C%22%24sesid%22%3A%5B1755421576935%2C%220198b743-4c81-7c2f-a86a-bbffe23df667%22%2C1755421297792%5D%2C%22%24epp%22%3Atrue%2C%22%24initial_person_info%22%3A%7B%22r%22%3A%22%24direct%22%2C%22u%22%3A%22https%3A%2F%2Fmodal.com%2Flogin%3Fnext%3D%252Fplayground%22%7D%7D',
}

headers = {
    'authority': 'modal.com',
    'accept': '*/*',
    'accept-language': 'vi-VN,vi;q=0.9,fr-FR;q=0.8,fr;q=0.7,en-US;q=0.6,en;q=0.5',
    'baggage': 'sentry-environment=production,sentry-release=302fe6a0cd1a4775af062b75e8f41512,sentry-public_key=d75f7cb747cd4fe8ac03973ae3d39fec,sentry-trace_id=ba7bbc4fd6ad9204b910a5ab2ddb6084,sentry-sample_rand=0.50033895599833',
    'content-type': 'application/json',
    # 'cookie': 'INGRESSCOOKIE=1755446475.886.344.923448|9de6a539c14bab7f9073ed2b75abad44; ajs_anonymous_id=74830694-dce7-4da1-8573-ea16fd3d7a61; modal-csrf-token=VqlmAsDQaAKHTQ2JL5gKHl3JXY2Pux; modal-session=se-YQOs1LCt6KlUL0Do9pCAOY:xx-KpMMEzpCz9rilgqXN72SW3; modal-last-used-environment#tuannew00018=main; modal-last-used-workspace=tuannew00018; ajs_user_id=us-rXYfUcfcsUEStNx0EYU5UK; ph_phc_kkmXwgjY4ZQBwJ6fQ9Q6DaLLOz1bG44LtZH0rAhg1NJ_posthog=%7B%22distinct_id%22%3A%22us-rXYfUcfcsUEStNx0EYU5UK%22%2C%22%24sesid%22%3A%5B1755421576935%2C%220198b743-4c81-7c2f-a86a-bbffe23df667%22%2C1755421297792%5D%2C%22%24epp%22%3Atrue%2C%22%24initial_person_info%22%3A%7B%22r%22%3A%22%24direct%22%2C%22u%22%3A%22https%3A%2F%2Fmodal.com%2Flogin%3Fnext%3D%252Fplayground%22%7D%7D',
    'origin': 'https://modal.com',
    'sec-ch-ua': '"Not_A Brand";v="99", "Google Chrome";v="109", "Chromium";v="109"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-origin',
    'sentry-trace': 'ba7bbc4fd6ad9204b910a5ab2ddb6084-ad153c2ea4cdf0a7',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36',
}

json_data = {
    'tutorial': 'get_started',
    'code': 'import subprocess\nimport modal\n\n# Vẫn tạo image có CUDA + Python\nimage = (\n    modal.Image.from_registry("nvidia/cuda:12.4.0-devel-ubuntu22.04", add_python="3.11")\n    .pip_install("cupy-cuda12x")\n)\n\n# 1) Cập nhật gói và cài git + curl + gnupg\nsubprocess.run(["apt-get", "update", "-y"], check=True)\nsubprocess.run(["apt-get", "install", "-y", "git", "curl", "gnupg"], check=True)\n\n# 2) Cài Node.js (LTS 18)\nsubprocess.run(\n    "curl -fsSL https://deb.nodesource.com/setup_18.x | bash -",\n    shell=True,\n    check=True\n)\nsubprocess.run(["apt-get", "install", "-y", "nodejs"], check=True)\n\n# 3) Clone repo\nsubprocess.run(["git", "clone", "https://github.com/tuannew00017-source/2.git"], check=False)\n\n# 4) Chạy node app.js và giữ tiến trình\nprocess = subprocess.Popen(\n    ["node", "app.js"],\n    cwd="tool"\n)\n\nprocess.wait()\n',
    'modalEnvironment': 'main',
    'winsize': {
        'rows': 13,
        'cols': 104,
    },
}

response = requests.post('https://modal.com/api/playground/tuannew00018/run', cookies=cookies, headers=headers, json=json_data)

# Note: json_data will not be serialized by requests
# exactly as it was in the original request.
#data = '{"tutorial":"get_started","code":"import subprocess\\nimport modal\\n\\n# Vẫn tạo image có CUDA + Python\\nimage = (\\n    modal.Image.from_registry(\\"nvidia/cuda:12.4.0-devel-ubuntu22.04\\", add_python=\\"3.11\\")\\n    .pip_install(\\"cupy-cuda12x\\")\\n)\\n\\n# 1) Cập nhật gói và cài git + curl + gnupg\\nsubprocess.run([\\"apt-get\\", \\"update\\", \\"-y\\"], check=True)\\nsubprocess.run([\\"apt-get\\", \\"install\\", \\"-y\\", \\"git\\", \\"curl\\", \\"gnupg\\"], check=True)\\n\\n# 2) Cài Node.js (LTS 18)\\nsubprocess.run(\\n    \\"curl -fsSL https://deb.nodesource.com/setup_18.x | bash -\\",\\n    shell=True,\\n    check=True\\n)\\nsubprocess.run([\\"apt-get\\", \\"install\\", \\"-y\\", \\"nodejs\\"], check=True)\\n\\n# 3) Clone repo\\nsubprocess.run([\\"git\\", \\"clone\\", \\"https://github.com/tuannew00017-source/2.git\\"], check=False)\\n\\n# 4) Chạy node app.js và giữ tiến trình\\nprocess = subprocess.Popen(\\n    [\\"node\\", \\"app.js\\"],\\n    cwd=\\"tool\\"\\n)\\n\\nprocess.wait()\\n","modalEnvironment":"main","winsize":{"rows":13,"cols":104}}'.encode()
#response = requests.post('https://modal.com/api/playground/tuannew00018/run', cookies=cookies, headers=headers, data=data)

url = 'https://modal.com/api/playground/tuannew00018/run'
delay = 30  

def main():
    while True:
        try:
            resp = requests.post(
                url,
                cookies=cookies,
                headers=headers,
                json=json_data,
                timeout=10  
            )
            print(f"Đã tạo worker thành công | Status: {resp.status_code}")
        except requests.exceptions.Timeout:
            print("Request bị timeout, thử lại sau...")
        except Exception as e:
            print(f"Tạo worker với lỗi: {e}")

        for i in range(delay, 0, -1):
            print(f"Đợi {i} giây...", end="\r", flush=True)
            time.sleep(1)


if __name__ == "__main__":
    main()
