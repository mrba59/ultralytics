from flask import Flask, send_from_directory, abort, jsonify, send_file
import os
import base64
import mimetypes

app = Flask(__name__)

@app.route('/')
def serve_app_enty():
    try:
        return send_from_directory("public", "index.html")
    except FileNotFoundError:
        abort(404)

@app.route('/<path:filename>')
def serve_front_app(filename):
    try:
        return send_from_directory("public", filename)
    except FileNotFoundError:
        abort(404)


@app.route('/video/<path:filepath>')
def serve_video_asset(filepath):
    decoded_file_path =  base64.b64decode(filepath).decode("utf-8")
    print(decoded_file_path)

    if not os.path.isfile(decoded_file_path):
        print("file not found")
        return abort(404, description="File not found")
    

    with open(decoded_file_path, "r") as file:
        print(file)

    # Guess the MIME type
    mime_type, _ = mimetypes.guess_type(decoded_file_path)
    mime_type = mime_type or 'application/octet-stream'

    return send_file(decoded_file_path, mimetype=mime_type)

@app.route('/api/get-project/<name>')
def get_project_as_json(name):
    path = "../results/" + name
    video_metadata_path = path + "/track.yaml"
    labels_dir_path = path + "/labels"

    res = {
        "videoData": {},
        "frames": []
    }

    #share video Data
    with open(video_metadata_path, "r") as file:
        key_pairs =  file.read().split('\n')

        for key_pair in key_pairs:
            key, value = (key_pair.split(':') + [''])[:2]

            if key != '' and value != '':
                res["videoData"][key] = value

    #add labels to frames    
    labels = os.listdir(labels_dir_path)
    labels.sort()
    labels.sort(key=len)
    
    c = 1
    for file_path in labels:
        one_frame = {
            "frame": c,
            "elements": []
        }

        with open(labels_dir_path + "/" + file_path, "r") as file:
            one_frame_details = file.read().split("\n")
            for one_id_frame_detail in one_frame_details:
                if one_id_frame_detail != '':
                    typeId, x,y,w,h,score,elementId = one_id_frame_detail.split(" ")
                    one_frame["elements"].append({
                        "typeId": int(typeId),
                        "x": float(x),
                        "y": float(y),
                        "w": float(w),
                        "h": float(h),
                        "score": float(score),
                        "elementId": int(elementId)
                    })

        res["frames"].append(one_frame)
        c = c+1

    return jsonify(res)


if __name__ == '__main__':
    app.run(debug=True)