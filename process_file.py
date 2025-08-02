import pandas as pd
import io

def process_file(file_content):
    try:
        # Read the CSV file from the uploaded content
        df = pd.read_csv(io.BytesIO(file_content))
        # Return the first 5 rows as a string
        result = df.head().to_string()
        return {"output": result, "status": "success"}
    except Exception as e:
        return {"output": f"Error: {str(e)}", "status": "error"}