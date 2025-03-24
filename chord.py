import requests
import json
import os
abc = open('art1').read()
inp3 = abc.splitlines()
for inpn in inp3:
 print(inpn)
 main = f"""
 <!DOCTYPE html>
 <html lang="en">
 <head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{inpn}</title>
    <style>"""


 main2 = """       body {
            font-family: Arial, sans-serif;
            margin: 0;
            padding: 0;
            background-color: #f8f9fa;
            display: flex;
            justify-content: center;
            align-items: center;
            height: 100vh;
        }
        .container {
            width: 90%;
            max-width: 1200px;
        }
        .product-grid {
            display: flex;
            justify-content: space-between;
            flex-wrap: wrap;
            gap: 20px;
        }
        .product {
            width: calc(20% - 20px);
            background-color: white;
            padding: 15px;
            border-radius: 8px;
            box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
            text-align: center;
        }
        .product img {
            width: 100%;
            border-radius: 5px;
        }
        .product h3 {
            margin: 10px 0;
            font-size: 18px;
        }
        .product p {
            color: #555;
        }
        .product button {
            background-color: #28a745;
            color: white;
            border: none;
            padding: 10px 15px;
            cursor: pointer;
            border-radius: 5px;
        }
        .product button:hover {
            background-color: #218838;
        }
    </style>
</head>
<body>
    <div class="container">
        <div class="product-grid">
"""
 text = open('data.json').read()
 jj = json.loads(text)

 filei = open(f'./{inpn}.html','a')
 filei.write(main)
 filei.write(main2)
 for i in range(0,10000):
  try:
   ja = jj['data']['songs'][i]['id']
   jb = jj['data']['songs'][i]['name']
   jc = jj['data']['songs'][i]['artis']
   je = jj['data']['songs'][i]['link']
  except IndexError:
   pass
  else:
   #print(jc) 
   if jc == inpn:
    #print(jb,'\n',jc,'\n',je,'\n----')
    htmlx = f"""            <div class="product">
                <h3>{jb}</h3>
                <p>{jc}</p>
                <a href='{je}'><button>Download</button></a>
            </div>"""
    filei.write(htmlx)
   else:
    pass

 ending = """        </div>
    </div>
</body>
</html>"""

 filei.write(ending)
 #os.system(f"firefox '{inpn}.html'")
