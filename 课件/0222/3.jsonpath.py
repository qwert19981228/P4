import jsonpath,json

books = '''
{ "store": {
    "book": [ 
      { "category": "reference",
        "author": "Nigel Rees",
        "title": "Sayings of the Century",
        "price": 8.95
      },
      { "category": "fiction",
        "author": "Evelyn Waugh",
        "title": "Sword of Honour",
        "price": 12.99
      },
      { "category": "fiction",
        "author": "Herman Melville",
        "title": "Moby Dick",
        "isbn": "0-553-21311-3",
        "price": 8.99
      },
      { "category": "fiction",
        "author": "J. R. R. Tolkien",
        "title": "The Lord of the Rings",
        "isbn": "0-395-19395-8",
        "price": 22.99
      }
    ],
    "bicycle": {
      "color": "red",
      "price": 19.95
    }
  }
}
'''
# 获取 book的所有信息
# res = jsonpath.jsonpath(json.loads(books),'$..book')
# 获取跟下的所有信息
# res = jsonpath.jsonpath(json.loads(books),'$.*')
# 获取book的素有单价
# res = jsonpath.jsonpath(json.loads(books),'$.store.book..price')
# 获取第2个数信息
# res = jsonpath.jsonpath(json.loads(books),'$.store.book[1,(@.length-1)]')
# 找到第一本书的价格
# res = jsonpath.jsonpath(json.loads(books),'$.store.book[0]..price')
# 获取book中有isbn
res = jsonpath.jsonpath(json.loads(books),'$.store.book[?(@.isbn)]')

print(res)