# Task 1 — File Read & Write Basics


# -------- Part A: Write --------

# Writing initial content
with open("python_notes.txt", "w", encoding="utf-8") as file:
    file.write("Topic 1: Variables store data. Python is dynamically typed.\n")
    file.write("Topic 2: Lists are ordered and mutable.\n")
    file.write("Topic 3: Dictionaries store key-value pairs.\n")
    file.write("Topic 4: Loops automate repetitive tasks.\n")
    file.write("Topic 5: Exception handling prevents crashes.\n")

print("✅ File written successfully.")

# Appending additional lines
with open("python_notes.txt", "a", encoding="utf-8") as file:
    file.write("Topic 6: Functions help reuse code.\n")
    file.write("Topic 7: Modules help organize code.\n")

print("✅ Lines appended successfully.")


# -------- Part B: Read --------

print("\n--- Reading File ---")

with open("python_notes.txt", "r", encoding="utf-8") as file:
    lines = file.readlines()

# Print numbered lines
for i, line in enumerate(lines, start=1):
    print(f"{i}. {line.strip()}")

# Count total lines
print(f"\nTotal number of lines: {len(lines)}")

# Keyword search
keyword = input("\nEnter keyword to search: ").lower()

found = False

print("\nSearch Results:")
for line in lines:
    if keyword in line.lower():
        print(line.strip())
        found = True

if not found:
    print("No matching lines found.")



# Task 2 — API Integration

import requests

BASE_URL = "https://dummyjson.com/products"

# =========================
# Step 1 — Fetch Products
# =========================

print("\n--- Fetching Products ---")

try:
    response = requests.get(f"{BASE_URL}?limit=20")
    response.raise_for_status()  # raises error if request fails

    data = response.json()
    products = data["products"]

    # Print table header
    print(f"{'ID':<4} | {'Title':<30} | {'Category':<15} | {'Price':<8} | {'Rating'}")
    print("-" * 75)

    for p in products:
        print(f"{p['id']:<4} | {p['title']:<30} | {p['category']:<15} | ${p['price']:<7} | {p['rating']}")

except Exception as e:
    print("❌ Error fetching products:", e)


# =========================
# Step 2 — Filter & Sort
# =========================

print("\n--- Filtered Products (Rating ≥ 4.5, Sorted by Price Desc) ---")

try:
    filtered = [p for p in products if p["rating"] >= 4.5]
    sorted_products = sorted(filtered, key=lambda x: x["price"], reverse=True)

    for p in sorted_products:
        print(f"{p['title']} | ${p['price']} | Rating: {p['rating']}")

except Exception as e:
    print("❌ Error in filtering/sorting:", e)


# =========================
# Step 3 — Search by Category
# =========================

print("\n--- Laptops Category ---")

try:
    response = requests.get(f"{BASE_URL}/category/laptops")
    response.raise_for_status()

    laptops = response.json()["products"]

    for p in laptops:
        print(f"{p['title']} — ${p['price']}")

except Exception as e:
    print("❌ Error fetching laptops:", e)


# =========================
# Step 4 — POST Request
# =========================

print("\n--- Creating New Product (Simulated) ---")

new_product = {
    "title": "My Custom Product",
    "price": 999,
    "category": "electronics",
    "description": "A product I created via API"
}

try:
    response = requests.post(f"{BASE_URL}/add", json=new_product)
    response.raise_for_status()

    print("Response from server:")
    print(response.json())

except Exception as e:
    print("❌ Error in POST request:", e)


# Task 3 - Execution Handling

# Part A — Guarded Calculator

def safe_divide(a, b):
    try:
        return a / b
    except ZeroDivisionError:
        return "Error: Cannot divide by zero"
    except TypeError:
        return "Error: Invalid input types"

# Test cases
print("\n--- Safe Divide Tests ---")
print(safe_divide(10, 2))
print(safe_divide(10, 0))
print(safe_divide("ten", 2))

