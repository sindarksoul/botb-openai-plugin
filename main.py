from fastapi import FastAPI
from fastapi.responses import JSONResponse
from utils.crypto_fetch import get_crypto_price
from utils.zip_utils import extract_zip
from utils.log_parser import parse_log
from utils.vm_control import control_vm
from utils.device_control import control_device

app = FastAPI(title="BOTB Plugin", description="Local File + Device + Crypto Assistant")

@app.get("/healthz")
def health_check():
    return {"status": "alive"}

@app.get("/crypto/{symbol}")
def crypto_price(symbol: str):
    return get_crypto_price(symbol)

@app.post("/unzip")
def unzip_file(path: str, dest: str):
    return extract_zip(path, dest)

@app.post("/parse-log")
def parse_log_file(path: str):
    return parse_log(path)

@app.post("/vm")
def vm_action(action: str):
    return control_vm(action)

@app.post("/device")
def smart_device(action: str):
    return control_device(action)
