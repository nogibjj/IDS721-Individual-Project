# Project 1

http://3.144.194.197/

### Cloud Continuous Delivery of Microservice (MLOps or Data Engineering Focused)

- Create a Microservice in Flask or Fast API
- Push source code to Github
- Configure Build System to Deploy changes
- Use IaC (Infrastructure as Code) to deploy code
- Use either AWS, Azure, GCP (recommended services include Google App Engine, AWS App Runner or Azure App Services)
- Containerization is optional, but recommended

Reference Video(s):

- Data Engineering with Python and AWS Lambda: https://learning.oreilly.com/videos/data-engineering-with/9780135964330
- Building AI & ML Applications on Google Cloud Platform: https://learning.oreilly.com/videos/building-ai-applications/9780135973462

Reference Source Code: https://github.com/noahgift/gcp-hello-ml


Development:
```bash
docker build -t ids721-proj1 .   
docker run --rm -p 80:80 casnz1601/ids721-proj1   
docker tag ids721-proj1 casnz1601/ids721-proj1     
docker push casnz1601/ids721-proj1  
```