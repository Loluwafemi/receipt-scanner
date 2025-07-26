from fastapi import FastAPI
from lib import ReceiptParameter


''' 
    This Project is intend to scan and interpret contents on receipt of any kind as long as the following parameter is found on it:
    1. Bank Name
    2. Account Name
    3. Transaction Amount
    4. & Transaction date-time

    A. The program work in hand with the fontend as this program can send a post request containing form data such as:
    1. Sender details
    2. File (Receipt Image)
    3. ViewPoints data

    There will be an AI agent which will use the frontend as a tool to identify data and return the axis data just like how a human will do.

    B. This program on a unit level [must use], will takes in slice of file and interprete its data to text, making it meaningful. But this is done asynchronously:
    The system accepts parameters defined above with file slice (as image) as a dictionary (key-value) and return the parameter with the text interpretatiun.

    The output is confirmed by two ends. First by the AI agent (when on live), then by the requester which is either admin or app user.


    C. The system uses an isolated db to manage all data, this is to ensure integration to other systems and lightweight and quick manipulation by ai agents (which is modification of captured axis boundaries)


    ##########################################################################
    Requests are:
    -x :Get: show_registries -> all saved receipt registries
    -y :Post: interprete -> translate text on image to string and return object/dictionary
    -z :Post: register_receipt -> save to db, must include author: admin/agent
    -u :Post: verify data before submission
    


    Flow:
        async call on y, which send the file slice, axis and key and return a single dictionary

        if all y is true/valid: save using z

        by default, x will always fetch all saved data


'''

app = FastAPI()

@app.get("/")
async def read_root():
    return {"message": "Hello, World!"}



@app.get("/registries")
async def read_root():
    return {"message": "Hello, World!"}



@app.post("/interprete")
async def read_root(request: ReceiptParameter):

    return {"message": 'request'}