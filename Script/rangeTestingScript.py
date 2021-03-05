maxOhm = int(input("Max ohm (darkest):"))
minOhm = int(input("Min ohm (lightest):"))

fixedOhm = int(input("Fixed ohm:"))

maxVoltageDrop = maxOhm / (fixedOhm + maxOhm)
minVoltageDrop = minOhm / (fixedOhm + minOhm)

maxVout = 5 * (1 - minVoltageDrop)
minVout = 5 * (1 - maxVoltageDrop)

# ======================================================================

bestEff = 0
for i in range(minOhm, maxOhm + 1):
    RmaxVoltageDrop = maxOhm / (i + maxOhm)
    RminVoltageDrop = minOhm / (i + minOhm)

    RmaxVout = 5 * (1 - RminVoltageDrop)
    RminVout = 5 * (1 - RmaxVoltageDrop)

    # print(i)
    # print(f"max volt {RmaxVout}")
    # print(f"min volt {RminVout}")

    eff = RmaxVout - RminVout
    # print(eff)
    # print()
    if eff > bestEff:
        result = i
        bestEff = eff
        bestRmaxVout = RmaxVout
        bestRminVout = RminVout
        bestRmaxVoltageDrop = RmaxVoltageDrop
        bestRminVoltageDrop = RminVoltageDrop

print(f"Maximum LDR voltage drop >>> {maxVoltageDrop * 100} %")
print(f"Minimum LDR voltage drop >>> {minVoltageDrop * 100} %")
print("")
print(f"Maximum voltage out >>> {maxVout}V")
print(f"Minimum voltage out >>> {minVout}V")
print(f"Efficiency: {maxVout - minVout}")
print("-----------------------------------")
print(f"Recmmended fixed resistance >>> {result} ohm")
print("Recmmened resistance result ↓↓↓↓↓")
print(f"Maximum LDR voltage drop >>> {bestRmaxVoltageDrop * 100} %")
print(f"Minimum LDR voltage drop >>> {bestRminVoltageDrop * 100} %")
print("")
print(f"Maximum voltage out >>> {bestRmaxVout}V")
print(f"Minimum voltage out >>> {bestRminVout}V")
print(f"Efficiency: {bestEff}")
