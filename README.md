[![Build Status](https://travis-ci.org/andela-jmwangi/bucketlist-api.svg?branch=feature-review)](https://travis-ci.org/andela-jmwangi/bucketlist-api)
[![Coverage Status](https://coveralls.io/repos/github/andela-jmwangi/MasduRestApi/badge.svg?branch=feature-review)](https://coveralls.io/github/andela-jmwangi/MasduRestApi?branch=feature-review)
![MIT License Badge](https://img.shields.io/badge/license-mit-blue.svg)
[![Code Health](https://landscape.io/github/andela-jmwangi/MasduRestApi/feature-review/landscape.svg?style=flat)](https://landscape.io/github/andela-jmwangi/MasduRestApi/feature-review)


## Masdu Rest Api

## What is it?

Django Rest Api for [Masdu Bucketlist Application](http://masdu.herokuapp.com/)

## Features

- Registering a new user
- Authenticating users
- Creating a bucketlist
- Creating bucketlist items
- Crud actions on bucketlists and bucketlist items


### Available API Endpoints


| Endpoint                              | Functionality                         |
|---------------------------------------|-------------------------------------|
| POST /api/auth/register               | Create a new user                   |
| POST /api/auth/login/                 | Get an authentication token         |
| POST /api/bucketlists/                | Create a new bucket list              |
| GET  /api/bucketlists/                | List all the created bucket lists     |
| GET  /api/bucketlists/id              | Get single bucket list                |
| PUT /api/bucketlists/id                 | Update this bucket list             |
| DELETE /api/bucketlists/id              | Delete this single bucket list      |
| POST /api/bucketlists/id/items          | Create a bucketlist item              |
| PUT /api/bucketlists/id/items/id      | Update a bucketlist item            |
| DELETE /api/bucketlists/id/items/id   | Update a bucketlist item            |

## Usage

For developers, the API docs can be accessed on [Masdu API Docs](https://masduapi.herokuapp.com/docs/).

#### Example usage (Note: Examples use [HTTPie](https://github.com/jkbrzt/httpie) to send requests)

Registration:

```
http -f POST masduapi.herokuapp.com/api/auth/register/  username=testuser password=1234 email=testuser@test.com

HTTP/1.1 201 Created
Allow: POST, OPTIONS
Connection: keep-alive
Content-Type: application/json
Date: Fri, 15 Apr 2016 09:04:03 GMT
Server: gunicorn/19.4.5
Transfer-Encoding: chunked
Vary: Accept
Via: 1.1 vegur
X-Frame-Options: SAMEORIGIN

```

Login

```
http -f POST masduapi.herokuapp.com/api/auth/login/  username=testuser password=1234

HTTP/1.1 200 OK
Allow: POST, OPTIONS
Connection: keep-alive
Content-Type: application/json
Date: Fri, 15 Apr 2016 09:06:17 GMT
Server: gunicorn/19.4.5
Transfer-Encoding: chunked
Via: 1.1 vegur
X-Frame-Options: SAMEORIGIN

{
    "token": "b2be7eb7e5eebd4c3d348285249ba819868e7d89"
}
```

## Testing

In the project root folder, run command `python manage.py test --settings=MasduRestApi.settings.test`

## License

The MIT License

Copyright (c) 2016 Jack Mwangi

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in
all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
THE SOFTWARE.
