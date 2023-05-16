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
            "expiry_time":"2023-04-25T10:10:50.292762Z",
            "title":"string",
            "to":"string",
            "from":"string",
            "body":"string",
            "date":"2023-05-09"
        },
        {

        },
        ...
    ]

}

# [POST] mail/send


get, post(get+データ送る), 