# =========================
# Part B — Guarded File Reader
# =========================

def read_file_safe(filename):
    try:
        with open(filename, "r", encoding="utf-8") as f:
            content = f.read()
            return content
    except FileNotFoundError:
        print(f"Error: File '{filename}' not found.")
    finally:
        print("File operation attempt complete.")

# Test cases
print("\n--- File Read Test (Valid) ---")
print(read_file_safe("python_notes.txt"))

print("\n--- File Read Test (Invalid) ---")
print(read_file_safe("ghost_file.txt"))

import requests

print("\n--- Robust API Call ---")

try:
    response = requests.get("https://dummyjson.com/products?limit=5", timeout=5)
    response.raise_for_status()
    
    data = response.json()
    for p in data["products"]:
        print(p["title"])

except requests.exceptions.ConnectionError:
    print("Connection failed. Please check your internet.")

except requests.exceptions.Timeout:
    print("Request timed out. Try again later.")

except Exception as e:
    print("Error:", e)

# =========================
# Part D — Input Validation Loop
# =========================

print("\n--- Product Lookup ---")

while True:
    user_input = input("\nEnter a product ID (1–100) or 'quit': ")
    
    if user_input.lower() == "quit":
        print("Exiting...")
        break

    # Validate integer
    if not user_input.isdigit():
        print("⚠ Invalid input. Please enter a number.")
        continue

    product_id = int(user_input)

    # Validate range
    if not (1 <= product_id <= 100):
        print("⚠ ID must be between 1 and 100.")
        continue

    # API call
    try:
        url = f"https://dummyjson.com/products/{product_id}"
        response = requests.get(url, timeout=5)

        if response.status_code == 404:
            print("Product not found.")
        elif response.status_code == 200:
            product = response.json()
            print(f"{product['title']} — ${product['price']}")
        else:
            print("Unexpected response:", response.status_code)

    except requests.exceptions.ConnectionError:
        print("Connection failed. Please check your internet.")

    except requests.exceptions.Timeout:
        print("Request timed out. Try again later.")

    except Exception as e:
        print("Error:", e)

    

# Task 4 — Logging to File


import requests
from datetime import datetime

LOG_FILE = "error_log.txt"

# Logger function
def log_error(function_name, error_type, message):
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    
    log_entry = f"[{timestamp}] ERROR in {function_name}: {error_type} — {message}\n"
    
    with open(LOG_FILE, "a", encoding="utf-8") as f:
        f.write(log_entry)


# =========================
# 1. Trigger ConnectionError
# =========================

print("\n--- Testing Connection Error ---")

try:
    response = requests.get("https://this-host-does-not-exist-xyz.com/api", timeout=5)

except requests.exceptions.ConnectionError as e:
    print("Connection failed (expected). Logging error...")
    log_error("fetch_products", "ConnectionError", str(e))


# =========================
# 2. Trigger HTTP Error (404)
# =========================

print("\n--- Testing HTTP Error (404) ---")

try:
    product_id = 999
    url = f"https://dummyjson.com/products/{product_id}"
    
    response = requests.get(url, timeout=5)
    
    if response.status_code != 200:
        message = f"{response.status_code} Not Found for product ID {product_id}"
        print("HTTP error detected. Logging error...")
        log_error("lookup_product", "HTTPError", message)

except requests.exceptions.ConnectionError:
    print("Connection failed.")
    log_error("lookup_product", "ConnectionError", "Failed to connect")

except requests.exceptions.Timeout:
    print("Request timed out.")
    log_error("lookup_product", "Timeout", "Request took too long")

except Exception as e:
    print("Unexpected error:", e)
    log_error("lookup_product", "Exception", str(e))


# =========================
# 3. Display Log File
# =========================

print("\n--- Error Log Contents ---")

try:
    with open(LOG_FILE, "r", encoding="utf-8") as f:
        print(f.read())

except FileNotFoundError:
    print("No log file found.")