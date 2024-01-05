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


class NormalizedBoundingBox(TypedDict):
    tag: str
    bottom: float
    left: float
    top: float
    right: float


from typing import Union

from fastapi import FastAPI

class ExtractionConfig(BaseModel):
    arr_normalized_bb: list[NormalizedBoundingBox]


app = FastAPI()

@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.get("/items/{item_id}")
def read_item(item_id: int, q: Union[str, None] = None):
    return {"item_id": item_id, "q": q}


@app.post("/process")
def define_Extraction(arr_normalized_bb:ExtractionConfig):
    return "processing api"


