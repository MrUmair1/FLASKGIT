
from flask import Flask

from flask_restful import Resource, Api, reqparse, abort, fields, marshal_with
from sqlalchemy import Table, Column, Integer, String, MetaData, ForeignKey

from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker

database_user = 'root'
database_pwd = 'admin123'
database = 'mydb'

####### DATABASE ENGINE ##########
engine = create_engine(f"mysql://{database_user}:{database_pwd}@localhost/{database}")
db = scoped_session(sessionmaker(bind=engine))

app = Flask(__name__)
api = Api(app)

######### DATABASE MODEL ############

metadata = MetaData()
mydb = Table('Videos', metadata,
             Column('v_id', Integer, primary_key=True, nullable=False),
             Column('v_name', String(100), nullable=False),
             Column('v_views', Integer, nullable=False),
             Column('likes', Integer, nullable=False),
             )
metadata.create_all(engine)


def __repr__(self):
    return f'Videos(name = {self.v_name}, views = {self.v_views}, likes ={self.likes})'


########### Argument PARSER ##############

Video_put_args = reqparse.RequestParser()
Video_put_args.add_argument("name", type=str, help="name of video required", required=True)
Video_put_args.add_argument("views", type=int, help="views of video required", required=True)
Video_put_args.add_argument("likes", type=int, help="likes of video required ", required=True)

########### Creating DB_FIELDS Into JSON FORMAT ############

resource_fields = {
    'v_id': fields.Integer,
    'v_name': fields.String,
    'v_views': fields.Integer,
    'likes': fields.Integer
}





#
#
# def If_exist(video_id):
#     abort(409, message = "Video already exist....")

######### MAIN CLASS FOR API RESOURCES ##############

class Video(Resource):
    @marshal_with(resource_fields)
    def get(self, video_id):




        # Not_exist(video_id)
        # result = Videos.query.get(v_id = video_id)
       try:
            result = db.execute(f"SELECT * FROM Videos where v_id = {video_id}").fetchall()
            if not result.v_id == video_id:
                print("not found")
            else:
                print("Found")

       except:
           print ("could not find")

    @marshal_with(resource_fields)
    def put(self, video_id):
        # If_exist(video_id)
        # if_exist(video_id)
        args = Video_put_args.parse_args()
        arg_name = args['name']
        arg_view = args['views']
        arg_likes = args['likes']

        ######### Querying For Inserting into DB ##################

        with engine.connect() as con:
            v = """INSERT INTO Videos(v_id, v_name, v_views, likes) VALUES( %s, %s, %s, %s)"""
            con.execute(v, (video_id, arg_name, arg_view, arg_likes))

    ############# DELETE ############
    @marshal_with(resource_fields)
    def delete(self, video_id):
        chk = db.execute(f"SELECT * FROM Videos where v_id = {video_id}").fetchone()
        if not chk :print("could not find......")

        with engine.connect() as con:
            result = con.execute(f"DELETE FROM Videos where v_id = {video_id}")

            print(result)

        # not_exist(video_id)
        # del Videos[video_id]
        # return '', 204
    ############# UPDATE ############
    @marshal_with(resource_fields)
    def patch(self,video_id):
        with engine.connect() as con:
            UPD = con.execute(f"update Videos set v_views = 200000 where v_id = {video_id}")
            print(UPD)


api.add_resource(Video, "/video/<int:video_id>")

if __name__ == "__main__":
    app.run(host='127.0.0.2', port=3308, debug=True)
