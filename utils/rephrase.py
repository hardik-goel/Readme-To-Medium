import google.generativeai as genai


def initialise_model(API_KEY, MODEL_NAME):
    genai.configure(api_key=API_KEY)
    model = genai.GenerativeModel(MODEL_NAME)
    return model

def write_to_file(rephrased_text):
    with open('resources/file.txt', 'w') as file:
        file.write(f"{rephrased_text}")
        return file

def rephrase_text(CONTENT, MODEL):
    print (f"CONTENT:: {CONTENT}")
    text_prompt = str(CONTENT) + "\n Rephrase this text."
    responses = MODEL.generate_content(text_prompt)
    # for response in responses:
    #     rephrased_text = response.text
    #     print(rephrased_text, end="")
    # file = write_to_file(rephrased_text)
    # return file
    if responses:
        rephrased_text = responses[0].text  # Take the first response
        print(rephrased_text, end="")
        file = write_to_file(rephrased_text)
        return file
    else:
        print("No responses generated.")
        return None
