from fastapi import FastAPI

app = FastAPI()

@app.get("/my-first-api")
def hello(name: str):
  return {'Hello ' + name + '!'}

# Press the green button in the gutter to run the script.






# See PyCharm help at https://www.jetbrains.com/help/pycharm/
