from flask import Flask, render_template
import pandas as pd

app = Flask(__name__)

# Load data from Excel
def load_blog_data():
    df = pd.read_excel('data.xlsx')
    return df.to_dict(orient='records')

@app.route('/')
def home():
    blog_posts = load_blog_data()
    return render_template('index.html', posts=blog_posts)

if __name__ == '__main__':
    # Generate static index.html file
    with app.app_context():
        blog_posts = load_blog_data()
        static_html = render_template('index.html', posts=blog_posts)
        with open('index.html', 'w', encoding='utf-8') as f:
            f.write(static_html)
    print("Static index.html generated successfully.")
