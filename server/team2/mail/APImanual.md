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
            "expiry": int
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
        "expiry": "2023/04/25/ 10:10:50"
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
    "level": int(0 or 1 or 2)
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