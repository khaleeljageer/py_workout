import requests

base_url = "https://www.youtube.com/watch?v="


def main():
    api_key = "API_KEY"
    page_token = 'CNgEEAA'

    while True:
        video_ids, page_token = get_tamil_videos_with_license(api_key, page_token)
        for video_id in video_ids:
            save_url(video_id)
        print('Next Page Token: ', page_token)
        if not page_token:
            break


def get_tamil_videos_with_license(api_key, page_token):
    api_url = "https://www.googleapis.com/youtube/v3/search"
    params = {
        "key": api_key,
        "part": "id",
        "q": "tamil",
        "type": "video",
        "videoLicense": "creativeCommon",
        "relevanceLanguage": "ta",
        "maxResults": 50,
        "pageToken": page_token
    }

    response = requests.get(api_url, params=params)
    print('Status Code: ', response.status_code)
    if response.status_code == 200:
        data = response.json()

        next_page_token = data.get('nextPageToken')
        video_ids = []

        for item in data.get('items', []):
            video_ids.append(item['id']['videoId'])

        return video_ids, next_page_token
    else:
        return [], None


def save_url(video_id):
    print("Video ID: ", video_id)
    with open('urls1.txt', 'a') as file:
        file.write(f'{base_url + video_id}\n')
        file.close()


if __name__ == '__main__':
    main()
