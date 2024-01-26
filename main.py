import json

from flask import Flask, jsonify, request

from model.post import Post

posts = []

app = Flask(__name__)


class CustomJSONEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, Post):
            return {'body': obj.body, 'author': obj.author, 'comment': obj.comment}
        else:
            return super().default(obj)


@app.route('/post', methods=['GET'])
def read_posts():
    return jsonify({'posts': posts})


@app.route('/post', methods=['POST'])
def create_post():
    post_json = request.get_json()
    post = Post(post_json['body'], post_json['author'])

    posts.append(json.loads(json.dumps(post, cls=CustomJSONEncoder)))
    return jsonify({'status': 'success'})


if __name__ == '__main__':
    app.run(debug=True)
