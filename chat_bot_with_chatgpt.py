import google.generativeai as genai


api_key="AIzaSyCdXVmEbitazkQSkp5Amcylv92tzhrZVas"

genai.configure(api_key=api_key)


while(True):

    model = genai.GenerativeModel('gemini-pro')
    user_input=input("USER: ")
    user_input=user_input.lower()
    if(user_input=="exit"):
        break
    response = model.generate_content(user_input)
    print("\n")

    print("AnmolAI: ",response.text)
    print("\n")
    
    
