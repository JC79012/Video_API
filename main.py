import required as required
from flask import Flask
from flask_restful import Api, Resource, reqparse, abort, fields, marshal_with
from flask_sqlalchemy import SQLAlchemy

# to create a new flask app
app = Flask(__name__)
# wrap the app in an api
api = Api(app)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
db = SQLAlchemy(app)

class VideoModel(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	name = db.Column(db.String(100), nullable=False)
	views = db.Column(db.Integer, nullable=False)
	likes = db.Column(db.Integer, nullable=False)

    # def __repr__(self):
    #     pass
        # return "name and stuff"
        # return f"Video(name ={name}, views={views}, likes ={likes}"
   
video_put_args = reqparse.RequestParser()
video_put_args.add_argument("name", type=str, help="Name of the video is required", required=True)
video_put_args.add_argument("views", type=int, help="Views of the video", required=True)
video_put_args.add_argument("likes", type=int, help="Likes on the video", required=True)

video_update_args = reqparse.RequestParser()
video_update_args.add_argument("name", type=str, help="Name of the video is required")
video_update_args.add_argument("views", type=int, help="Views of the video")
video_update_args.add_argument("likes", type=int, help="Likes on the video")


class Video(Resource):
    #when we return the ans is returns as a dictionary/json format
    @marshal_with(resource_fields)
    def get(self, video_id):
        result = VideoModel.query.get(id= video_id)
        return result
        
    @marshal_with(resource_fields)
    def put(self, video_id):
        args = video_put_args.parse_args()
	    result = VideoModel.query.filter_by(id= video_id).first()
	    if result:
		    abort(409, message="Video id taken...")
    
    def delete(self, video_id):
        abort_if_video_id_doesnt_exist(video_id)
        del videos[video_id]
        return '', 204


api.add_resource(Video, "/video/<int:video_id>")
if __name__ == '__main__':
    # starts the server
    # in debug mode and logging information
    # only done when testing
    app.run(debug=True)
