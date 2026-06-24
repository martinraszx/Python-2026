tablero = dict(
    letra = [" A ", " B ", " C ", " D ", " E ", " F ", " G ", " H "],
    uno = ["NT1", "NC1", "NA1", "NR ", "NK ", "NA2", "NC2", "NT2"],
    dos = ["NP1","NP2","NP3","NP4","NP5","NP6","NP7","NP8"],
    tres = ["   ", "   ", "   ", "   ", "   ", "   ", "   ", "   "],
    cuatro = ["   ", "   ", "   ", "   ", "   ", "   ", "   ", "   "],
    cinco = ["   ", "   ", "   ", "   ", "   ", "   ", "   ", "   "],
    seis = ["   ", "   ", "   ", "   ", "   ", "   ", "   ", "   "],
    siete = ["BP1","BP2","BP3","BP4","BP5","BP6","BP7","BP8"],
    ocho = ["BT1", "BC1", "BA1", "BR ", "BK ", "BA2", "BC2", "BT2"]
)

tipos = ("letra","uno", "dos", "tres", "cuatro", "cinco", "seis","siete", "ocho")

for i in range(len(tablero)):
    total = tipos[i]
    print("-----------------------------------")
    print(f"{i} |{"|".join(tablero[total])}|")
