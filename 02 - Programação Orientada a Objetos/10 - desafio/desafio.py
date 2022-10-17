from pydoc import doc
# #Alfabeto
# abc = []

# # list de a-n
# for i in range(ord('A'), ord('Z')+1):
#   abc.append(chr(i))
# ind_letra = abc.index('A')+1

# print(ind_letra)


# pernas = ['esquerda','direita','nenhuma','ambas']

# while True:
#   try:
#     for perna in pernas:
#      if perna == 'esquerda':
#        print('ingles')
#      elif perna == 'direita':
#        print('frances')
#      elif perna == 'nenhuma':
#        print('portugues')
#      elif perna == 'ambas':
#        print('caiu')
#     break
      
#   except Exception:
#     break 
  

# salario = 900

# def calcular_reajuste(salario):
#     reajuste = 0
#     if salario <= 600:
#         reajuste = 17
#     elif salario <= 900:
#         reajuste = 13
#     elif salario <= 1500:
#         reajuste = 12
#     elif salario <= 2000:
#         reajuste = 10
#     else:
#         reajuste = 5

#     return reajuste


# porcentagem = calcular_reajuste(salario)
# reajust = (salario*porcentagem) / 100
# print(f"Novo salario: {(salario + reajust):.2f}\nReajuste ganho: {reajust:.2f}\nEm percentual: {porcentagem} %")