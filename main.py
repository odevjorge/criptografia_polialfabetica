sc = [6, 5]

alfa = [
  'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o',
  'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd',
  'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's',
  't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h',
  'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w',
  'x', 'y', 'z'
]


def main():
  opcao, palavra = [
    int(input("Digite:\n0 para CRIPTOGRAFAR\n1 para DESCRIPTOGRAFAR\n: ")),
    str(input("\nDigite a palavra: "))
  ]


  for c in cript(opcao, palavra):
    print(c, end="")


def cript(opcao, palavra):
  def crip_palavra(palavra):
    if type(palavra) == str:
      palavra = list(palavra)

    lista = []
    for c in palavra:
      if c == " ":
        pass
      else:
        if opcao == 1:
          calc = 26 - sc[0]
        else:
          calc = sc[0]
          
        lista.append(int(alfa.index(c)) + calc)

    listaalfa = []
    for i in lista:
      listaalfa.append(alfa[i])

    return listaalfa

  paldecrip = crip_palavra(palavra)
  for c in range(sc[1]):
    paldecrip = crip_palavra(paldecrip)

  return paldecrip


if __name__ == '__main__':
  main()


