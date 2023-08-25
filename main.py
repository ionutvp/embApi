from fastapi import FastAPI
#from sentence_transformers import SentenceTransformer
from fastapi.middleware.cors import CORSMiddleware
from gradio_client import Client

app = FastAPI()

origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
@app.get("/")
def read_root():
    
    client = Client("https://ionutvp-clip-embeddings.hf.space/")
    urlLink ="https://picsum.photos/id/1/200/300"
    result = client.predict(
				urlLink,	# str in 'url' Textbox component
				api_name="/predict"
)
    #print(result)
    return {result}

@app.get("/i/{id}")
async def read_item(id: int):
    urlLink = "https://picsum.photos/id/"+str(id)+"/200/300"
    
    client = Client("https://ionutvp-clip-embeddings.hf.space/")
    result = client.predict(
	    urlLink,	# str in 'url' Textbox component
		api_name="/predict")
    return {result}

@app.get("/p/{folderId}/{pictureId}")
def pred_image(folderId: str, pictureId:str):
    #https://jnvqzybejoxjibkygcgk.supabase.co/storage/v1/object/public/private/349/ec56f45ce5725.png
    # return {'path': full_path}
    urlLink = "https://jnvqzybejoxjibkygcgk.supabase.co/storage/v1/object/public/private/"+folderId+"/"+pictureId+".png"

    client = Client("https://ionutvp-clip-embeddings.hf.space/")
    result = client.predict(
	    urlLink,	# str in 'url' Textbox component
		api_name="/predict")
    return {result}

# @app.get("/items/{full_path:path}")
# def read_items(full_path:str):
#     client = Client("https://ionutvp-clip-embeddings.hf.space/")
#     result = client.predict(
# 	    full_path,	# str in 'url' Textbox component
# 		api_name="/predict"
# )
#     #print(result)
#     return {result}