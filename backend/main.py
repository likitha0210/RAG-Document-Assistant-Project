from fastapi import FastAPI, UploadFile, File
from pydantic import BaseModel
from rag_pipeline import load_pdf, build_vectorstore, ask_question

app = FastAPI()

# Swagger request schema
class QuestionRequest(BaseModel):
    question: str

@app.post("/upload/")
async def upload_pdf(file: UploadFile = File(...)):
    pdf_path = f"temp_{file.filename}"

    with open(pdf_path, "wb") as f:
        f.write(await file.read())

    docs = load_pdf(pdf_path)
    build_vectorstore(docs)

    return {"message": "PDF uploaded and processed successfully"}


@app.post("/ask/")
async def ask(req: QuestionRequest):
    answer = ask_question(req.question)
    return {"answer": answer}
