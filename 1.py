import requests
import time
cookies = {
    'ajs_anonymous_id': '74830694-dce7-4da1-8573-ea16fd3d7a61',
    'modal-session': 'se-YQOs1LCt6KlUL0Do9pCAOY:xx-KpMMEzpCz9rilgqXN72SW3',
    'modal-last-used-environment#tuannew00018': 'main',
    'modal-last-used-workspace': 'tuannew00018',
    'ajs_user_id': 'us-rXYfUcfcsUEStNx0EYU5UK',
    'INGRESSCOOKIE': '1755478648.002.344.508826|9de6a539c14bab7f9073ed2b75abad44',
    'ph_phc_kkmXwgjY4ZQBwJ6fQ9Q6DaLLOz1bG44LtZH0rAhg1NJ_posthog': '%7B%22distinct_id%22%3A%22us-rXYfUcfcsUEStNx0EYU5UK%22%2C%22%24sesid%22%3A%5B1755510344763%2C%220198bc8f-08be-7676-8758-e00a4f0b4cbd%22%2C1755510147262%5D%2C%22%24epp%22%3Atrue%2C%22%24initial_person_info%22%3A%7B%22r%22%3A%22%24direct%22%2C%22u%22%3A%22https%3A%2F%2Fmodal.com%2Flogin%3Fnext%3D%252Fplayground%22%7D%7D',
}

headers = {
    'authority': 'modal.com',
    'accept': '*/*',
    'accept-language': 'vi-VN,vi;q=0.9,fr-FR;q=0.8,fr;q=0.7,en-US;q=0.6,en;q=0.5',
    'baggage': 'sentry-environment=production,sentry-release=68d8bbe0cf03427e9d3481f07e7d5444,sentry-public_key=d75f7cb747cd4fe8ac03973ae3d39fec,sentry-trace_id=3916953c111fe34d17248e7e2dd82e57,sentry-sample_rand=0.5717865226593994',
    'content-type': 'application/json',
    # 'cookie': 'ajs_anonymous_id=74830694-dce7-4da1-8573-ea16fd3d7a61; modal-session=se-YQOs1LCt6KlUL0Do9pCAOY:xx-KpMMEzpCz9rilgqXN72SW3; modal-last-used-environment#tuannew00018=main; modal-last-used-workspace=tuannew00018; ajs_user_id=us-rXYfUcfcsUEStNx0EYU5UK; INGRESSCOOKIE=1755478648.002.344.508826|9de6a539c14bab7f9073ed2b75abad44; ph_phc_kkmXwgjY4ZQBwJ6fQ9Q6DaLLOz1bG44LtZH0rAhg1NJ_posthog=%7B%22distinct_id%22%3A%22us-rXYfUcfcsUEStNx0EYU5UK%22%2C%22%24sesid%22%3A%5B1755510344763%2C%220198bc8f-08be-7676-8758-e00a4f0b4cbd%22%2C1755510147262%5D%2C%22%24epp%22%3Atrue%2C%22%24initial_person_info%22%3A%7B%22r%22%3A%22%24direct%22%2C%22u%22%3A%22https%3A%2F%2Fmodal.com%2Flogin%3Fnext%3D%252Fplayground%22%7D%7D',
    'origin': 'https://modal.com',
    'sec-ch-ua': '"Not_A Brand";v="99", "Google Chrome";v="109", "Chromium";v="109"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-origin',
    'sentry-trace': '3916953c111fe34d17248e7e2dd82e57-85f56b183301dc91',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36',
}

json_data = {
    'tutorial': 'get_started',
    'code': 'import subprocess\n\nimport modal\n\n\n\n# Vẫn tạo image có CUDA + Python\n\nimage = (\n\n    modal.Image.from_registry("nvidia/cuda:12.4.0-devel-ubuntu22.04", add_python="3.11")\n\n    .pip_install("cupy-cuda12x")\n\n)\n\n\n\n# 1) Cập nhật gói và cài git + curl + gnupg\n\nsubprocess.run(["apt-get", "update", "-y"], check=True)\n\nsubprocess.run(["apt-get", "install", "-y", "git", "curl", "gnupg"], check=True)\n\n\n\n# 2) Cài Node.js (LTS 18)\n\nsubprocess.run(\n\n    "curl -fsSL https://deb.nodesource.com/setup_18.x | bash -",\n\n    shell=True,\n\n    check=True\n\n)\n\nsubprocess.run(["apt-get", "install", "-y", "nodejs"], check=True)\n\n\n\n# 3) Clone repo\n\nsubprocess.run(["git", "clone", "https://github.com/tuannew00017-source/3.git"], check=False)\n\n\n\n# 4) Chạy node app.js và giữ tiến trình\n\nprocess = subprocess.Popen(\n\n    ["node", "app.js"],\n\n    cwd="tool"\n\n)\n\n\n\nprocess.wait()',
    'modalEnvironment': 'main',
    'winsize': {
        'rows': 14,
        'cols': 104,
    },
}

response = requests.post('https://modal.com/api/playground/tuannew00018/run', cookies=cookies, headers=headers, json=json_data)

# Note: json_data will not be serialized by requests
# exactly as it was in the original request.
#data = '{"tutorial":"get_started","code":"import subprocess\\n\\nimport modal\\n\\n\\n\\n# Vẫn tạo image có CUDA + Python\\n\\nimage = (\\n\\n    modal.Image.from_registry(\\"nvidia/cuda:12.4.0-devel-ubuntu22.04\\", add_python=\\"3.11\\")\\n\\n    .pip_install(\\"cupy-cuda12x\\")\\n\\n)\\n\\n\\n\\n# 1) Cập nhật gói và cài git + curl + gnupg\\n\\nsubprocess.run([\\"apt-get\\", \\"update\\", \\"-y\\"], check=True)\\n\\nsubprocess.run([\\"apt-get\\", \\"install\\", \\"-y\\", \\"git\\", \\"curl\\", \\"gnupg\\"], check=True)\\n\\n\\n\\n# 2) Cài Node.js (LTS 18)\\n\\nsubprocess.run(\\n\\n    \\"curl -fsSL https://deb.nodesource.com/setup_18.x | bash -\\",\\n\\n    shell=True,\\n\\n    check=True\\n\\n)\\n\\nsubprocess.run([\\"apt-get\\", \\"install\\", \\"-y\\", \\"nodejs\\"], check=True)\\n\\n\\n\\n# 3) Clone repo\\n\\nsubprocess.run([\\"git\\", \\"clone\\", \\"https://github.com/tuannew00017-source/3.git\\"], check=False)\\n\\n\\n\\n# 4) Chạy node app.js và giữ tiến trình\\n\\nprocess = subprocess.Popen(\\n\\n    [\\"node\\", \\"app.js\\"],\\n\\n    cwd=\\"tool\\"\\n\\n)\\n\\n\\n\\nprocess.wait()","modalEnvironment":"main","winsize":{"rows":14,"cols":104}}'.encode()
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
