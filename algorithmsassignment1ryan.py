#RYAN SARWAR 100825599 ALGORITHMS ASSINGMENT 1

import time
import timeit

#Function to reverse the dataset for worst-case scenario analysis
def reversed_dataset(dataset):
    return dataset[::-1]

product_data = [ #Sorted by: ID, Name, Price, Category
    (57353, "Camera SBBHC", 546.88, "Electronics"),
    (40374, "Smartphone ILGCU", 947.54, "Electronics"),
    (34863, "Biography XPESK", 287.31, "Books"),
    (18086, "Shirt ZQLTI", 439.07, "Clothing"),
    (16041, "Jacket OTBKQ", 986.73, "Clothing"),
    (43566, "Mystery COKPK", 836.57, "Books"),
    (69260, "Toaster FODKJ", 867.6, "Home & Kitchen"),
    (30895, "Knife Set KGFUF", 385.77, "Home & Kitchen"),
    (19897, "Blender DPKLR", 488.62, "Home & Kitchen"),
    (87296, "Skirt IRTZX", 261.08, "Clothing"),
    (68215, "Laptop QLBQC", 404.21, "Electronics"),
    (68097, "Camera SGSRZ", 36.39, "Electronics"),
    (26556, "Novel METLI", 376.45, "Books"),
    (30483, "Knife Set WRSZZ", 55.97, "Home & Kitchen"),
    (62422, "Camera VFQWS", 382.69, "Electronics"),
    (22806, "Smartwatch VVFNT", 203.55, "Electronics"),
    (24976, "Pants YZMAK", 449.56, "Clothing"),
    (30631, "Headphones JFGYQ", 115.08, "Electronics"),
    (27939, "Textbook TWQKZ", 108.5, "Books"),
    (41355, "Headphones JOUXM", 211.57, "Electronics"),
    (94162, "Laptop WRJOZ", 956.53, "Electronics"),
    (28710, "Dress FRSMO", 879.09, "Clothing"),
    (90291, "Pants TIPUD", 853.38, "Clothing"),
    (20368, "Shirt FQFPK", 83.19, "Clothing"),
    (68960, "Blender OMDPS", 720.06, "Home & Kitchen"),
    (40852, "Novel IRROY", 603.68, "Books"),
    (97895, "Blender KSJHL", 123.25, "Home & Kitchen"),
    (96314, "Cutting Board LUICX", 628.29, "Home & Kitchen"),
    (85719, "Laptop GZORF", 641.33, "Electronics"),
    (98625, "Mystery BOPTP", 160.68, "Books"),
    (66208, "Blender GCZSK", 161.83, "Home & Kitchen"),
    (86128, "Biography ASTVE", 90.44, "Books"),
    (10889, "Shirt DNRZU", 316.48, "Clothing"),
    (82777, "Shirt OZWXU", 790.46, "Clothing"),
    (43451, "Mixer CKVJQ", 379.5, "Home & Kitchen"),
    (12848, "Toaster VZXUE", 867.97, "Home & Kitchen"),
    (17646, "Biography BPWXR", 424.83, "Books"),
    (85197, "Cutting Board IJVPP", 986.89, "Home & Kitchen"),
    (13471, "Knife Set TPCMO", 831.9, "Home & Kitchen"),
    (66237, "Headphones LTPLK", 995.13, "Electronics"),
    (30251, "Pants HCBKI", 450.68, "Clothing"),
    (46944, "Smartwatch QNALX", 647.08, "Electronics"),
    (93533, "Novel WOHSN", 516.39, "Books"),
    (95090, "Cutting Board RBACL", 568.63, "Home & Kitchen"),
    (98827, "Shirt RSQGL", 231.54, "Clothing"),
    (64489, "Novel EFPYC", 502.61, "Books"),
    (39148, "Cutting Board OYHCV", 220.15, "Home & Kitchen"),
    (25425, "Mystery MGSPG", 783.17, "Books"),
    (69525, "Camera XROCD", 76.05, "Electronics"),
    (44574, "Knife Set ASRHX", 64.62, "Home & Kitchen")
]

#Convert tuples into dictionaries, also demonstrate the data load
print("Loading data...")

products = [{"ID": p[0], "Name": p[1], "Price": p[2], "Category": p[3]} for p in product_data]

print(f"Data loaded: {len(products)} products")

#Insert operation function
def insert_product(products, new_product):
    products.append(new_product)

#Update operation function
def update_product(products, product_id, new_data):
    for product in products:
        if product['ID'] == product_id:
            product.update(new_data)
            return product
    return None

#Deletion operation function
def delete_product(products, product_id):
    for i, product in enumerate(products):
        if product['ID'] == product_id:
            return products.pop(i)
    return None

#Search operation function
def search_product(products, search_key, search_value):
    return [product for product in products if product.get(search_key) == search_value]

#Quicksort algorithm construction
def quick_sort(arr, low, high):
    if low < high:
        pi = partition(arr, low, high)
        quick_sort(arr, low, pi - 1)
        quick_sort(arr, pi + 1, high)

def partition(arr, low, high):
    pivot = arr[high]['Price']
    i = low - 1
    for j in range(low, high):
        if arr[j]['Price'] < pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
    arr[i+1], arr[high] = arr[high], arr[i+1]
    return i + 1


#Using quicksort for products
quick_sort(products, 0, len(products) - 1)

#Average case analysis measurement 
start_perf_counter = time.perf_counter()
quick_sort(products, 0, len(products) - 1)
end_perf_counter = time.perf_counter()
print(f"Time taken to sort in average case scenario: {end_perf_counter - start_perf_counter:.6f} seconds")

#Best case analysis measurement
start_perf_counter = time.perf_counter()
quick_sort(products, 0, len(products) - 1)  # Assuming products are already sorted
end_perf_counter = time.perf_counter()
print(f"Time taken to sort already sorted data (Best case scenario): {end_perf_counter - start_perf_counter:.6f} seconds")

#reverses order of data for worst case analysis
products_reversed = reversed_dataset(products)

#Worst case analysis measurement
start_perf_counter = time.perf_counter()
quick_sort(products_reversed, 0, len(products_reversed) - 1)
end_perf_counter = time.perf_counter()
print(f"Time taken to sort data in reverse order (Worst case scenario): {end_perf_counter - start_perf_counter:.6f} seconds") #needed more decimal places to read the time for each analysis

#Insert operation demonstration
print("\nInserting a new product...")
insert_product(products, {"ID": 12345, "Name": "TEST PRODUCT", "Price": 150.45, "Category": "EXAMPLE"})
print("New product has been inserted. Total products:", len(products))

#Update operation demonstration
print("\nUpdating product...")
update_product(products, 12345, {"Price": 150.45})
print("Product updated. New details:", search_product(products, "ID", 12345))

#Delete operation demonstration
print("\nDeleting product...")
delete_product(products, 12345)
print("Product deleted. Total products:", len(products))

#Search operation demonstration
print("\nSearching for Electronics category...")
search_results = search_product(products, "Category", "Electronics")
print(f"Found {len(search_results)} products in Electronics.")

# Print all sorted products for verification
print("All products sorted by lowest to highest price: ")
for product in products[:50]:  
    print(product)
