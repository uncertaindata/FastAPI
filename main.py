from fastapi import FastAPI, HTTPException

app = FastAPI()
items = []
@app.get('/')
def root():
    return {"Hello" : "World"}

@app.post('/items')
def create_item(item : str):
    items.append(item)
    return items


@app.get('/item_list/{item_id}')
def get_item(item_id : int):
    if item_id < len(items):
        return items[item_id]
    else:
        raise HTTPException(status_code = 404,detail = "Item Index Not Allowed")