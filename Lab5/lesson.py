import re
import csv

result =[["Order", "Name", "Total"]]


file = open(r'C:\Users\k_mir\OneDrive\Рабочий стол\PP2\Lab5\test.txt','r', encoding="utf8")

text = file.read()

BINPattern = "\nБИН\s+(?P<BIN>[0-9]{12})"
KassaPattern = "\nКасса\s+(?P<Kassa>.+)"

BINValue = re.search (BINPattern, text).group("BIN")
KassaValue = re.search (KassaPattern, text).group("Kassa")

print(BINValue)
print(KassaValue)
print()

ItemPatternText = r"\n(?P<Order>.*)\n(?P<Name>.*)\n(?P<Count>.*)x(?P<Price>.*)\n(?P<Subtotal>.*)\nСтоимость\n(?P<Total>.*)"
CompiledItemPattern = re.compile(ItemPatternText)
items = re.finditer(CompiledItemPattern, text)
for match in items:
    row = [match.group("Order"), match.group("Name"), match.group("Total")]
    result.append(row)
print(result)

with open(r'C:\Users\k_mir\OneDrive\Рабочий стол\PP2\Lab5\data.csv', 'w', newline='', encoding='utf8') as f:
    writer = csv.writer(f)
    writer.writerows(result)

file.close()