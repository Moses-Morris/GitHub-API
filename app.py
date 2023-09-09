from flask import Flask, request, jsonify
import datetime
import pytz

app = Flask(__name__)

@app.route('/api', methods=['GET'])
def get_info():
    # Get query parameters
    slack_name = request.args.get('slack_name')
    track = request.args.get('track')

    # Validate parameters
    if not slack_name or not track:
        return jsonify({"error": "slack_name and track are required parameters"}), 400

    # Get the current day of the week
    current_day = datetime.datetime.now(pytz.utc).strftime('%A')

    # Get the current UTC time with a +/-2 minute window
    utc_time = datetime.datetime.now(pytz.utc)
    utc_time = utc_time.replace(second=0, microsecond=0)
    utc_time_str = utc_time.strftime('%Y-%m-%dT%H:%M:%SZ')

    # Construct GitHub URLs
    github_file_url = "https://github.com/username/repo/blob/main/file_name.ext"
    github_repo_url = "https://github.com/username/repo"

    # Create the JSON response
    response_data = {
        "slack_name": slack_name,
        "current_day": current_day,
        "utc_time": utc_time_str,
        "track": track,
        "github_file_url": github_file_url,
        "github_repo_url": github_repo_url,
        "status_code": 200
    }

    return jsonify(response_data)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
