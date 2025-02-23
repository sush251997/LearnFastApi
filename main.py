from fastapi import FastAPI


app = FastAPI()


@app.get('/')
def index():
    return {'data':{'name':'Sushant'}}


@app.get("/blog/unpublished")
def unpublished():
    return {"data":["defining all unpublished blogs"]}


@app.get("/blog/{blog_id}")
def about(blog_id: int):
    return {"Data":blog_id}