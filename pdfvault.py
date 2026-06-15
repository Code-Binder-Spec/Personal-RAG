import chromadb
from pypdf import PdfReader

client = chromadb.PersistentClient("pdfvault.db")
collection = client.get_or_create_collection("pdfvault")

if collection.count() == 0 :
         
            full_page_data = []
            reader = PdfReader("C:/Users/adhim/OneDrive/Documents/ai_roadmap.pdf")
            for i in range(1,3):
                         page = reader.pages[i]
                         text = page.extract_text(extraction_mode="layout", layout_mode_space_vertically=False)
                         full_page_data.append(text)
            ids_v = [f"{i}" for i in range(1,(len(full_page_data)+1))]
            collection.add(
                    documents=full_page_data,
                    ids=ids_v,
                    metadatas=[{"page":int(page)}for page in ids_v]
            )

while True:
       print("\n Type stop in You for exit")
       query = str(input("YOU : "))
       result = collection.query(
               query_texts=[query],
               n_results=2
       )
