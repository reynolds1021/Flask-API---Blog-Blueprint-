from app import db
from app.blueprints.blog import bp as blog
from flask import jsonify, request, url_for

from app.models import Blog


@blog.route('/', methods=['GET']) #Get all blogs
def index():
    """
    [GET] /blogs/

    """
    data = {
        'blogs': [blog.to_dict() for blog in Blog.query.all()]
    }
    return jsonify(data)

@blog.route('/<id>', methods=['GET']) #Fetch a single blog by searching user_id
def get_blog(id):
    """
   [GET] /blogs/<email>

    """
    blog = Blog.query.filter_by(id=id).first()
    data = {
        'blogs': blog.to_dict() if blog else []
    }
    return jsonify(data), 200

@blog.route('/', methods=['POST']) #Route to create a new blog
def create_blog():
    """
    [POST] /createblog/

    """
    data = request.get_json()
    title = data.get('title')
    content = data.get('content')
    id = data.get('id')
    user_id = data.get('user_id')
    #if not title or user_id:
     #   return jsonify({"detail": "The credentials you entered are invalid"}), 400  #Add status code
    blog = Blog(title, content, user_id)
    db.session.add(blog)
    db.session.commit()
    response = jsonify(blog.to_dict())
    response.status_code = 291 #Add status code
    response.headers['Location'] =url_for('blog.get_blog', title=blog.title)
    return response

@blog.route('/<int:id>', methods=['DELETE']) #Route to delete a blog(s)
def delete_blog(id):
    """
    [DELETE] /blogs/<id>

    """

    blog = Blog.query.get(id)
    if not blog:
        return jsonify({"detail": f"Blog with id:{id} does not exist"}), 400 #Add error handling
    db.session.delete(blog)
    db.session.commit()
    return jsonify({"detail": f"Post:{blog.title} has been deleted"}), 201  #Return 204 status

@blog.route('/<int:id>', methods=['PUT'])
def update_blog(id):
    """
    [PUT] /blogs/<id>

    """
    blog = Blog.query.get(id)
    data = request.get_json()
    blog.from_dict(data)
    db.session.commit()
    return jsonify({'users': blog.to_dict()}), 200


