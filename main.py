from flask import Flask
from flask_restful import Api, Resource, reqparse, abort

app = Flask(__name__)
api = Api(app)

#Controlul corespunderii requestului POST cu regulile de aditie
book_post_args = reqparse.RequestParser()
book_post_args.add_argument("name", type=str, help="Name of the book", required=True)
book_post_args.add_argument("author", type=str, help="Author of the book", required=True)
book_post_args.add_argument("year", type=int, help="Year of publication of the book", required=True)
##Procesul de update a listei de carti
book_update_args = reqparse.RequestParser()
book_update_args.add_argument("name", type=str)
book_update_args.add_argument("author", type=str)
book_update_args.add_argument("year", type=int)

books = {}
## Definim erorile care pot aparea
def abort_if_book_id_doesnt_exist(book_id):
	if book_id not in books:
		abort(404, message="Could not find the book")

def abort_if_book_exists(book_id):
	if book_id in books:
		abort(409, message="Book with this id already exists")

class Book(Resource):
    ##GET Request
    def get(self, book_id):
        abort_if_book_id_doesnt_exist(book_id)
        return books[book_id]
    ##POST Request
    def post(self, book_id):
        args = book_post_args.parse_args()
        if book_id in books:
            abort(409, message="Book id already taken")
        books[book_id] = {"name": args["name"], "author": args["author"], "year": args["year"]}
        return books[book_id]
    ##PUT Request
    def put(self, book_id):
        abort_if_book_exists(book_id)
        args = book_update_args.parse_args()
        if args['name']:
            books[book_id]['name'] = args['name']
        if args['author']:
            books[book_id]['author'] = args['author']
        if args['year']:
            books[book_id]['year'] = args['year']
        return books[book_id], 201 #A fost creat
    ##DELETE Request
    def delete(self, book_id):
        abort_if_book_id_doesnt_exist(book_id)
        del books[book_id]
        return books, 204 #A fost sters

#Registrat ca resursa
api.add_resource(Book, "/book/<int:book_id>")

if __name__ == "__main__":
    app.run('localhost', 5000)