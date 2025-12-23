from decisao_nicho import analisar_nichos

def executar():
    print("\n🔍 ANÁLISE DE NICHO COM IA")
    print("-" * 40)

    objetivo = input("\nDescreva seu objetivo:\n> ")

    print("\n⏳ Analisando com a IA...\n")

    resultado = analisar_nichos(objetivo)

    print("📊 RESULTADO DA IA:")
    print("-" * 40)

    if resultado:
        print(resultado)
    else:
        print("⚠️ A IA não retornou resposta. Verifique o prompt.")

    print("\n--- FIM DA ANÁLISE ---\n")

if __name__ == "__main__":
    executar()
