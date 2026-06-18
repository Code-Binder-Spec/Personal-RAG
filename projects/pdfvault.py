import chromadb
from groq import Groq
import os
from pypdf import PdfReader
import math

client = chromadb.PersistentClient("pdfvault.db")
collection = client.get_or_create_collection("pdfvault")

if collection.count() == 0 :
         
            full_page_data = []
            reader = PdfReader("C:/Users/adhim/OneDrive/Documents/ai_roadmap.pdf")
            pages_count = len(reader.pages)
            for i in range(pages_count):
                         page = reader.pages[i]
                         text = page.extract_text(extraction_mode="layout", layout_mode_space_vertically=False)
                         full_page_data.append(text)
            text_joined = " ".join(full_page_data)
            text_splitted = text_joined.split()
            total_chunks_needed = len(text_splitted)/200
            if isinstance(total_chunks_needed,float):
                   total_chunks_needed =  math.ceil(total_chunks_needed)
            chunks = []
            extra_safety_last_word = []
            starting = 0
            for i in range(1,(total_chunks_needed+1)):  
                    word_count = i*200
                    chunk_text = " ".join(text_splitted[starting:word_count])
                    last_words = word_count - 50
                    last_word_text = " ".join(text_splitted[last_words:word_count])
                    extra_safety_last_word.append(last_word_text)
                    chunks.append(chunk_text)
                    starting+=200
            for i in range(len(extra_safety_last_word)-1):
                    chunks[i+1] = extra_safety_last_word[i] + chunks[i+1]
            ids_v = [f"{i}" for i in range((len(full_page_data)+1))]
            collection.add(
                    documents=chunks,
                    ids=ids_v,
                    metadatas=[{"page":int(page)}for page in ids_v]
            )

groq_client = Groq(api_key=(os.getenv("GROQ_API_KEY")))
print("\nType stop in You for exit \n")

while True:
      
       query = str(input("YOU : "))
       if "stop" in query.lower():
                break
       result = collection.query(
               query_texts=[query],
               n_results=3
       )
       chunk = result["documents"][0]
       message = groq_client.chat.completions.create(
               model="llama-3.3-70b-versatile",
               max_tokens=1024,
               messages=[
                       {"role":"user","content":f"Context : {chunk}\n\nInstructions : Answer the user's question using only the provided context. If no question is given, ask the user to provide one. If the answer isn't found in the context, say it's not in the PDF. Retrieved chunks may overlap — avoid repeating duplicate information, and if an answer spans multiple chunks, combine them into one clear response.\n\nQuestion : {query}"}
               ]
       )
       print(F"AI : {message.choices[0].message.content}")



