# import libs
try:
    from PIL import Image
except ImportError:
    import Image
import cv2
import pytesseract
import os
import numpy as np
import pandas as pd
import re
from pdf2image import convert_from_bytes
from pydantic import BaseModel
from typing import TypedDict, Optional
import logging
import processor.extractor
from contextlib import asynccontextmanager


class NormalizedBoundingBox(TypedDict):
    tag: str
    bottom: float
    left: float
    top: float
    right: float


from typing import Union

from fastapi import FastAPI,HTTPException,status
from fastapi.middleware.cors import CORSMiddleware
import psycopg2
import dbConnect

@asynccontextmanager
async def lifespan(app: FastAPI):
    logging.info("before start")
    dbConnect.connect()
    yield
    logging.info("before shut down")


logging.basicConfig(format='%(asctime)s - %(message)s', level=logging.INFO)
# logging.info('Admin logged in')


class ExtractionConfig(BaseModel):
    arr_normalized_bb: list[NormalizedBoundingBox]


app = FastAPI(lifespan=lifespan)

origins = [
    "http://localhost:3000",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.on_event("startup")


@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.get("/items/{item_id}")
def read_item(item_id: int, q: Union[str, None] = None):
    return {"item_id": item_id, "q": q}


@app.post("/process",status_code=201)
def define_Extraction(arr_normalized_bb:ExtractionConfig):
    extracted = processor.extractor.extractText(arr_normalized_bb)
    return extracted


