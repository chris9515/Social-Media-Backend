# Social-Media-Backend

To build: 
```bash
docker-compose build
```


To run the containers: 
```bash
docker-compose up
```

The container will be up and running.

### API Endpoints

- JWT token: POST `http://127.0.0.1:8000/api/token/` will give us the JWT token in exchange to username and password. (The default username and password is **admin**)
- JWT token: POST `http://127.0.0.1.8000/api/follow/{id}` will make the current logged in user to follow the user with the specified user id
- JWT token: POST `http://127.0.0.1.8000/api/unfollow/{id}` will make the current logged in user to unfollow the user with the sepcified user id
- JWT token: GET `http://127.0.0.1.8000/api/user` will give back us the repective user profile
- JWT token: POST `http://127.0.0.1.8000/api/posts` will make the respective user post a new post
- JWT token: DELETE `http://127.0.0.1.8000/api/posts/{id}` will let the logged in user delete the post having corresponding id
- JWT token: POST `http://127.0.0.1.8000/api/like/{id}` will make the logged in user to like a specific post
- JWT token: POST `http://127.0.0.1.8000/api/unlike/{id}` will make the logged in user to remove the like given to a specific post
- JWT token: POST `http://127.0.0.1.8000/api/comment/{id}` will make the logged in user to comment on a specified post 
- JWT token: GET `http://127.0.0.1.8000/api/posts/{id}` will give us the details of a post with the specified id
- JWT token: GET `http://127.0.0.1.8000/api/all_posts{id}` will give us all the posts created by the logged in user
