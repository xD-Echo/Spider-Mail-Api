from fastapi import FastAPI, HTTPException
import random
import platform,subprocess
import os
import requests
app = FastAPI()

@app.get("/")
def route():
    return "Spider Mail "


def read_random_lines_from_file(filename: str, amount: int) -> str:
    with open(filename, 'r',errors="ignore") as file:

        lines = file.readlines()
        random_lines = random.sample(lines, min(amount, len(lines)))
        return '|'.join(random_lines)

@app.get("/{file_name}/{amount}")
def get_random_lines(file_name: str, amount: int):
    file_path = file_name + ".txt"

    try:
        random_lines = read_random_lines_from_file(file_path, amount)
        return random_lines
    except FileNotFoundError:
        raise HTTPException(status_code=404, detail="File not found")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
