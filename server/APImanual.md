# [POST] /mail/getall

## request (client -> server)

```
{
    "auth": {
        "token": "*****",
        "refresh_token": "***",
        "expiry": int
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
            "date": "2023-05-09T10:10+09:00"
            "expiry": "2023-05-10T24:00+09:00"
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
        "expiry": int
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