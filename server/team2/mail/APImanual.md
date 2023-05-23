# [POST] /mail/getall

## request (client -> server)

```
{
    "auth": {
        "token": "*****",
        "refresh_token": "***",
        "expiry": "2023/04/25/ 10:10:50"
    }

}
```



## response (server -> client)
```
{ 
    "mails":[
        {   
            "id":"string",
            "threadId": "string",
            "snipet": "string",
            "body": "string",
            "subject": "string",
            "from": "string",
            "to": "string",
            "date": "2023-05-09"
            "expiry": "string"
        },
        {

        },
        ...
    ]

}
```
# [POST] mail/send

## request (client -> server)
```
{
    "auth": {
        "token": "*****",
        "refresh_token": "***",
        "expiry": "expiry": "2023/04/25/ 10:10:50"
    },
    "mail": {
        "to": "string",
        "subject": "string",
        "body": "string"
    }

}
```

## response (server -> client)
```
{ 
    "result": "string" ("success"/"failure")
    
}
```

# [POST] /translation/gpt

## request

```
{
    "word": "string"
}
```

## response

```
{
    "translated_words": [
        "string",
        "string",
        ...
    ]
}
```