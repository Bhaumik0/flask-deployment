from website import blog

if __name__=="__main__":
    application=blog()
    application.run(debug=False,host='0.0.0.0')