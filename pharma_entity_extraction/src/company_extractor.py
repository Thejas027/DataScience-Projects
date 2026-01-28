import spacy

nlp = spacy.load("en_core_web_sm")

def extract_companies(text):

    if not isinstance(text, str) or not text.strip():
        return []

    doc = nlp(text)
    companies = set()

    for ent in doc.ents:
        if ent.label_ == "ORG":
            companies.add(ent.text)

    return list(companies)
