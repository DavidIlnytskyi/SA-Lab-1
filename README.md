# SA-Lab-1
**Author: Davyd Ilnytkyi**


# Results
## POST
**Sending two messages ("I am message {1, 2}") via Postman:**

![alt text](./images/POST_postman.png)

**Facade service console:**
![alt text](./images/POST_facade.png)

**Logging service console:**![alt text](./images/POST_logging.png)


## GET
**Sending GET request via Postman**
![alt text](./images/GET_postman.png)

**Facade service console:**
![alt text](./images/GET_facade.png)

**Logging service console:**
![alt text](./images/GET_logging.png)

**Messages service console:**
![alt text](./images/GET_messages.png)


## Retry functionality
**To test retry system I have shotted down logging_service, so there was no answer:**
![alt text](./images/POST_postman_retry.png)

**After a retry, server sends this message:**
![alt text](./images/POST_postman_retry_result.png)

**Facade service console**:
![alt text](./images/POST_facade_retry.png)

## Deduplication functionality
**To test deduplication functionality I generate the same UUID for a message**\
Sending first message(this one has uuid 9991):
![alt text](./images/POST_postman_deduplication.png)

Sending second message(this one also has uuid 9991):\
![alt text](./images/POST_postman_deduplication_result.png)

**Facade service console:**
![alt text](./images/POST_facade_deduplication.png)

**Logging service console:**
![alt text](./images/POST_logging_deduplication.png)

# Usage
```
pip install -r requirements.txt
```

```
python3 facade_service.py
```


```
python3 logging_service.py
```


```
python3 messages_service.py
```

**Send requests via Postman or something.**