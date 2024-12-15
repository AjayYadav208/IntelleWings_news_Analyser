import spacy

# Load the spaCy model for Named Entity Recognition
nlp = spacy.load('en_core_web_sm')

# Function to extract entities from text
def extract_entities(text):
    doc = nlp(text)
    entities = {'PERSON': [], 'ORG': []}

    # Extract PERSON and ORG entities
    for ent in doc.ents:
        if ent.label_ == 'PERSON':
            entities['PERSON'].append(ent.text)
        elif ent.label_ == 'ORG':
            entities['ORG'].append(ent.text)
    
    return entities
