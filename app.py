from website import app

if __name__=="__main__":
    app=app()
    app.run(debug=True,port=5050)