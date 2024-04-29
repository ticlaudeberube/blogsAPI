from fastapi import FastAPI, HTTPException
from typing import List
from blog_post import BlogPost
import uuid

host = 'https://www.ipsofactointeractif.ca'
app = FastAPI()
NOT_FOUND_MESSAGE = "Blogpost not found"
DUPLICATE_ITEM = "Blogpost already exits"
blogPosts: List[BlogPost] = []

# Route to add a new blogpost
@app.post("/blogposts")
def create_blogpost(item: BlogPost):
    for blogpost in blogPosts:
        if blogpost.title == item.title:
            raise HTTPException(status_code=403, detail=DUPLICATE_ITEM)
    item.id = str(uuid.uuid4())
    blogPosts.append(item)
    return item

# Route to get all blogposts
@app.get("/blogposts")
def get_blogposts():
    return blogPosts

# Route to get a specific blogpost by ID
@app.get("/blogposts/{item_id}")
def get_blogpost(item_id: str):
    for blogpost in blogPosts:
        if blogpost.id == item_id:
            return blogpost

    raise HTTPException(status_code=404, detail=NOT_FOUND_MESSAGE)

# Route to get a specific blogpost by ID
@app.put("/blogposts/{item_id}", response_model=BlogPost)
def update_blogpost(item_id: str, item: BlogPost):
    for i, blogpost in enumerate(blogPosts):
        if blogpost.id == item_id:
            blogPosts[i] = item
            return item
    raise HTTPException(status_code=404, detail=NOT_FOUND_MESSAGE)

from typing import Dict, Union

@app.delete("/blogposts/{item_id}")
def delete_blogpost(item_id: str) -> Dict[str, Union[int, str]]:
    return { "code": 200, "deleted": "true" }

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="localhost", port=8000)
