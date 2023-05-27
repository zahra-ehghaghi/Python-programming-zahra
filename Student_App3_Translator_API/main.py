from flask import Flask, render_template
import pandas as pd
app = Flask("Translator")
@app.route("/")
def home():
    return render_template("home.html")

@app.route("/api/v1/<word>")
def translate(word):
    df = pd.read_csv("dictionary.csv")
    definition = df.loc[df['word'] == word]['definition'].squeeze()
    print(definition)
    return {
         "Word": word,
         "Definition": definition}
if __name__== "__main__":
    app.run(debug=True,port=5001)