try:
    indice_satisfacao = int(input("Como você avalia nosso atendimento? Dê uma nota de 0 a 100: "))

    if indice_satisfacao < 0 or indice_satisfacao > 100:
        print("Informe um número válido!")
    else:
        if indice_satisfacao >= 90:
            print(f"Nota atribuída: {indice_satisfacao}. Atendimento de Qualidade")
        elif indice_satisfacao >= 70:
            print(f"Nota atribuída: {indice_satisfacao}. Atendimento neutro")
        else:
            print(f"Nota atribuída: {indice_satisfacao}. Atendimento insatisfatório")

except ValueError:
    print("Informe um número válido!")
