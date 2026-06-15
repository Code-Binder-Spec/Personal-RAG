import chromadb
from groq import Groq
import os
from pypdf import PdfReader

client = chromadb.PersistentClient("pdfvault.db")
collection = client.get_or_create_collection("pdfvault")

if collection.count() == 0 :
         
            full_page_data = []
            reader = PdfReader("C:/Users/adhim/OneDrive/Documents/ai_roadmap.pdf")
            for i in range(2):
                         page = reader.pages[i]
                         text = page.extract_text(extraction_mode="layout", layout_mode_space_vertically=False)
                         full_page_data.append(text)
            ids_v = [f"{i}" for i in range(1,(len(full_page_data)+1))]
            collection.add(
                    documents=full_page_data,
                    ids=ids_v,
                    metadatas=[{"page":int(page)}for page in ids_v]
            )

groq_client = Groq(api_key=(os.getenv("GROQ_API_KEY")))
print("\n Type stop in You for exit \n")
print(collection.count())

while True:

       query = str(input("YOU : "))
       if "stop" in query.lower():
                break
       result = collection.query(
               query_texts=[query],
               n_results=1
       )
       chunk = result["documents"][0][0]
       print(chunk)
       message = groq_client.chat.completions.create(
               model="llama-3.3-70b-versatile",
               max_tokens=1024,
               messages=[
                       {"role":"user","content":f"Context : {chunk}\n\nInstructions : Answer correctly based on the question.If theres no question from user force them to add question for reply.If the answer is not in the context say the answer is not in pdf.\n\nQuestion : {query}"}
               ]
       )
       print(F"AI : {message.choices[0].message.content}")



