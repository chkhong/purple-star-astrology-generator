import uvicorn
from fastapi import FastAPI, Body
from fastapi.responses import JSONResponse
from fastapi.middleware.cors import CORSMiddleware
from loguru import logger
import traceback
from schema import schema
from functions.arranger import Arranger

arranger = Arranger()

app = FastAPI(
  title="Sample Application",
  description="Backend API",
)

# allow CORS setting
origins = ['*']

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# security setting
# https://geekflare.com/http-header-implementation/https://geekflare.com/http-header-implementation/
HEADERS = {
    # CORS setting
    "Access-Control-Allow-Credentials": "true",
    "Access-Control-Allow-Origin": "*",
    "Access-Control-Allow-Methods": "*",
    "Access-Control-Allow-Headers": "*",
    # security setting
    "X-Frame-Options": "SAMEORIGIN",
    "X-Content-Type-Options": "nosniff",
    "X-XSS-Protection": "1; mode=block",
    "Strict-Transport-Security": "max-age=31536000; includeSubDomains",
    "Expect-CT": "max-age=86400, enforce", # enforcement of Certificate Transparency for 24 hours
    "Content-Security-Policy": "default-src https:"
}

OUTPUT_RESPONSE = {
    "success": False,
    "message": "",
    "data": {}
}

def set_out_response(**args)->dict:
    ''' merge args into OUTPUT_RESPONSE,
        param @args, e.g. args = { 'success': True, 'data': {...} }
    '''
    # content = dict(OUTPUT_RESPONSE, **args)

    response = JSONResponse(content=args, headers=HEADERS)

    # return content # return content w/o headers
    return response # return content w/ headers

@app.get('/')
def hello():
  return {"message": "App is running..."}

@app.post('/arrange')
def arrange(payload:schema.Request = Body(..., examples=schema.Request.Example.examples)):
  r = {}
  try:
    payload = dict(payload) 
    r = arranger.arrange(year=payload['year'],month=payload['month'],day=payload['day'],hour=payload['hour'],minute=payload['minute'])
  except Exception as e:
    logger.error(e)
    logger.error(traceback.format_exc())
  finally:
    return r


if __name__ == '__main__':
  uvicorn.run("main:app", host="127.0.0.1", port=5000, log_level="info", reload=True)