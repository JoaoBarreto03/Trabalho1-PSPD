from fastapi import FastAPI, Request, Form
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from client_grpc import contar_palavras, palavra_mais_frequente

app = FastAPI()
app.mount("/static", StaticFiles(directory="static"), name="static")

templates = Jinja2Templates(directory="templates")

# IPs dos servidores
VM2_IP = "192.168.122.35"   # CountWords
VM3_IP = "192.168.122.151"  # MostFrequentWord

@app.get("/", response_class=HTMLResponse)
def home(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

@app.post("/processar", response_class=HTMLResponse)
def processar(request: Request, texto: str = Form(...), servico: str = Form(...)):
    resultado = None
    palavra = None
    contagem = None

    if servico == "contar":
        resultado = contar_palavras(texto, VM2_IP)
    elif servico == "frequente":
        palavra, contagem = palavra_mais_frequente(texto, VM3_IP)
    elif servico == "ambos":
        resultado = contar_palavras(texto, VM2_IP)
        palavra, contagem = palavra_mais_frequente(texto, VM3_IP)

    return templates.TemplateResponse("index.html", {
        "request": request,
        "resultado": resultado,
        "mais_frequente": palavra,
        "contagem": contagem
    })

