React Shop back-end made with Flask-RESTful
https://flask-market.herokuapp.com

### Endpoints
- /categories
- /products

#### Categories Params

| param    | description                                   | type   | example       |
|----------|-----------------------------------------------|--------|---------------|
| id       | Returns category specified by id              | string | "xjtFVYnD"    |
| category | Returns category specified by a category name | string | "Video Games" |

#### https://flask-market.herokuapp.com/categories?id=xjtFVYnD

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


#### https://flask-market.herokuapp.com/products?category=video%20games&sub=nintendo%20switch&minprice=1500

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
      {
        "about": {
          "description": "Gaming icons clash in the ultimate brawl you can play anytime, anywhere! Smash rivals off the stage as...",
          "rating": 0,
          "release_date": 1555263528359
        },
        "category": {
          "category_name": "Video Games",
          "sub_category": {
            "name": "Nintendo Switch",
            "type": "Games"
          }
        },
        "company": "Nintendo",
        "created_at": "Sun, 14 Apr 2019 14:38:52 GMT",
        "images": [
          "https://res.cloudinary.com/db5msl9ld/image/upload/v1555263535/hx1vwl/oprbskwhfmpmzugt3fws.jpg"
        ],
        "num_of_shares": 0,
        "pid": "J3dgJB6F",
        "price": 5999,
        "price_percentage": 17,
        "quantity": 100,
        "title": "Super Smash Bros. Ultimate"
      },
      {
        "about": {
          "description": "Inspired by original Mario Party board game play...",
          "rating": 0,
          "release_date": 1555263927944
        },
        "category": {
          "category_name": "Video Games",
          "sub_category": {
            "name": "Nintendo Switch",
            "type": "Games"
          }
        },
        "company": "Nintendo",
        "created_at": "Sun, 14 Apr 2019 14:45:30 GMT",
        "images": [
          "https://res.cloudinary.com/db5msl9ld/image/upload/v1555263933/lwekr7/opx29yb1uxfhsvt5qdxb.jpg"
        ],
        "num_of_shares": 0,
        "pid": "MuWlfweL",
        "price": 5900,
        "price_percentage": 0,
        "quantity": 100,
        "title": "Super Mario Party"
      },
      {
        "about": {
          "description": "Jump into a new Yoshi adventure in a world made of everyday objects—like boxes and paper cups! As Yoshi, you’ll leap up ...",
          "rating": 4,
          "release_date": "22-04-2019"
        },
        "category": {
          "category_name": "Video Games",
          "sub_category": {
            "name": "Nintendo Switch",
            "type": "Games"
          }
        },
        "company": "Nintendo",
        "created_at": "Mon, 22 Apr 2019 19:24:16 GMT",
        "images": [
          "https://images-na.ssl-images-amazon.com/images/I/91N72kmLpbL._AC_SL1500_.jpg"
        ],
        "num_of_shares": 0,
        "pid": "ykTipKap",
        "price": 5799,
        "price_percentage": 0,
        "quantity": 100,
        "title": "Yoshi's Crafted World - Nintendo Switch"
      },
      {
        "about": {
          "description": "Join Mario, Luigi, and Pals for single-player or multiplayer fun anytime, anywhere! take on two family-friendly...",
          "rating": 4,
          "release_date": "22-04-2019"
        },
        "category": {
          "category_name": "Video Games",
          "sub_category": {
            "name": "Nintendo Switch",
            "type": "Games"
          }
        },
        "company": "Nintendo",
        "created_at": "Mon, 22 Apr 2019 19:24:26 GMT",
        "images": [
          "https://images-na.ssl-images-amazon.com/images/I/813JPZr%2BpCL._AC_SL1500_.jpg"
        ],
        "num_of_shares": 0,
        "pid": "r3Gxlkg6",
        "price": 5499,
        "price_percentage": 0,
        "quantity": 100,
        "title": "New Super Mario Bros. U Deluxe - Nintendo Switch"
      },
      {
        "about": {
          "description": "Dance to your own beat with Just Dance 2019, the ultimat...",
          "rating": 4,
          "release_date": "22-04-2019"
        },
        "category": {
          "category_name": "Video Games",
          "sub_category": {
            "name": "Nintendo Switch",
            "type": "Games"
          }
        },
        "company": "Ubisoft",
        "created_at": "Mon, 22 Apr 2019 19:24:35 GMT",
        "images": [
          "https://images-na.ssl-images-amazon.com/images/I/81qZbC6FvzL._AC_SL1500_.jpg"
        ],
        "num_of_shares": 0,
        "pid": "OiBsCzZQ",
        "price": 1999,
        "price_percentage": 0,
        "quantity": 100,
        "title": "Just Dance 2019 - Nintendo Switch Standard Edition"
      },
      {
        "about": {
          "description": "This pass includes the following downloadable content...",
          "rating": 4,
          "release_date": "22-04-2019"
        },
        "category": {
          "category_name": "Video Games",
          "sub_category": {
            "name": "Nintendo Switch",
            "type": "Games"
          }
        },
        "company": "Nintendo",
        "created_at": "Mon, 22 Apr 2019 19:24:43 GMT",
        "images": [
          "https://images-na.ssl-images-amazon.com/images/I/81cZQGx9x-L._AC_SL1500_.jpg"
        ],
        "num_of_shares": 0,
        "pid": "kLo0BI4H",
        "price": 2499,
        "price_percentage": 0,
        "quantity": 100,
        "title": "Super Smash Bros. Ultimate Fighter Pass DLC - Nintendo Switch [Digital Code]"
      },
      {
        "about": {
          "description": "Minecraft is bigger, better and more beautiful than ever! Build anything you can imagine in Creative mode...",
          "rating": 4,
          "release_date": "22-04-2019"
        },
        "category": {
          "category_name": "Video Games",
          "sub_category": {
            "name": "Nintendo Switch",
            "type": "Games"
          }
        },
        "company": "Nintendo",
        "created_at": "Mon, 22 Apr 2019 19:24:50 GMT",
        "images": [
          ""
        ],
        "num_of_shares": 0,
        "pid": "cu2cRrR7",
        "price": 2799,
        "price_percentage": 0,
        "quantity": 100,
        "title": "Minecraft - Nintendo Switch"
      },
      {
        "about": {
          "description": "The critically acclaimed action-RPG Dragon's Dogma: Dark Arisen makes its way to Nintendo Switch...",
          "rating": 0,
          "release_date": "22-04-2019"
        },
        "category": {
          "category_name": "Video Games",
          "sub_category": {
            "name": "Nintendo Switch",
            "type": "Games"
          }
        },
        "company": "Capcom",
        "created_at": "Mon, 22 Apr 2019 19:24:52 GMT",
        "images": [
          "https://images-na.ssl-images-amazon.com/images/I/61ci3sFlLHL._AC_SL1004_.jpg"
        ],
        "num_of_shares": 0,
        "pid": "biBqLWjx",
        "price": 2999,
        "price_percentage": 0,
        "quantity": 100,
        "title": "Dragon's Dogma: Dark Arisen - Nintendo Switch"
      },
      {
        "about": {
          "description": "Introducing your gateway into the most immersive, robust Nintendo Labo kit to date—this one combines DIY fun...",
          "rating": 4,
          "release_date": "22-04-2019"
        },
        "category": {
          "category_name": "Video Games",
          "sub_category": {
            "name": "Nintendo Switch",
            "type": "Games"
          }
        },
        "company": "Nintendo",
        "created_at": "Mon, 22 Apr 2019 19:24:59 GMT",
        "images": [
          "https://images-na.ssl-images-amazon.com/images/I/71k8vM6RrdL._AC_SL1500_.jpg"
        ],
        "num_of_shares": 0,
        "pid": "5Aqn1tjB",
        "price": 3999,
        "price_percentage": 0,
        "quantity": 100,
        "title": "Nintendo Labo Toy-Con 04: VR Kit - Starter Set + Blaster - Switch"
      },
      {
        "about": {
          "description": "Pokemon Let's Go Pikachu for Nintendo Switch Take your Pokémon journey to the Kanto region with your energetic partner...",
          "rating": 4,
          "release_date": "22-04-2019"
        },
        "category": {
          "category_name": "Video Games",
          "sub_category": {
            "name": "Nintendo Switch",
            "type": "Games"
          }
        },
        "company": "Nintendo",
        "created_at": "Mon, 22 Apr 2019 19:25:05 GMT",
        "images": [
          "https://images-na.ssl-images-amazon.com/images/I/81eJlNQ1UCL._AC_SL1500_.jpg"
        ],
        "num_of_shares": 0,
        "pid": "3mmDpUFh",
        "price": 4599,
        "price_percentage": 0,
        "quantity": 100,
        "title": "Pokemon: Let's Go, Pikachu!"
      },
      {
        "about": {
          "description": "Take your game sessions up a notch with the Nintendo Switch Pro Controller. Includes motion controls, HD rumble, built-in amiibo functionality, and more. ",
          "rating": 0,
          "release_date": 1556440453080
        },
        "category": {
          "category_name": "Video Games",
          "sub_category": {
            "name": "Nintendo Switch",
            "type": "Accessories"
          }
        },
        "company": "Nintendo",
        "created_at": "Sun, 28 Apr 2019 05:34:15 GMT",
        "images": [
          "https://res.cloudinary.com/db5msl9ld/image/upload/v1556440458/747ixp/pmkntdfxhychsenli9hm.jpg"
        ],
        "num_of_shares": 0,
        "pid": "zUhMSiSW",
        "price": 6999,
        "price_percentage": 19,
        "quantity": 100,
        "title": "Nintendo Switch Pro Controller"
      }
    ],
    "query_next": "?limit=20&offset=11",
    "query_prev": "?limit=20&offset=0",
    "total_length": 12,
    "total_pages": 1,
    "total_query": 12
  }
}
~~~~

