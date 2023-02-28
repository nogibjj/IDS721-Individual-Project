# Project 2: Kubernetes based Continuous Delivery 
- Create a customized Docker container.
- Push image to DockerHub, or Cloud based Container Registry (ECR)
- Project should deploy automatically to Kubernetes cluster
- Deployment is to some form of Kubernetes service (Amazon EKS)
- Reference Reading: https://learning.oreilly.com/library/view/python-for-devops/9781492057680/ch09.html#containers-docker
- Reference Source Code: https://github.com/noahgift/container-revolution-devops-microservices


--- 
### Instructions of how to use the deployment of this project:

`kubectl get services`
```bash
NAME            TYPE           CLUSTER-IP      EXTERNAL-IP                                                               PORT(S)          
auth-service    ClusterIP      10.100.199.85   <none>                                                                    3000/TCP      
kubernetes      ClusterIP      10.100.0.1      <none>                                                                    443/TCP        
users-service   LoadBalancer   10.100.9.35     aab2033fe89cb4b7c9da2de527af7aba-1620600369.us-east-1.elb.amazonaws.com   80:30404/TCP   
```

Please use Postman to test the API endpoints. The API endpoints are:  

http://aab2033fe89cb4b7c9da2de527af7aba-1620600369.us-east-1.elb.amazonaws.com/signup   
Sample Request: POST(raw JSON)
```JSON
{
    "email": "test@test.com",
    "password": "testers"
}
```
Sample Response: 
```JSON
{
    "message": "User created.",
    "user": {
        "_id": "6418cf7f5c59597f38beffee",
        "email": "test@test.com",
        "password": "$2a$12$zsoduk5PhVxqOkR5JXzYo..moBqXkSmQm/f/dTtNe2kadreA7tVZO",
        "__v": 0
    }
}
```

---
http://aab2033fe89cb4b7c9da2de527af7aba-1620600369.us-east-1.elb.amazonaws.com/login    
Sample Request: POST(raw JSON)
```JSON
{
    "email": "test@test.com",
    "password": "testers"
}
```
Sample Response:
```JSON
{
    "token": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpYXQiOjE2NzkzNDc2ODUsImV4cCI6MTY3OTM1MTI4NX0.4IA9_wS1g63fWuCUI2zicigFHrXyv9Rg1oWAQ1-73bE",
    "userId": "6418cb2f5c595994debeffea"
}
```