✅ File written successfully.
✅ Lines appended successfully.

--- Reading File ---
1. Topic 1: Variables store data. Python is dynamically typed.
2. Topic 2: Lists are ordered and mutable.
3. Topic 3: Dictionaries store key-value pairs.
4. Topic 4: Loops automate repetitive tasks.
5. Topic 5: Exception handling prevents crashes.
6. Topic 6: Functions help reuse code.
7. Topic 7: Modules help organize code.

Total number of lines: 7

Enter keyword to search: help

Search Results:
Topic 6: Functions help reuse code.
Topic 7: Modules help organize code.

--- Fetching Products ---
ID   | Title                          | Category        | Price    | Rating
---------------------------------------------------------------------------
1    | Essence Mascara Lash Princess  | beauty          | $9.99    | 2.56
2    | Eyeshadow Palette with Mirror  | beauty          | $19.99   | 2.86
3    | Powder Canister                | beauty          | $14.99   | 4.64
4    | Red Lipstick                   | beauty          | $12.99   | 4.36
5    | Red Nail Polish                | beauty          | $8.99    | 4.32
6    | Calvin Klein CK One            | fragrances      | $49.99   | 4.37
7    | Chanel Coco Noir Eau De        | fragrances      | $129.99  | 4.26
8    | Dior J'adore                   | fragrances      | $89.99   | 3.8
9    | Dolce Shine Eau de             | fragrances      | $69.99   | 3.96
10   | Gucci Bloom Eau de             | fragrances      | $79.99   | 2.74
11   | Annibale Colombo Bed           | furniture       | $1899.99 | 4.77
12   | Annibale Colombo Sofa          | furniture       | $2499.99 | 3.92
13   | Bedside Table African Cherry   | furniture       | $299.99  | 2.87
14   | Knoll Saarinen Executive Conference Chair | furniture       | $499.99  | 4.88
15   | Wooden Bathroom Sink With Mirror | furniture       | $799.99  | 3.59
16   | Apple                          | groceries       | $1.99    | 4.19
17   | Beef Steak                     | groceries       | $12.99   | 4.47
18   | Cat Food                       | groceries       | $8.99    | 3.13
19   | Chicken Meat                   | groceries       | $9.99    | 3.19
20   | Cooking Oil                    | groceries       | $4.99    | 4.8

--- Filtered Products (Rating ≥ 4.5, Sorted by Price Desc) ---
Annibale Colombo Bed | $1899.99 | Rating: 4.77
Knoll Saarinen Executive Conference Chair | $499.99 | Rating: 4.88
Powder Canister | $14.99 | Rating: 4.64
Cooking Oil | $4.99 | Rating: 4.8

--- Laptops Category ---
Apple MacBook Pro 14 Inch Space Grey — $1999.99
Asus Zenbook Pro Dual Screen Laptop — $1799.99
Huawei Matebook X Pro — $1399.99
Lenovo Yoga 920 — $1099.99
New DELL XPS 13 9300 Laptop — $1499.99

--- Creating New Product (Simulated) ---
Response from server:
{'id': 195, 'title': 'My Custom Product', 'price': 999, 'description': 'A product I created via API', 'category': 'electronics'}

--- Safe Divide Tests ---
5.0
Error: Cannot divide by zero
Error: Invalid input types

--- File Read Test (Valid) ---
File operation attempt complete.
Topic 1: Variables store data. Python is dynamically typed.
Topic 2: Lists are ordered and mutable.
Topic 3: Dictionaries store key-value pairs.
Topic 4: Loops automate repetitive tasks.
Topic 5: Exception handling prevents crashes.
Topic 6: Functions help reuse code.
Topic 7: Modules help organize code.


--- File Read Test (Invalid) ---
Error: File 'ghost_file.txt' not found.
File operation attempt complete.
None

--- Robust API Call ---
Essence Mascara Lash Princess
Eyeshadow Palette with Mirror
Powder Canister
Red Lipstick
Red Nail Polish

--- Product Lookup ---

Enter a product ID (1–100) or 'quit': 10
Gucci Bloom Eau de — $79.99

Enter a product ID (1–100) or 'quit': quit
Exiting...

--- Testing Connection Error ---
Connection failed (expected). Logging error...

--- Testing HTTP Error (404) ---
HTTP error detected. Logging error...

--- Error Log Contents ---
[2026-04-03 22:32:48] ERROR in fetch_products: ConnectionError — HTTPSConnectionPool(host='this-host-does-not-exist-xyz.com', port=443): Max retries exceeded with url: /api (Caused by NameResolutionError("HTTPSConnection(host='this-host-does-not-exist-xyz.com', port=443): Failed to resolve 'this-host-does-not-exist-xyz.com' ([Errno 11001] getaddrinfo failed)"))
[2026-04-03 22:32:49] ERROR in lookup_product: HTTPError — 404 Not Found for product ID 999
[2026-04-03 22:40:23] ERROR in fetch_products: ConnectionError — HTTPSConnectionPool(host='this-host-does-not-exist-xyz.com', port=443): Max retries exceeded with url: /api (Caused by NameResolutionError("HTTPSConnection(host='this-host-does-not-exist-xyz.com', port=443): Failed to resolve 'this-host-does-not-exist-xyz.com' ([Errno 11001] getaddrinfo failed)"))
[2026-04-03 22:40:29] ERROR in lookup_product: Timeout — Request took too long
[2026-04-03 22:42:09] ERROR in fetch_products: ConnectionError — HTTPSConnectionPool(host='this-host-does-not-exist-xyz.com', port=443): Max retries exceeded with url: /api (Caused by NameResolutionError("HTTPSConnection(host='this-host-does-not-exist-xyz.com', port=443): Failed to resolve 'this-host-does-not-exist-xyz.com' ([Errno 11001] getaddrinfo failed)"))
[2026-04-03 22:42:11] ERROR in lookup_product: HTTPError — 404 Not Found for product ID 999
[2026-04-03 22:42:45] ERROR in fetch_products: ConnectionError — HTTPSConnectionPool(host='this-host-does-not-exist-xyz.com', port=443): Max retries exceeded with url: /api (Caused by NameResolutionError("HTTPSConnection(host='this-host-does-not-exist-xyz.com', port=443): Failed to resolve 'this-host-does-not-exist-xyz.com' ([Errno 11001] getaddrinfo failed)"))
[2026-04-03 22:42:46] ERROR in lookup_product: HTTPError — 404 Not Found for product ID 999

 *  Terminal will be reused by tasks, press any key to close it. 
