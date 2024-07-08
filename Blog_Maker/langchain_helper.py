import google.generativeai as palm
API_KEY = "AIzaSyAiBOiKqa2ahKi1Zb7O0zkl3g-c8MZ-s1E"
palm.configure(api_key=API_KEY)


def generate_text(prompt,max_output_tokens):
    completion = palm.generate_text(
        model="models/text-bison-001",
        prompt=prompt,
        temperature=0.99,
        max_output_tokens=max_output_tokens,
    )
    return completion.result


if __name__ == "__main__":
    response = generate_text(f"Generating a 1000-word blog on 'Virat Kohli' gives Title for Blog. with keywords 'Cricket,Career,Records' and give detail about keywords regarding topic. it should completed if it takes some more number of words that's okay.",2500)
    print(response)
