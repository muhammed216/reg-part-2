)cumle = "en sevdigim kanal base42"
patern = r"\s\w{5, }"

for eslesme in re.finditer(patern, cumle):
    print(eslesme.group(), eslesme.span()


