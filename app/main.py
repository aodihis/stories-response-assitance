from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

app = FastAPI()
app.mount("/static", StaticFiles(directory="static"), name="static")
templates = Jinja2Templates(directory="templates")

@app.get("/", response_class=HTMLResponse)
async def indexrequest(request: Request):
    return templates.TemplateResponse("index.html",{"request": request})

@app.post("/request")
async def readRequest(request: Request):
    return {'data': ["Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Cursus turpis massa tincidunt dui ut. Pulvinar neque laoreet suspendisse interdum consectetur libero. Lectus nulla at volutpat diam ut venenatis. Risus commodo viverra maecenas accumsan. Imperdiet nulla malesuada pellentesque elit eget gravida cum sociis natoque. Nibh tortor id aliquet lectus proin nibh nisl condimentum id. Egestas fringilla phasellus faucibus scelerisque eleifend donec pretium. Velit aliquet sagittis id consectetur purus ut faucibus pulvinar. Egestas erat imperdiet sed euismod nisi porta lorem. Cursus turpis massa tincidunt dui ut ornare lectus. Urna et pharetra pharetra massa massa ultricies.",
                     "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Cursus turpis massa tincidunt dui ut. Pulvinar neque laoreet suspendisse interdum consectetur libero. Lectus nulla at volutpat diam ut venenatis. Risus commodo viverra maecenas accumsan. Imperdiet nulla malesuada pellentesque elit eget gravida cum sociis natoque. Nibh tortor id aliquet lectus proin nibh nisl condimentum id. Egestas fringilla phasellus faucibus scelerisque eleifend donec pretium. Velit aliquet sagittis id consectetur purus ut faucibus pulvinar. Egestas erat imperdiet sed euismod nisi porta lorem. Cursus turpis massa tincidunt dui ut ornare lectus. Urna et pharetra pharetra massa massa ultricies."
                  ]}