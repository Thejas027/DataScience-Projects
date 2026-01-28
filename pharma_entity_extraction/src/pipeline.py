import pandas as pd
import spacy

from company_extractor import extract_companies
from drug_extractor import extract_drugs
from molecule_extractor import extract_molecules

nlp = spacy.load("en_core_web_sm")

DATA_PATH = "../data/articles.csv"

def run_pipeline():
    df = pd.read_csv(DATA_PATH)

    for _, row in df.iterrows():
        text = row["article_text"]
        doc = nlp(text)

        company = extract_companies(text)
        drug = extract_drugs(text)
        molecule = extract_molecules(doc)

        print(f"Article ID: {int(row['article_id'])}")
        print(f"Drug Name: {drug}")
        print(f"Molecule: {molecule}")
        print(f"Organization: {company}")
        print("-" * 50)

if __name__ == "__main__":
    run_pipeline()
