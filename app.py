# Import required modules
import spacy  # For natural language processing
from fastapi import FastAPI  # For creating the FastAPI application
from pydantic import BaseModel  # For defining the input and output data models

# Create a FastAPI application instance
app = FastAPI()

# Load the pre-trained language model
model = spacy.load('api/models/en')

# Define a Pydantic model to represent the incoming user request
class UserRequestIn(BaseModel):
    text: str

# Define a Pydantic model to represent the output data
class EntitiesOut(BaseModel):
    entities: list  # A list of entity objects containing information about each entity
    anonymized_text: str  # The text with the identified entities anonymized

# Define a route for the FastAPI application
@app.post("/anonymize", response_model=EntitiesOut)
def extract_entities(user_request: UserRequestIn):
    # Get the text from the user request
    text = user_request.text
    # Process the text using the pre-trained model
    doc = model(text)

    # Extract the entities from the processed text and create a list of entity objects
    entities = [
        {
            "start": ent.start_char,  # Start position of the entity in the text
            "end": ent.end_char,  # End position of the entity in the text
            "type": ent.label_,  # Type of the entity (e.g., PERSON, ORG, etc.)
            "text": ent.text,  # The text of the entity
        }
        for ent in doc.ents  # Loop through each entity in the processed text
    ]

    # Anonymize the identified entities in the text
    anonymized_text = list(text)
    for entity in entities:
        start = entity["start"]
        end = entity["end"]
        anonymized_text[start:end] = "X" * (end - start)
    anonymized_text = "".join(anonymized_text)

    # Return the list of entities and the anonymized text as the response
    return {"entities": entities, "anonymized_text": anonymized_text}


# Add a simple route to check if the server is running
@app.get("/")
def read_root():
    return {"Business Data Science 2023 🚀💪"}
