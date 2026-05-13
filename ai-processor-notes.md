How it works step-by-step:
1. The Connection (genai.configure)
It uses your API Key to open a secure "tunnel" between your computer and Google's servers. Without this key, the script cannot talk to the AI.

2. Selecting the Model (GenerativeModel)
You are choosing Gemini 1.5 Flash. In engineering terms, this is like picking the right tool for the job. "Flash" is optimized for speed and high-volume text processing, making it perfect for summarizing long legal documents without costing much in tokens.

3. The "Architectural Brief" (The Prompt)
This is the most important part. You aren't just asking "summarize this." You are giving the AI a Professional Persona and a Structure:

Persona: "Expert legal assistant specialized in Paraguayan real estate law." This forces the AI to look for specific legal nuances.

Specific Requirements: By listing 1 through 4 (Parties, Finca, Price, etc.), you ensure the AI doesn't get distracted by irrelevant notary filler and goes straight to the data you need for your family records.

4. The Execution (generate_content)
The script sends your cleaned text and the instructions to the cloud. Gemini processes the logic and returns a string of text containing the formatted summary.