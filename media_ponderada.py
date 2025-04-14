nota1,nota2,nota3,nota4 = map(float, input().split())
nota1 *= 2
nota2 *= 3
nota3 *= 4
media = (nota1+nota2+nota3+nota4)/10
print(f'Media: {media:.1f}')
if media >= 7:
    print(f'Aluno aprovado.')
elif media >= 5 and media <= 6.9:
    print(f'Aluno em exame.')
    exame = float(input())
    print(f'Nota do exame: {exame:.1f}')
    mediafinal = (media + exame)/2
    if mediafinal >= 5:
        print(f'Aluno aprovado.')
    else:
        print(f'Aluno reprovado.')
    print(f'Media final: {mediafinal:.1f}')
elif media <5:
        print(f'Aluno reprovado.')


        