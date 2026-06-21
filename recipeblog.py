from openai import OpenAI

client = OpenAI(api_key="YOUR_OPENAI_API_KEY_HERE")  # Replace with your actual API key

user_profile = {}

user_profile["dietary_restrictions"] = "vegetarian, gluten-free"
user_profile["cuisine_preferences"] = "Italian, Mediterranean, Mexican"
user_profile["ingredients_available"] = "chickpeas, tomatoes, olive oil, garlic, onion, bell peppers, spinach, lemons"

system_prompt = {
    "role": "system",
    "content": "You are an AI assistant that generates HTML code for a recipe blog. The blog must take into account specific dietary restrictions, chosen cuisine type, and a provided list of ingredients. Create beautiful, well-formatted HTML that's ready to publish on a website."
}

user_content1 = "I want to create a recipe blog post for my culinary hub. Here is my user profile data:\n"
user_content1 += f"Dietary Restrictions: {user_profile['dietary_restrictions']}\n"
user_content1 += f"Cuisine Preferences: {user_profile['cuisine_preferences']}\n"
user_content1 += f"Available Ingredients: {user_profile['ingredients_available']}\n"

user_content2 = "Please create a blog post with the following structure:\n"
user_content2 += "- A catchy title for the recipe\n"
user_content2 += "- A descriptive paragraph about the recipe\n"
user_content2 += "- A clearly formatted ingredients list\n"
user_content2 += "- Step-by-step cooking instructions\n"
user_content2 += "Example format for ingredients: • Ingredient name (quantity)\n"
user_content2 += "Example format for instructions: Step 1: [instruction text]\n"

user_content3 = "Important constraints for this recipe:\n"
user_content3 += "- The recipe must be made using ONLY the ingredients listed in my user profile above\n"
user_content3 += "- Your output should be limited to a single blog post only\n"
user_content3 += "- The recipe instructions should not exceed six steps\n"

user_prompt = {
    "role": "user",
    "content": user_content1 + "\n" + user_content2 + "\n" + user_content3
}

response = client.chat.completions.create(
    model="gpt-3.5-turbo",
    messages=[system_prompt, user_prompt]
)

html_content = response.choices[0].message.content
print(html_content)

print("\n" + "=" * 50)
print("HTML code generated successfully! Ready for website publication.")
print("=" * 50)
