import random

def escolher_palavra():

    palavras = ["cruzeiro", "futebol", "python", "brasil", "algoritmo"]
    return random.choice(palavras)

def jogo_da_forca():
    palavra = escolher_palavra()
    tentativas_restantes = 6
    letras_tentadas = []
    palavra_oculta = ["_" for _ in palavra]
    
    print("Que comece o jogo!")
    
    while tentativas_restantes > 0 and "_" in palavra_oculta:
        print("\nPalavra:", " ".join(palavra_oculta))
        print(f"Tentativas restantes: {tentativas_restantes}")
        print(f"Letras tentadas: {', '.join(letras_tentadas)}")
        
        letra = input("Digite uma letra: ").lower()
        
        if letra in letras_tentadas:
            print("Você já tentou essa letra. Tente outra.")
            continue
        
        letras_tentadas.append(letra)
        
        if letra in palavra:
            print(f"A letra '{letra}' está na palavra.")
            for i, l in enumerate(palavra):
                if l == letra:
                    palavra_oculta[i] = letra
        else:
            print(f"A letra '{letra}' não está na palavra.")
            tentativas_restantes -= 1
    
    if "_" not in palavra_oculta:
        print("\n-VITÓRIA- Você acertou a palavra:", palavra)
    else:
        print("\nVocê perdeu! A palavra era:", palavra)


jogo_da_forca()
