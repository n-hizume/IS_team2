# [POST] /mail/getall

## request (client -> server)

{
    auth: {
        "token": "*****",
        "refresh_token": "***",
        "expiry": "2023-04-25T10:10:50.292762Z"
    }

}


## response (server -> client)

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
        },
        {

        },
        ...
    ]

}

# [POST] mail/send

## request (client -> server)

{
    auth: {
        "token": "*****",
        "refresh_token": "***",
        "expiry": "2023-04-25T10:10:50.292762Z"
    }

}


## response (server -> client)

{ 
    "mail":{   
            "id":"string",
            "threadId": "string",
            "snipet": "string",
            "body": "string",
            "subject": "string",
            "from": "string",
            "to": "string",
    }
    
}

get, post(get+データ送る), 