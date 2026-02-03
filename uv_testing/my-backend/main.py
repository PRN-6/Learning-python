from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def read_root():
    return {"hello world"}

def main():
    print("Hello from my-backend!")

    
if __name__ == "__main__":
    main()
