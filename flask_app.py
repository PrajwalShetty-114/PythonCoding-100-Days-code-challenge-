from flask import Flask,request,render_template
# import file_system
import random
port=3000
app=Flask(__name__)
all_books=[]
length=len(all_books)
print(__name__)


def bold(function):
    def wrap():
        return f"<b>{function()}</b>"
    return wrap

def underline(function):
    def wrap():
        return f"<u>{function()}</u>"
    return wrap

def italic(function):
    def wrap():
        return f"<em>{function()}</em>"
    return wrap

@app.route('/')
def say_hi():
    return render_template('index.html',size=length)

@app.route('/add', methods=['GET','POST'])
def add_book():
    if request.method=='GET':
        return render_template('add.html',)
    else:
        book_name=request.form.get('book')
        author=request.form.get('author')
        rating=request.form.get('rating')
        dictionary={
            "title":f"{book_name}",
            "author":f"{author}",
            "rating":rating
        }

        all_books.append(dictionary)
        length_library=len(all_books)
        print(length_library)
        return render_template('index.html',books=all_books,size=length_library)


@app.route('/hello')
@bold
@italic
@underline
def say_hello():
    return "hello"


guessed_number=random.randint(0,9)
@app.route('/Guess/<int:number>')
def guess_number(number):
    if number<guessed_number:
        return "<h1 style='color:red;'>Too Low,Try Again</h1>/" \
        "<img src='https://media2.giphy.com/media/v1.Y2lkPTc5MGI3NjExanpjaHBjNWQ0N2Rjd2xhcjZoMWhhdTMxaGd2bWRnd3Y1enlzaDV2aCZlcD12MV9naWZzX3NlYXJjaCZjdD1n/4V3RuU0zSq1SC8Hh4x/200w.webp'>"
    elif number==guessed_number:
        return "<h1 style='color:green'>You found the number</h1>/" \
        "<img src='https://media0.giphy.com/media/v1.Y2lkPTc5MGI3NjExOW90bGpjMGp0MWk4bW5rNzU1aWN1aXQwNTQ1aWwwZzlpZGFzdzF6YSZlcD12MV9naWZzX3NlYXJjaCZjdD1n/3o7aCWJavAgtBzLWrS/200.webp'>"
    else :
        return "<h1 style='color:blue'>Too High</h1>/" \
        "<img src='https://media3.giphy.com/media/v1.Y2lkPTc5MGI3NjExNXZkY2puZDgwYXRiZzVyZjl5dDhrczU2MzRodXVqaG5uY3B3N3J6bSZlcD12MV9naWZzX3NlYXJjaCZjdD1n/YpfevjbcK4HWjjIQGL/200.webp'>"

    

@app.route("/form", methods=["GET","POST"])
def template():
    if request.method=="GET":
        return render_template('form.html')
    else:
        name=request.form.get('name')
        password=request.form.get('password')
        
        print(request.form)
        return f"<h1>Successfully sent the message</h1>"
        # print(name)


if __name__=="__main__":
    app.run(debug=True)
