from deep_translator  import GoogleTranslator
import os

def pausar():
    pausar = input('Clique ENTER para continuar...')
def limpar():
    os.system('cls')

lingua = 'en'
while True:
    print("""
########################      
#                      #
#       TRADUTOR       #
#                      #
######################## 
    
A - Alterar Lingua
T - Traduzir
F - Fechar Programa
    """)
    escolha = input('Escolha a opção que deseja: ')
    limpar()

    if escolha == 'A' or escolha == 'a':
        lingua_traducao = input('''
############################      
#                          #
#     Escolha a Lingua     #
#                          #
############################ 
                    
Para que lingua deseja traduzir: ''')
        
        tradutor = GoogleTranslator(source='pt',target='en')
        traducao = tradutor.translate(lingua_traducao)
        lingua = traducao.lower()
        limpar()

    elif escolha == 'T' or escolha == 't':
        texto = input('''
############################      
#                          #
#         Tradução         #
#                          #
############################
O que deseja traduzir? ''')
        try:
            tradutor = GoogleTranslator(source='pt',target=f'{lingua}')
            traducao = tradutor.translate(texto)
            print(traducao)
            pausar()
            limpar()
        except:
            print('Lingua Invalida')
        
    elif escolha == 'F' or escolha == 'f':
        break
    
    else:
        erro = input('Opção Errada, tente novamente(ENTER)...')
        limpar()