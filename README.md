React Shop back-end made with Flask-RESTful

https://market-flask.herokuapp.com/

### Endpoints
#### GET
- /categories
- /products
- /customers
- /customers/all

#### Categories Params

| param    | description                                   | type   | example       |
|----------|-----------------------------------------------|--------|---------------|
| id       | Returns category specified by id              | string | "xjtFVYnD"    |
| category | Returns category specified by a category name | string | "Video Games" |

#### https://market-flask.herokuapp.com/categories?id=xjtFVYnD

~~~~{
"data": {
    "category_name": "Video Games",
    "cid": "xjtFVYnD",
    "num_of_products": 106,
    "sub_categories": [
    { 
        "name": "PlayStation 4",
        "types": [
          {
            "products": [...],
            "type_label": "Consoles"
          },
          {
            "products": [...],
            "type_label": "Games"
          }
        ]
    },
    {
        "name": "Nintendo Switch",
        "types": [
          {
            "products": [...],
            "type_label": "Consoles"
          },
          {
            "products": [...],
            "type_label": "Games"
          },
          {
            "products": [...],
            "type_label": "Accessories"
          }
        ]
    },
    {
        "name": "Xbox One",
        "types": [
          {
            "products": [...],
            "type_label": "Games"
          },
          {
            "products": [...],
            "type_label": "Consoles"
          },
          {
            "products": [...],
            "type_label": "Accessories"
          }
        ]
    }
    ]
  },
  "total_categories": 0,
  "total_products": 106
}
~~~~

#### Products Params

| param    | description                                                 | type    | example           |
|----------|-------------------------------------------------------------|---------|-------------------|
| id       | Returns product specified by id                             | string  | "J3dgJB6F"        |
| category | Return all products from specified category                 | string  | "Video Games"     |
| sub      | Return all products from specified subcategory              | string  | "Nintendo Switch" |
| type     | Return all products from specified product type             | string  | "Games"           |
| company  | Return all products from specified company/manufacturer     | string  | "Nintendo"        |
| minprice | Return products at a minimum price point                    | number  | 2000 ($20.00)     |
| maxprice | Return products at a maximum price point                    | number  | 60000 ($600.00)   |
| rating   | Return products with rating above specified value           | number  | 3                 |
| limit    | Return the maximum number of products (default 20 , max 50) | number  | 50                |
| offset   | Return products after specified length                      | number  | 20                |


#### https://market-flask.herokuapp.com/products?category=video%20games&sub=nintendo%20switch&minprice=1500

~~~~
{
  "data": {
    "list_companies": [
      "Nintendo",
      "Ubisoft",
      "Capcom"
    ],
    "list_subs": [
      "Nintendo Switch"
    ],
    "list_types": [
      "Consoles",
      "Games",
      "Accessories"
    ],
    "products": [
      {
        "about": {
          "description": "Introducing Nintendo Switch, the new home video game system from Nintendo. In addition to providing single and multiplayer thrills at home, the Nintende mobility of a handheld is now added to the power of a home gaming system, with unprecedented new play styles brought to life by the two new Joy-Con co...",
          "rating": 0,
          "release_date": 1555263433797
        },
        "category": {
          "category_name": "Video Games",
          "sub_category": {
            "name": "Nintendo Switch",
            "type": "Consoles"
          }
        },
        "company": "Nintendo",
        "created_at": "Sun, 14 Apr 2019 14:37:16 GMT",
        "images": [
          "https://res.cloudinary.com/db5msl9ld/image/upload/v1555263438/l00cua/l3dvqeqhv24mwwcbwguy.jpg"
        ],
        "num_of_shares": 0,
        "pid": "O7zS1yEa",
        "price": 29900,
        "price_percentage": 0,
        "quantity": 100,
        "title": "Nintendo Switch – Neon Red and Neon Blue Joy-Con"
      },
      {...}
    ],
    "query_next": "?limit=20&offset=11",
    "query_prev": "?limit=20&offset=0",
    "total_length": 12,
    "total_pages": 1,
    "total_query": 12
  }
}
~~~~

#### Customer Params

You can get a token and secret by simply logging in at https://market-react.herokuapp.com/log

User needs to be an admin. For that use the default user:

~~~~
email: test@user.com
password: abcd1234
~~~~

| param    | description                                   | type   | example                                        |
|----------|-----------------------------------------------|--------|------------------------------------------------|
| id       | Your user ID                                  | string | "Lf2TCMC1Yw"                                   |
| secret   | Your section secret key                       | string | "rZP0y2lg5A61NtC"                              |
| token    | Your section token                            | string | "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1..." |

#### https://market-flask.herokuapp.com/customer?id=Lf2TCMC1Yw&secret=secret_key&token=token

~~~~
{
  "data": {
    "created_at": "Tue, 14 May 2019 14:37:35 GMT",
    "email": "test@user.com",
    "id": "Lf2TCMC1Yw",
    "is_admin": false,
    "name": "Test User"
  }
}
~~~~

#### Customer/all Params

| param    | description                                   | type   | example                                        |
|----------|-----------------------------------------------|--------|------------------------------------------------|
| secret   | Your section secret key                       | string | "rZP0y2lg5A61NtC"                              |
| token    | Your section token                            | string | "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1..." |


#### https://market-flask.herokuapp.com/customer/all?secret=secret_key&token=token

~~~~
{
  "data": [
    {
      "created_at": "Sun, 12 May 2019 16:07:41 GMT",
      "email": "Amelia341@gmail.com",
      "id": "kkgIsRTCl4",
      "is_admin": false,
      "name": "Graves Rolando"
    },
    {
      "created_at": "Sun, 12 May 2019 16:07:41 GMT",
      "email": "Wilma001@gmail.com",
      "id": "2qiqv5Lu5w",
      "is_admin": false,
      "name": "Newman Tricia"
    },
    {
      "created_at": "Sun, 12 May 2019 16:07:42 GMT",
      "email": "Hubert640@gmail.com",
      "id": "5WXLsyxkrt",
      "is_admin": false,
      "name": "Dianna Norton"
    },
    {
      "created_at": "Tue, 14 May 2019 14:37:35 GMT",
      "email": "test@user.com",
      "id": "Lf2TCMC1Yw",
      "is_admin": true,
      "name": "Test User"
    }
  ]
}
~~~~
