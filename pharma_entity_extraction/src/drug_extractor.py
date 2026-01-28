import spacy
from spacy.matcher import PhraseMatcher

nlp = spacy.load("en_core_web_sm")

DRUG_NAMES = [
    "Paxlovid",
    "Tylenol",
    "Advil",
    "Aspirin",
    "Metformin",
    "Dolo 650",
    "Azee 500"
]

def extract_drugs(text):

    if not isinstance(text, str) or not text.strip():
        return []

    doc = nlp(text)

    matcher = PhraseMatcher(nlp.vocab, attr="LOWER")
    patterns = [nlp.make_doc(drug) for drug in DRUG_NAMES]
    matcher.add("DRUG", patterns)

    matches = matcher(doc)
    drugs = set()

    for _, start, end in matches:
        drugs.add(doc[start:end].text)

    return list(drugs)
