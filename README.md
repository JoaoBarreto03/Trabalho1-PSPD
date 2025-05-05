# Trabalho 1 de PSPD


## 1. Alunos

| Nome | Matrícula|
|---|---|
| Artur Vinícius | 190142421 |
| Henrique Hida | 180113569 |
| João Manoel Barreto Neto | 211039519 | 
| Leonardo Milomes Vitoriano | 201000379 | 
| Miguel Matos Costa de Frias Barbosa | 211039635 |


## 2. Objetivo

Construir uma aplicação distribuída com **gRPC** e **ProtoBuffer** e explorar virtualização para suportar a aplicação. Server em **gRPC Golang (GO)**, backend/client em **gRPC python** e **FastAPI**, frontend em **HTML/CSS**.

A aplicação será um microserviço de contador de palavras, onde as palavras são contadas e a palavra mais frequente é apresentada. 

Adicione o texto desejado e depois escolha os serviços: ```Contar Palavras (histograma)```, ou  ```Palavra mais frequente``` ou ```Ambos``` para realizar os 2 serviços. Isso no frontend da aplicação.



## 3. Tecnologias

### 3.1. gRPC
O [gRPC](https://grpc.io/) (RPC da GOOGLE) é uma estrutura que permite a comunicação eficiente entre clientes e servidores por meio do protocolo HTTP/2, proporcionando alta performance e boa escalabilidade em sistemas distribuídos.

### 3.2. Virtualização

Este projeto faz uso da virtualização com o auxílio de ferramentas como **QEMU**, **Libvirt**, **Virt-manager** e **virsh** para criar e gerenciar máquinas virtuais, que compõem a base da infraestrutura distribuída implementada.

## 4. Requisitos

### 4.1. Ferramentas Necessárias

A execução deste projeto requer a instalação das seguintes ferramentas:

- **Git**: Utilizado para o controle e versionamento do código-fonte.

- **gRPC**: Responsável por estabelecer a comunicação entre cliente e servidor.

- **QEMU/KVM**: Empregados na criação e execução das máquinas virtuais.

- **Libvirt**: Usado para gerenciar os recursos das VMs.

- **Virt-manager**: Fornece uma interface gráfica para facilitar o gerenciamento das máquinas virtuais.


### 4.2. Capacidades das VMs

- **vm01:** 20GB de disco, 2GB de RAM e 2 CPUs.
- **vm02:** 20GB de disco, 2GB de RAM e 2 CPUs.
- **vm03:** 20GB de disco, 2GB de RAM e 2 CPUs.


## 5. Passo a Passo para Implementação

### 5.1. Instalação do Git e Configuração do Repositório

```bash
sudo apt update
sudo apt install git
```
Clone o repositório:
```bash
git clone https://github.com/JoaoBarreto03/Trabalho1-PSPD.git
```



### 5.2. Preparando o Ambiente para o gRPC

Clone o repositório gRPC e Faça a intalação localmente conforme no site oficial e linguagem:

- Servidores [GO](https://grpc.io/docs/languages/go/quickstart/)
- Cliente  [Python](https://grpc.io/docs/languages/python/quickstart/)

Lembre-se de executar o servidor antes do cliente.


#### 5.2.1. Executando Servidor (VM2 e VM3) em GO


```bash
go run server.go
```


#### 5.2.2. Executando Servidor (VM1) em Python


```bash
sudo apt install python3-pip
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```


### 5.3. Configuração da Virtualização



1. Instale o QEMU, libvirt e virt-manager:

```bash
sudo apt install qemu-kvm libvirt-daemon-system libvirt-clients bridge-utils virt-manager
```
2. Crie e configure as VMs (VM01 e VM02 e VM03) com **virt-manager** ou **virsh**.


### 5.4. Configuração de Rede

Configure duas redes:

- **LAN #1**: Rede conectando os hosts.
- **LAN #2**: Rede virtual conectando as VMs.


### 5.5 Executando o Backend (gRPC cliente VM1)


```bash
uvicorn main:app --host 0.0.0.0 --port 8080
```


Abra o navegador e acesse:

```
http://localhost:8080/
```

OU

```
http://<IP_DA_VM_CLIENTE>:8080/
```


## 6. Estrutura do Projeto


- **B1-gRPC**: Pasta com códigos de exemplo utilizando gRPC.
- **B2-apl-gRPC**: Códigos dos serviços **P**, **A** e **B**, descritos no enunciado do problema.
- **B3-wordCount**: Pasta com códigos das máquinas virtuais e separado por VMs.
- **README.md**: Este arquivo com instruções do projeto.


## 7. Entrega

A entrega consiste em:
1. **Relatório**: Descrição do gRPC, virtualização e a infraestrutura configurada.
2. **Arquivos das VMs** configuradas.
3. **Vídeo** de apresentação.
4. **Documentação dos códigos** e configurações.

## 8. Links Úteis

- [gRPC](https://grpc.io/)
- [QEMU](https://www.qemu.org/)
- [Libvirt](https://libvirt.org/)
- [Virt-Manager](https://virt-manager.org/)









<!-- ### Virtual Environment with python (venv)


```bash




python3 -m venv venv
pip install -r requirements.txt




```


## B.3


### VM1 (Ubunutu Desktop 22.04)


user vm1
ping 192.168.122.77

ssh vm1@192.168.122.77



#### Comandos

```bash

sudo apt install python3-pip
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
uvicorn main:app --host 0.0.0.0 --port 8080


```



### VM2 (Ubuntu Server 22.04)


user vm2
ping 192.168.122.35

ssh vm2@192.168.122.35



```bash

protoc --go_out=. --go-grpc_out=. proto/wordcount.proto

```


### VM3 (Ubuntu Server 22.04)


user: vm3
ping 192.168.122.151


ssh vm3@192.168.122.151 -->


