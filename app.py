from fastapi import FastAPI, Request, Depends, HTTPException
from pydantic import BaseModel
from sqlalchemy.orm import Session

from database import engine, Base, SessionLocal
from router import auth, doctors, patients

from router.auth import get_user_exception, get_current_user
import model
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
import json
import os


with open('config.json') as data_file:
    config = json.load(data_file)

app = FastAPI()

app.mount("/static", StaticFiles(directory="static"), name="static")
templates = Jinja2Templates(directory="templates")


class patient_payment(BaseModel):
    id: int
    name: str
    payment_status: int
    order_id:str
    amount:int

    # email_id: str
    class Config:
        orm_mode = True

def get_db():
    try:
        db = SessionLocal()
        yield db
    finally:
        db.close()

model.Base.metadata.create_all(bind=engine)

app.include_router(auth.router)
app.include_router(doctors.router)
app.include_router(patients.router)



# @app.get("/payment_gateway", response_class=HTMLResponse,tags=["patients"])
# async def read_item(request: Request, order_ID:str,db:Session=Depends(get_db)):
#     patient = db.query(model.Patients).filter(order_ID == model.Patients.order_id).first()
#         # if not patient:
#         #     return get_notfound_exception()

#     return templates.TemplateResponse("index.html", {"request": request, "amount": patient.amount,"order_id":order_ID,"name":patient.name,})



# --------------------- Pages --------------------- #
# -------------------------------------------------- #

# ------------------ Dashboard ------------------ #
@app.get("/", response_class=HTMLResponse, name="home")
async def home(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

# ------------------ Patient ------------------ #
@app.get("/patientPage", response_class=HTMLResponse, name="patientPage")
async def patientPage(request: Request):
    return templates.TemplateResponse("patient.html", {"request": request})

# ------------------ Admission ------------------ #
@app.get("/admissionPage", response_class=HTMLResponse, name="admissionPage")
async def admissionPage(request: Request):
    return templates.TemplateResponse("admission.html", {"request": request})

@app.get("/appointmentsPage", response_class=HTMLResponse, name="appointmentsPage")
async def appointmentsPage(request: Request):
    return templates.TemplateResponse("appointments.html", {"request": request})

# ------------------ Billings ------------------ #
@app.get("/billingsPage", response_class=HTMLResponse, name="billingsPage")
async def billingsPage(request: Request):
    return templates.TemplateResponse("billings.html", {"request": request})

@app.get("/labordersPage", response_class=HTMLResponse, name="labordersPage")
async def labordersPage(request: Request):
    return templates.TemplateResponse("lab-orders.html", {"request": request})

@app.get("/pharmacyPage", response_class=HTMLResponse, name="pharmacyPage")
async def pharmacyPage(request: Request):
    return templates.TemplateResponse("pharmacy.html", {"request": request})

@app.get("/radiologyPage", response_class=HTMLResponse, name="radiologyPage")
async def radiologyPage(request: Request):
    return templates.TemplateResponse("radiology.html", {"request": request})

@app.get("/rootPage", response_class=HTMLResponse, name="rootPage")
async def rootPage(request: Request):
    return templates.TemplateResponse("root.html", {"request": request})

@app.get("/statisticsPage", response_class=HTMLResponse, name="statisticsPage")
async def statisticsPage(request: Request):
    return templates.TemplateResponse("statistics.html", {"request": request})



# ------------------- Sub-pages ------------------- #
# ----------------------------------------------------- #

# ------------------ Add patient ------------------ #
@app.get("/addPatientPage", response_class=HTMLResponse, name="addPatientPage")
async def addPatientPage(request: Request):
    return templates.TemplateResponse("subpages/add-patient.html", {"request": request})


# @app.get("/accidentEmergencyForm", response_class=HTMLResponse, name="accidentEmergencyForm")
# async def accidentEmergencyForm(request: Request):
#     return templates.TemplateResponse("subpages/accidentEmergencyForm.html", {"request": request})

# @app.get("/ancfollowupForm", response_class=HTMLResponse, name="ancfollowupForm")
# async def ancfollowupForm(request: Request):
#     return templates.TemplateResponse("subpages/ancfollowupForm.html", {"request": request})

# @app.get("/accidentEmergencyForm", response_class=HTMLResponse, name="accidentEmergencyForm")
# async def accidentEmergencyForm(request: Request):
#     return templates.TemplateResponse("subpages/accidentEmergencyForm.html", {"request": request})

# @app.get("/dentalForm", response_class=HTMLResponse, name="dentalForm")
# async def dentalForm(request: Request):
#     return templates.TemplateResponse("subpages/dentalForm.html", {"request": request})

# @app.get("/eyeclinicForm", response_class=HTMLResponse, name="eyeclinicForm")
# async def eyeclinicForm(request: Request):
#     return templates.TemplateResponse("subpages/eyeclinicForm.html", {"request": request})

# @app.get("/gopdForm", response_class=HTMLResponse, name="gopdForm")
# async def gopdForm(request: Request):
#     return templates.TemplateResponse("subpages/gopdForm.html", {"request": request})

# @app.get("/internalmedicineForm", response_class=HTMLResponse, name="internalmedicineForm")
# async def internalmedicineForm(request: Request):
#     return templates.TemplateResponse("subpages/internalmedicineForm.html", {"request": request})



# @app.get("/{path}.html", response_class=HTMLResponse)
# async def render_template(path: str, request: Request):
#     return templates.TemplateResponse(f"{path}.html", {"request": request})


if __name__ == '__main__':
    app.run(debug=True,host=config['host'],port=config['port'])