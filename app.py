from flask import Flask, request, render_template
from stories import Story

app = Flask(__name__)

story = Story(
    ["place", "noun", "verb", "adjective", "plural_noun"],
    """
    Once upon a time in 18th century {place}, there lived a {adjective} {noun}. 
    It loved to {verb} with {plural_noun}. The people of {place} did not like this.
    You won't believe what happened next.
    """
)

@app.route('/')
def show_root():
    """Landing page for users"""
    return render_template(
        'home.html',
        prompts=story.prompts
    )

@app.route('/story')
def show_story():
    """Show madlib story given user inputs"""
    user_story = story.generate(dict(request.args))
    return f"""
    <h1>Your story</h1>
    <p>{user_story}</p>
    """
