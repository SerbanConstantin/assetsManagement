from app import createApp

if __name__ in '__main__':

    createApp()


""""
@app.route("/")
def helloWorld():
    return "Hello, world, my friends!!!"

@app.route("/greet")
def greet():
    return "Yoooo"

@app.route("/greet/<name>")
def greetName(name):
    return "Yoooo, " + name

@app.route("/bye", methods = ['POST'] )
def bye():
    print(request.form)
    return "Draga " + request.form["for"] + " iti urez " + request.form["wish"]


@app.route("/login")
def logIN():
    return "Log In"

@app.route("/register")
def register():
    return "Register"

"""