from fastapi import FastAPI, UploadFile, File
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

# Allow frontend to connect to backend
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/")
def home():
    return {
        "message": "AI Resume Scanner Backend is running"
    }


@app.post("/upload-resume")
async def upload_resume(file: UploadFile = File(...)):
    return {
        "filename": file.filename,
        "message": "Resume uploaded successfully"
    }