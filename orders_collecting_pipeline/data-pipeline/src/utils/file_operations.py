def write_to_csv(file_path, data):
    import pandas as pd

    df = pd.DataFrame(data)
    df.to_csv(file_path, mode='a', header=False, index=False)

def read_from_csv(file_path):
    import pandas as pd

    return pd.read_csv(file_path)

def write_to_excel(data_dict):
    import datetime
    import pandas as pd
    current_date = datetime.now().strftime("%Y-%m-%d")
    # Define the xlsx file path
    excel_file_path = 'D:/Fuego Blouse CO/fashion-data-pipeline/data/orders.xlsx'
    # Convert the order data to a DataFrame
    df = pd.DataFrame([data_dict])
    stats = data_dict.keys()
    # Append the data to the Excel file
    try:
        with pd.ExcelWriter(excel_file_path, engine='openpyxl', mode='a', if_sheet_exists='overlay') as writer:
            df.to_excel(writer, sheet_name=current_date, index=False, header=False, startrow=writer.sheets[current_date].max_row)
    except FileNotFoundError:
        with pd.ExcelWriter(excel_file_path, engine='openpyxl') as writer:
            df.to_excel(writer, sheet_name=current_date, index=False)
