

import codificador as cod

print(f'\n\n\n\n\n\n\n\n\n\n\n\n\n---')

#msg_entrada = str(input('Mensagem: '))
msg_entrada = "Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry's standard dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled it to make a type specimen book. It has survived not only five centuries, but also the leap into electronic typesetting, remaining essentially unchanged. It was popularised in the 1960s with the release of Letraset sheets containing Lorem Ipsum passages, and more recently with desktop publishing software like Aldus PageMaker including versions of Lorem Ipsum."
#msg_entrada = "Lorem Ipsum is simply dummy text of the printing and typesetting."
#msg_entrada = "Teste"
#msg_entrada = ""
#msg_entrada = "Vitor Vicente é, um progrador.!"

x = cod.Codificar()
x.criptografar(msg_entrada)
print(x)

y = x.codificado
print(f'>>> y [{y}] - len: {len(y)}')
decode_y = x.decriptografar(y)
print(f'>>>> {decode_y}')