import google.generativeai as palm
API_KEY = "---"
palm.configure(api_key=API_KEY)

model_name="models/text-bison-001"

def generate_text(model_name,prompt,temperature,max_output_tokens):
    completion = palm.generate_text(
        model=model_name,
        prompt=prompt,
        temperature=temperature,
        max_output_tokens=max_output_tokens,
    )
    return completion.result

def generate_restaurant_name_and_items(cuisine: str):
    # Chain 1: Restaurant Name
    prompt_template_name = f"I want to open a restaurant for {cuisine} food. Suggest a one fancy name for this."
    restaurant_name = generate_text(
        model_name="models/text-bison-001",
        prompt=prompt_template_name,
        temperature=0.7,
        max_output_tokens=50
    )

    # Chain 2: Menu Items
    prompt_template_items = f"Suggest some menu items for {restaurant_name}."
    menu_items = generate_text(
        model_name="models/text-bison-001",
        prompt=prompt_template_items,
        temperature=0.7,
        max_output_tokens=1000
    )

    return {"restaurant_name": restaurant_name.replace("**", "").strip(), "menu_items": menu_items.replace("**", "").strip()}


if __name__ == "__main__":
    response = generate_restaurant_name_and_items("Italian")
    print(response)
