
from flask import Flask, render_template, \
 url_for, redirect, request, flash, session

import os



app = Flask(__name__)

@app.route('/', methods= ['GET', 'POST'])
def home():

	if request.method == 'POST':
		code = request.form['code']
		language = request.form['language']
		print(code)
		print(language)

		f = open("haha."+language, "w")
		f.write(code)
		f.close()
		# print(language)
		ampersand = "&"
		cmd  = "./compile haha."+ language + " > output.txt 2>&1"
		os.system(cmd)

		f = open("output.txt", "r")
		output = f.read()

		return render_template("webpage.html", output=output, code=code)

	return render_template("webpage.html")



if __name__ == '__main__':
	app.run(debug=True)
