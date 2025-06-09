from fastapi import FastAPI
from pydantic import BaseModel
from fastapi import Cookie, Header

app = FastAPI()

houses = {
    "gryffindor": {
        "founder": "Godric Gryffindor",
        "mascot": "Lion",
        "colors": ["Red", "Gold"],
        "head": "Professor McGonagall"
    },
    "hufflepuff": {
        "founder": "Helga Hufflepuff",
        "mascot": "Badger",
        "colors": ["Yellow", "Black"],
        "head": "Professor Sprout"
    },
    "ravenclaw": {
        "founder": "Rowena Ravenclaw",
        "mascot": "Eagle",
        "colors": ["Blue", "Bronze"],
        "head": "Professor Flitwick"

    },
    "slytherin": {
        "founder": "Salazar Slytherin",
        "mascot": "Serpent",
        "colors": ["Green", "Silver"],
        "head": "Professor Snape"
    }
}
@app.get("/")
async def root_route():
    return {"message": "Welcome to the Harry Potter world!"}

@app.get("/houses")
async def all_houses():
    return houses

@app.get("/house/{name}")
async def get_house_info(name: str):
    return {"house": name, "details": houses.get(name)}

@app.get("/sortingHat")
async def sortingHat(student: str):
    return {"message": f"The sorting hat is not sure about what house to place {student}"}

@app.get("/house/{name}/head")
async def houseHead(name: str):
    selectedHouse = houses.get(name)
    return {"house": name, "head": selectedHouse.get("head")}

@app.get("/spells")
async def spell(spell: str):
    return {"message": f"we need to learn how to do {spell} "}

@app.get("/house/{name}/mascot")
async def mascot(name: str):
    selectedHouse = houses.get(name)
    return {"house": name, "mascot": selectedHouse.get("mascot")}

@app.get("/house/{name}/founder")
async def founder(name: str):
    selectedHouse = houses.get(name)
    return {"house": name, "founder": selectedHouse.get("founder")}

@app.get("/bestCharacter")
async def bestCharacter(person: str):
    return {"message": f"{person} is indeed a great character"}

@app.get("/house/{name}/colors")
async def colors(name: str):
    selectedHouse = houses.get(name)
    return {"house": name, "colors": selectedHouse.get("colors")}

@app.get("/welcome")
async def readCookie(username: str=Cookie(None)):
    return {"username": username}

@app.get("/verify-house")
async def verify_house(house: str = Header(None)):
    if house == "Hufflepuff":
        return "Hufflepuff"
    return "Not HufflePuff"

class PersonInput(BaseModel):
    name: str
    house: str

@app.post("/hello_personclass")
async def hello_personclass(input: PersonInput):
    return f" {input.name}, welcome to {input.house} "

