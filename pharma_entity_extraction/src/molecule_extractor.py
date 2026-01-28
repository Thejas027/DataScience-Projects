MOLECULES = {
    "paracetamol",
    "ibuprofen",
    "nirmatrelvir",
    "ritonavir",
    "azithromycin"
}

def extract_molecules(doc):

    molecules = set()

    for token in doc:
        if token.text.lower() in MOLECULES:
            molecules.add(token.text.lower())

    return list(molecules)
