from fastapi import FastAPI, Request, Form
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from client_grpc import contar_palavras

app = FastAPI()
templates = Jinja2Templates(directory="templates")

# IPs das VMs que rodam os servidores gRPC
GRPC_SERVERS = ["192.168.122.253", "192.168.122.142"]

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


