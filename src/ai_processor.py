import google.generativeai as genai
from pathlib import Path

def sumarize_legal_text(text: str, api_key: str) -> str:

    """Summarize legal text using Google Generative AI."""

    # Initialize the GenAI client with the provided API key
    genai.configure(api_key=api_key)

    # Selecting the 'gemini-1.5 Flash' model for summarization
    model = genai.GenerativeModel('gemini-1.5 Flash')

    prompt = f'''
    You are an expert legal assitant specialized in Paraguayan real state Law.
    Analyze the following deed text and provide a concise summary including:
    1. Transaction Type
    2. Parties involved (Sellers, Buyers, Usufructuaries)
    3. Property Details (Finca, Cuenta Corriente, Location)
    4. Price and Payment terms.
    5. Any special conditions or clauses mentioned in the deed.
    6. Date of the transaction.

    Text to analyze:
    {text}
    '''

    # Generate the summary using the model
    response = model.generate_content(prompt)
    return response.text