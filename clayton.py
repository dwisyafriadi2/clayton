import requests

def read_init_data(file_path):
    """Reads the init-data from the specified file."""
    with open(file_path, 'r') as file:
        return file.read().strip()

def authenticate(init_data):
    """Sends a POST request to authenticate using the given init-data."""
    url = "https://tonclayton.fun/api/user/auth"
    headers = {
        "accept": "application/json, text/plain, */*",
        "accept-encoding": "gzip, deflate, br, zstd",
        "accept-language": "en-US,en;q=0.9",
        "content-length": "0",
        "init-data": init_data,
        "origin": "https://tonclayton.fun",
        "priority": "u=1, i",
        "referer": "https://tonclayton.fun/?tgWebAppStartParam=1580490871",
        "sec-ch-ua": '"Microsoft Edge";v="129", "Not=A?Brand";v="8", "Chromium";v="129", "Microsoft Edge WebView2";v="129"',
        "sec-ch-ua-mobile": "?0",
        "sec-ch-ua-platform": '"Windows"',
        "sec-fetch-dest": "empty",
        "sec-fetch-mode": "cors",
        "sec-fetch-site": "same-origin",
        "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/129.0.0.0 Safari/537.36 Edg/129.0.0.0"
    }

    response = requests.post(url, headers=headers)
    
    if response.status_code == 200:
        print("Authentication successful!")
        return response.json()
    else:
        print(f"Failed to authenticate. Status code: {response.status_code}")
        return None
    

def fetch_task(init_data, urls):
    """Fetches the tasks from the given URLs using the provided init-data."""
    headers = {
        "accept": "application/json, text/plain, */*",
        "accept-encoding": "gzip, deflate, br, zstd",
        "accept-language": "en-US,en;q=0.9",
        "content-length": "0",
        "init-data": init_data,
        "origin": "https://tonclayton.fun",
        "priority": "u=1, i",
        "referer": "https://tonclayton.fun/earn",
        "sec-ch-ua": '"Microsoft Edge";v="129", "Not=A?Brand";v="8", "Chromium";v="129", "Microsoft Edge WebView2";v="129"',
        "sec-ch-ua-mobile": "?0",
        "sec-ch-ua-platform": '"Windows"',
        "sec-fetch-dest": "empty",
        "sec-fetch-mode": "cors",
        "sec-fetch-site": "same-origin",
        "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/129.0.0.0 Safari/537.36 Edg/129.0.0.0"
    }

    all_tasks = []
    
    for url in urls:
        response = requests.get(url, headers=headers)
        
        if response.status_code == 200:
            print(f"Fetch Task successful from {url}!")
            tasks = response.json()
            all_tasks.extend(tasks)  # Combine tasks from each URL
        else:
            print(f"Failed to fetch tasks from {url}. Status code: {response.status_code}")
    
    return all_tasks
    
def complete_task(task_id, init_data):
    """Marks the given task as complete."""
    url = "https://tonclayton.fun/api/tasks/complete"
    payload = {
        "task_id": task_id
    }
    headers = {
        "accept": "application/json, text/plain, */*",
        "accept-encoding": "gzip, deflate, br, zstd",
        "accept-language": "en-US,en;q=0.9",
        "content-length": "13",  # Updated content length for the payload
        "content-type": "application/json",
        "init-data": init_data,
        "origin": "https://tonclayton.fun",
        "priority": "u=1, i",
        "referer": "https://tonclayton.fun/earn",
        "sec-ch-ua": '"Microsoft Edge";v="129", "Not=A?Brand";v="8", "Chromium";v="129", "Microsoft Edge WebView2";v="129"',
        "sec-ch-ua-mobile": "?0",
        "sec-ch-ua-platform": '"Windows"',
        "sec-fetch-dest": "empty",
        "sec-fetch-mode": "cors",
        "sec-fetch-site": "same-origin",
        "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/129.0.0.0 Safari/537.36 Edg/129.0.0.0"
    }

    response = requests.post(url, headers=headers, json=payload)  # Using json=payload to send the data as JSON
    
    if response.status_code == 200:
        print("Task completed successfully!")
        return response.json()
    else:
        print(f"Failed to complete the task. Please do the task manually. Status code: {response.status_code}")
        return None
    
def claim_task(task_id, init_data):
    """Marks the given task as complete."""
    url = "https://tonclayton.fun/api/tasks/claim"
    payload = {
        "task_id": task_id
    }
    headers = {
        "accept": "application/json, text/plain, */*",
        "accept-encoding": "gzip, deflate, br, zstd",
        "accept-language": "en-US,en;q=0.9",
        "content-length": "13",  # Updated content length for the payload
        "content-type": "application/json",
        "init-data": init_data,
        "origin": "https://tonclayton.fun",
        "priority": "u=1, i",
        "referer": "https://tonclayton.fun/earn",
        "sec-ch-ua": '"Microsoft Edge";v="129", "Not=A?Brand";v="8", "Chromium";v="129", "Microsoft Edge WebView2";v="129"',
        "sec-ch-ua-mobile": "?0",
        "sec-ch-ua-platform": '"Windows"',
        "sec-fetch-dest": "empty",
        "sec-fetch-mode": "cors",
        "sec-fetch-site": "same-origin",
        "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/129.0.0.0 Safari/537.36 Edg/129.0.0.0"
    }

    response = requests.post(url, headers=headers, json=payload)  # Using json=payload to send the data as JSON
    
    if response.status_code == 200:
        print("Task claim successfully!")
        return response.json()
    else:
        print(f"Failed to claim the task. Please claim do the task manually. Status code: {response.status_code}")
        return None

if __name__ == "__main__":
    # Read init_data from query.txt
    init_data = read_init_data("query.txt")
    print("Join Telegram @dasarpemulung or https://t.me/dasarpemulung")
    urls = [
        "https://tonclayton.fun/api/tasks/daily-tasks",
        "https://tonclayton.fun/api/tasks/default-tasks",
        "https://tonclayton.fun/api/tasks/partner-tasks"
    ]
    
    # Fetch tasks
    tasks = fetch_task(init_data,urls)
    
    if tasks:
        print("Task List:", tasks)
        for task_item in tasks:
            task = task_item.get('task', {})
            task_id = task_item.get('task_id', None)
            title = task.get('title', 'No Title')
            if task_id:
                print(f"Completing Task: {title} (ID: {task_id})")
                complete_task(task_id, init_data)
                claim_task(task_id, init_data)
                print("Join Telegram @dasarpemulung or https://t.me/dasarpemulung")
    
    # if fetch_task_response:
    #     print("Task List:", fetch_task_response)
    #     for task_item in fetch_task_response:
    #         task = task_item.get('task', {})
    #         title = task.get('title', 'No Title')
    #         description = task.get('description', 'No Description')
    #         reward_tokens = task.get('reward_tokens', 0)
    #         print(f"Task: {title}")
    #         print(f"Description: {description}")
    #         print(f"Reward: {reward_tokens} tokens")

    # Perform authentication
    auth_response = authenticate(init_data)
    # Process the response
    if auth_response:
        print("Auth Response:", auth_response)
        user_info = auth_response.get('user', {})
        daily_reward = auth_response.get('dailyReward', {})
        
        print(f"User ID: {user_info.get('id_telegram')}")
        print(f"Username: {user_info.get('username')}")
        print(f"Tokens: {user_info.get('tokens')}")
        
        if daily_reward.get('can_claim_today', False):
            print(f"Today's reward: {daily_reward['reward']['tokens']} tokens, {daily_reward['reward']['game_tries']} game tries.")
        else:
            print("No daily reward available for today.")