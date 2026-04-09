# from PIL import Image
# import pytesseract
# import pandas as pd

# # Load the image
# # image_path = ""C:/Users/gc271/OneDrive/Pictures/Screenshots/Screenshot 2025-10-17 161703.png""
# image = Image.open(image_path)

# # Extract text using OCR
# text = pytesseract.image_to_string(image)

# # Split text into lines
# lines = [line.strip() for line in text.split("\n") if line.strip()]

# # Process data assuming consistent spacing
# data = []
# for line in lines[1:]:  # skip header line
#     parts = line.split()
#     if len(parts) >= 6:
#         date = parts[0]
#         category = parts[1]
#         sub_category = " ".join(parts[2:-3])
#         amount = parts[-3]
#         payment = parts[-2]
#         mode = parts[-1]
#         data.append([date, category, sub_category, amount, payment, mode])

# # Create dataframe
# columns = ["Date", "Category", "Sub-Category", "Amount", "Payment", "Mode"]
# df = pd.DataFrame(data, columns=columns)

# # Save to Excel
# excel_path = "/mnt/data/expenses_data.xlsx"
# df.to_excel(excel_path, index=False)

# excel_path

num=input("enter num: ")
c= num.count(num)
print(c)