# grpc_sample
* Its a sample gRPC python basic example

### Compile command
  ```python -m grpc_tools.protoc  -Iprotos --python_out=compiles --grpc_python_out=compiles hello.proto```
  

### Setup Project
  create a virtualenv and install the packages by running the below command
  ``` python -m pip install -r requirements.txt```


### Running Project

  First run the gRPC server
  ```python server.py```
  server will start ```localhost:50051```

  Next run python flask server
  ```python start.py```
  flask server will start ```localhost:5000```
  
  Open the link in browser ```http://127.0.0.1:5000/```