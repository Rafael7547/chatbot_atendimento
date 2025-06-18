import re

def responder(mensagem):
    mensagem = mensagem.lower()

    respostas = {
        r"(oi|ol[áa]|bom dia|boa tarde|boa noite)": "Olá! Em que posso ajudar?",
        r"(hor[áa]rio|funcionamento)": "Funcionamos de segunda a sábado, das 8h às 18h.",
        r"(preço|valor).*lavagem": "A lavagem simples custa R$ 30 e a completa R$ 60.",
        r"(formas de pagamento|pagamento)": "Aceitamos dinheiro, pix e cartão.",
        r"(endere[çc]o|localiza[çc][aã]o)": "Estamos localizados na Rua Exemplo, nº 123 - Centro.",
        r"(agendar|marcar|horário)": "Claro! Para agendar, por favor envie seu nome e o horário desejado.",
        r"(obrigado|valeu)": "De nada! 😊",
        r"(tchau|sair|encerrar)": "Até logo! Se precisar, estamos à disposição."
    }

    for padrao, resposta in respostas.items():
        if re.search(padrao, mensagem):
            return resposta

    return "Desculpe, não entendi. Pode reformular sua pergunta?"

def iniciar_chat():
    print("🤖 Chatbot de Atendimento")
    print("Digite 'sair' para encerrar.\n")

    while True:
        user_input = input("Você: ")
        if user_input.lower() in ["sair", "tchau", "encerrar"]:
            print("Bot: Até logo! Se precisar, estamos à disposição.")
            break

        resposta = responder(user_input)
        print("Bot:", resposta)

# Inicia o chatbot
if __name__ == "__main__":
    iniciar_chat()
