from flask import Flask, request, Response, jsonify
from requests import get

key = 'YOUR_API_KEY'
url = 'https://www.googleapis.com/youtube/v3/videos'

app = Flask(__name__)

@app.route("/video")
def vid():
    query = request.headers.get('q')
    if query == None:

        message = { "message" : "query not provided" }    

        return Response(
            status = 400,
            response = jsonify(message)
        )
    else:
        base_url = 'https://www.googleapis.com/youtube/v3/search'
    
        params = {
            'part': 'snippet',
            'q': query,
            'type': 'video',
            'maxResults': '5',
            'key': key
        }
        vid_info = []
        items = get(base_url, params=params).json()["items"]
        
        for item in items:
            vid_info.append({
                'id' : item['id']['videoId'],
                'thumbnailUrl' : item['snippet']['thumbnails']['default']['url'],
                'title' : item['snippet']['title']
            })
        return vid_info

app.run(port=81, host='0.0.0.0')
