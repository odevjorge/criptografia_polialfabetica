sc = [6, 8]

# ALFABETO * 2 PORQUE SE ELE CHEGAR NO Z O PROXIMO JÁ VAI SER O INDEX DA PRIMERA LETRA
alfa = [
  'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o',
  'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd',
  'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's',
  't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h',
  'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w',
  'x', 'y', 'z'
]

# FUNÇÃO QUE VAI CHAMAR A FUNÇÃO DE CRIPTOGRAFIA
def main():
  opcao, palavra = [
    int(input("Digite:\n0 para CRIPTOGRAFAR\n1 para DESCRIPTOGRAFAR\n: ")),
    str(input("\nDigite a palavra: ")).lower()
  ]

  for c in cript(opcao, palavra):  # FOR QUE VAI IMPLRIMIT A FRAZE
    print(c, end="")


# FUNÇÃO QUE ORGANIZA A CRIPTOGRAFIA
def cript(opcao, palavra):
  # FUNÇÃO QUE VAI FAZER A CRIPTOGRAFIA EM SI
  def crip_palavra(palavra):
    if type(palavra) == str:  # IF QUE VAI TRANSFORMAR E ENTRADA EM UMA LISTA SE FOR UMA STRING
      palavra = list(palavra)

    lista = []
    for c in palavra:  # FOR QUE VAI LETRA POR LETRA SOMANDO O INDEX DA LETRA + O SALTO
      if c == " ":
        pass
      else:
        if opcao == 1:  # IF PARA SABER SE ELE VAI CRIPTOGRAFAR OU DESCRIPTOGRAFAR
          calc = 26 - sc[0]
        else:
          calc = sc[0]
        
        # SE O ELE FOR DESCRIPTOGRAFAR ELE VAI PEGAR O INDEX DO (ALFABETO - SALTO) E VAI SOMAR COM O INDEX DA LETRA ATUAL
        # OU SEJA O INDEX VAI PARAR NO SEGUNDO ALFABETO NA LISTA QUE VAI SER A EXATA LETRA QUE ELE PRECISA
          
        lista.append(int(alfa.index(c)) + calc)

    listaalfa = []
    for i in lista:  # FOR PARA TRANSFORMAR A LISTA DE LETRAS QUE É NUMERIA EM LETRA
      listaalfa.append(alfa[i])

    return listaalfa

  paldecrip = crip_palavra(palavra)
  for c in range(sc[1] - 1):  # FOR QUE VAI FAZER A QUANTIDADE DE SALTOS -1 PORQUE O PRIMEIRO FOI FEITO NA VARIAVEL ACIMA
    paldecrip = crip_palavra(paldecrip)

  return paldecrip

# IF QUE VAI INICIAR O PROGRAMA SE O NOME DO ARQUIVO FOR MAIN
if __name__ == '__main__':
  main()


