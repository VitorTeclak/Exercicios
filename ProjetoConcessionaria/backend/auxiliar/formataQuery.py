def formatarResultados(resultados):
    dados = [dict(row) for row in resultados.mappings()]

    if not dados:
        print("Nenhum resultado encontrado.")
        return

    cabecalho = list(dados[0].keys())

    # Calcular largura máxima de cada coluna
    larguras = []
    for col in cabecalho:
        max_largura = max(len(str(col)), max(len(str(linha[col])) for linha in dados))
        larguras.append(max_largura)

    # Imprimir cabeçalho
    cab_str = " | ".join(col.upper().ljust(larguras[i]) for i, col in enumerate(cabecalho))
    print(cab_str)
    print("-" * len(cab_str))  # linha separadora

    # Imprimir linhas
    for linha in dados:
        linha_str = " | ".join(str(linha[col]).ljust(larguras[i]) for i, col in enumerate(cabecalho))
        print(linha_str)

