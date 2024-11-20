#exibir suas notas
nota1 = float(input("Digite a primeira nota: "))
nota2 = float(input("Digite a segunda nota: "))
nota3 = float(input("Digite a terceira nota:"))

# Calculando a média
media = (nota1 + nota2 + nota3) / 3


if media > 5.0 and media < 6.0:
    print("Recuperação")
elif media >= 6.0:
    print("Aprovado")
else:
    print("Reprovado")


  #Verificando se o aluno foi aprovado ou reprovado
if media >= 6:
    print("Você foi aprovado!")
else:
    print("Você foi reprovado!")

# Exibindo o resultado
print(f"Sua média final é: {media:.2f}")

