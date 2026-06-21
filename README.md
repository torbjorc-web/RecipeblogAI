OpenAI Python API Recipe Blog
This project uses the OpenAI Python API to generate a recipe blog post in HTML format based on a user's dietary restrictions, cuisine preferences, and available ingredients.
Project Goal
Build a prompt-driven recipe generator that creates a single, publish-ready HTML blog post.
What It Does
Imports the OpenAI class from the openai module.
Creates an OpenAI client.
Stores a simple user profile with:
dietary restrictions
cuisine preferences
ingredients available
Builds a system prompt and user prompt.
Sends both prompts to the Chat Completions API.
Prints the generated HTML recipe blog post.
Requirements
Python 3.8 or newer
openai Python package
A valid OpenAI API key
Installation
Install the OpenAI package:
pip install openai
Setup
Option 1: Set an environment variable
export OPENAI_API_KEY="your-api-key-here"
Then create the client like this:
client = OpenAI()
Option 2: Pass the API key directly
client = OpenAI(api_key="your-api-key-here")
How to Run
Save your Python script as recipe_blog.py.
Add your OpenAI API key.
Run the script:
python recipe_blog.py
Expected Output
The script prints HTML code for a recipe blog post that:
follows the user's dietary restrictions,
respects the user's cuisine preferences,
uses only the listed ingredients,
contains a title, description, ingredients, and instructions,
limits instructions to six steps or fewer.
Files
recipe_blog.py - Main Python script for generating the recipe blog HTML.
Notes
The generated HTML is meant to be reviewed before publishing.
You can customize the user profile values to generate different recipe styles.
License
This project is intended for learning and portfolio use.# RecipeblogAI