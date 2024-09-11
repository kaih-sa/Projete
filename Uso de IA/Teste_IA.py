'''
TESTANDO SE A IA FUNCIONA AQUI NO CODIGO
'''
def Gemini(quest):
    #Import the Python SDK
    import google.generativeai as genai
    # Used to securely store your API key

    GOOGLE_API_KEY = 'AIzaSyC5ubXAp6pbZkOfeSwT2Qx7N4lSyi_Dw6Y'

    genai.configure(api_key=GOOGLE_API_KEY)

    model = genai.GenerativeModel('gemini-pro')

    # tentar usar verdadeiro ou falso

    response = model.generate_content(quest)
    return response.text
escolha = "Gepmetria analitica"
r = Gemini("Me de uma questão de verdadeiro ou falso sobre "+escolha+" e me de a reposta em baixo")
resposta = r[-10:]  # últimos 6 caracteres
print(r)
print(resposta)
