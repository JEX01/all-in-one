# Import required libraries
import pandas as pd
import numpy as np
# from google.colab import files

# Upload the dataset
# uploaded = files.upload()
# file_name = list(uploaded.keys())[0]
file_name = str(input("enter path to file"))
df = pd.read_csv(file_name)

print("Dataset uploaded successfully!")
print(f"Shape: {df.shape}")

# Main cleaning loop
while True:
    print("\n" + "="*50)
    print("DATA CLEANING MENU")
    print("="*50)
    print("1. Dataset Overview")
    print("2. Handle Missing Values")
    print("3. Replace/Correct Values")
    print("4. Change Column Types")
    print("5. Clean String Columns")
    print("6. Remove Duplicates")
    print("7. Filtering/Conditional Cleaning")
    print("8. Rename Columns")
    print("9. Handle Outliers")
    print("10. Save Cleaned Dataset")
    print("11. HALF-print")
    print("12. FUll-print")
    print("13. Exit")

    choice = input("\nEnter your choice (1-11): ")

    # 1. Dataset Overview
    if choice == '1':
        print("\nDATASET OVERVIEW")
        print("="*30)

        print(f"\nFirst 5 rows:")
        print(df.head())

        print(f"\nLast 5 rows:")
        print(df.tail())

        print(f"\nDataset info:")
        print(df.info())

        print(f"\nSummary statistics:")
        print(df.describe(include='all'))

        print(f"\nShape: {df.shape}")
        print(f"\nColumns: {list(df.columns)}")
        print(f"\nData types:\n{df.dtypes}")

        print(f"\nMissing values:\n{df.isnull().sum()}")

        print(f"\nDuplicate rows: {df.duplicated().sum()}")

    # 2. Handle Missing Values
    elif choice == '2':
        print("\nHANDLE MISSING VALUES")
        print("="*30)

        print("Missing values per column:")
        null_counts = df.isnull().sum()
        for col, count in null_counts.items():
            if count > 0:
                print(f"{col}: {count} missing values")

        if null_counts.sum() == 0:
            print("No missing values found!")
            continue

        print("\nOptions:")
        print("1. Drop rows with missing values")
        print("2. Drop columns with missing values")
        print("3. Fill missing values")

        missing_choice = input("Enter your choice (1-3): ")

        if missing_choice == '1':
            threshold = input("Drop rows with how many missing values? (Enter 'all' or a number): ")
            if threshold.lower() == 'all':
                df.dropna(inplace=True)
                print("Dropped all rows with any missing values")
            else:
                try:
                    thresh_val = len(df.columns) - int(threshold)
                    df.dropna(thresh=thresh_val, inplace=True)
                    print(f"Dropped rows with more than {threshold} missing values")
                except:
                    print("Invalid input. Using default: drop all rows with any missing values")
                    df.dropna(inplace=True)

        elif missing_choice == '2':
            threshold = input("Drop columns with what percentage of missing values? (0-100): ")
            try:
                threshold = float(threshold)
                if 0 <= threshold <= 100:
                    # Calculate percentage of missing values for each column
                    missing_percentage = (df.isnull().sum() / len(df)) * 100
                    cols_to_drop = missing_percentage[missing_percentage > threshold].index
                    df.drop(columns=cols_to_drop, inplace=True)
                    print(f"Dropped columns with more than {threshold}% missing values: {list(cols_to_drop)}")
                else:
                    print("Invalid percentage. Must be between 0 and 100.")
            except:
                print("Invalid input. Please enter a number.")

        elif missing_choice == '3':
            col_to_fill = input("Enter column name to fill (or 'all' for all columns): ")

            if col_to_fill.lower() == 'all':
                print("\nFill options:")
                print("1. Fill with mean (numeric columns only)")
                print("2. Fill with median (numeric columns only)")
                print("3. Fill with mode (most frequent value)")
                print("4. Fill with specific value")
                print("5. Fill with forward fill")
                print("6. Fill with backward fill")

                fill_method = input("Choose fill method (1-6): ")

                for col in df.columns:
                    if df[col].isnull().sum() > 0:
                        if fill_method == '1' and df[col].dtype in ['int64', 'float64']:
                            df[col].fillna(df[col].mean(), inplace=True)
                            print(f"Filled {col} with mean: {df[col].mean()}")
                        elif fill_method == '2' and df[col].dtype in ['int64', 'float64']:
                            df[col].fillna(df[col].median(), inplace=True)
                            print(f"Filled {col} with median: {df[col].median()}")
                        elif fill_method == '3':
                            df[col].fillna(df[col].mode()[0], inplace=True)
                            print(f"Filled {col} with mode: {df[col].mode()[0]}")
                        elif fill_method == '4':
                            fill_val = input(f"Enter value to fill for {col}: ")
                            try:
                                # Try to convert to appropriate type
                                if df[col].dtype == 'int64':
                                    fill_val = int(fill_val)
                                elif df[col].dtype == 'float64':
                                    fill_val = float(fill_val)
                            except:
                                pass  # Keep as string if conversion fails
                            df[col].fillna(fill_val, inplace=True)
                            print(f"Filled {col} with value: {fill_val}")
                        elif fill_method == '5':
                            df[col].fillna(method='ffill', inplace=True)
                            print(f"Filled {col} with forward fill")
                        elif fill_method == '6':
                            df[col].fillna(method='bfill', inplace=True)
                            print(f"Filled {col} with backward fill")
            else:
                if col_to_fill in df.columns:
                    print("\nFill options:")
                    print("1. Fill with mean")
                    print("2. Fill with median")
                    print("3. Fill with mode (most frequent value)")
                    print("4. Fill with specific value")
                    print("5. Fill with forward fill")
                    print("6. Fill with backward fill")

                    fill_method = input("Choose fill method (1-6): ")

                    if fill_method == '1' and df[col_to_fill].dtype in ['int64', 'float64']:
                        df[col_to_fill].fillna(df[col_to_fill].mean(), inplace=True)
                        print(f"Filled {col_to_fill} with mean: {df[col_to_fill].mean()}")
                    elif fill_method == '2' and df[col_to_fill].dtype in ['int64', 'float64']:
                        df[col_to_fill].fillna(df[col_to_fill].median(), inplace=True)
                        print(f"Filled {col_to_fill} with median: {df[col_to_fill].median()}")
                    elif fill_method == '3':
                        df[col_to_fill].fillna(df[col_to_fill].mode()[0], inplace=True)
                        print(f"Filled {col_to_fill} with mode: {df[col_to_fill].mode()[0]}")
                    elif fill_method == '4':
                        fill_val = input(f"Enter value to fill for {col_to_fill}: ")
                        try:
                            # Try to convert to appropriate type
                            if df[col_to_fill].dtype == 'int64':
                                fill_val = int(fill_val)
                            elif df[col_to_fill].dtype == 'float64':
                                fill_val = float(fill_val)
                        except:
                            pass  # Keep as string if conversion fails
                        df[col_to_fill].fillna(fill_val, inplace=True)
                        print(f"Filled {col_to_fill} with value: {fill_val}")
                    elif fill_method == '5':
                        df[col_to_fill].fillna(method='ffill', inplace=True)
                        print(f"Filled {col_to_fill} with forward fill")
                    elif fill_method == '6':
                        df[col_to_fill].fillna(method='bfill', inplace=True)
                        print(f"Filled {col_to_fill} with backward fill")
                else:
                    print(f"Column '{col_to_fill}' not found!")

    # 3. Replace/Correct Values
    elif choice == '3':
        print("\nREPLACE/CORRECT VALUES")
        print("="*30)

        col_to_replace = input("Enter column name: ")

        if col_to_replace in df.columns:
            print(f"Unique values in {col_to_replace}:")
            print(df[col_to_replace].unique())

            print("\nOptions:")
            print("1. Replace specific value")
            print("2. Replace multiple values")
            print("3. Replace using condition")

            replace_choice = input("Enter your choice (1-3): ")

            if replace_choice == '1':
                old_val = input("Enter value to replace: ")
                new_val = input("Enter new value: ")

                # Handle numeric conversion if needed
                try:
                    if df[col_to_replace].dtype == 'int64':
                        old_val = int(old_val)
                        new_val = int(new_val)
                    elif df[col_to_replace].dtype == 'float64':
                        old_val = float(old_val)
                        new_val = float(new_val)
                except:
                    pass

                df[col_to_replace].replace(old_val, new_val, inplace=True)
                print(f"Replaced {old_val} with {new_val} in {col_to_replace}")

            elif replace_choice == '2':
                print("Enter replacements as old1:new1,old2:new2,...")
                replacements = input("Enter replacements: ")

                try:
                    replace_dict = {}
                    for pair in replacements.split(','):
                        old, new = pair.split(':')
                        # Handle numeric conversion if needed
                        try:
                            if df[col_to_replace].dtype == 'int64':
                                old = int(old)
                                new = int(new)
                            elif df[col_to_replace].dtype == 'float64':
                                old = float(old)
                                new = float(new)
                        except:
                            pass
                        replace_dict[old] = new

                    df[col_to_replace].replace(replace_dict, inplace=True)
                    print(f"Replaced multiple values in {col_to_replace}")
                except:
                    print("Invalid format! Use old1:new1,old2:new2,...")

            elif replace_choice == '3':
                print("Condition examples:")
                print("- values < 10")
                print("- values > 100")
                print("- values == 'text'")
                print("- values contains 'abc'")

                condition = input("Enter condition: ")
                new_val = input("Enter new value: ")

                try:
                    # Handle numeric conversion if needed
                    try:
                        if df[col_to_replace].dtype in ['int64', 'float64']:
                            new_val = float(new_val)
                    except:
                        pass

                    # Parse condition
                    if condition.startswith("values < "):
                        threshold = float(condition.split(" < ")[1])
                        df.loc[df[col_to_replace] < threshold, col_to_replace] = new_val
                    elif condition.startswith("values > "):
                        threshold = float(condition.split(" > ")[1])
                        df.loc[df[col_to_replace] > threshold, col_to_replace] = new_val
                    elif condition.startswith("values == "):
                        match_val = condition.split(" == ")[1].strip("'\"")
                        df.loc[df[col_to_replace] == match_val, col_to_replace] = new_val
                    elif condition.startswith("values contains "):
                        substr = condition.split(" contains ")[1].strip("'\"")
                        df.loc[df[col_to_replace].str.contains(substr, na=False), col_to_replace] = new_val
                    else:
                        print("Unsupported condition format!")
                        continue

                    print(f"Applied conditional replacement to {col_to_replace}")
                except Exception as e:
                    print(f"Error applying condition: {e}")
        else:
            print(f"Column '{col_to_replace}' not found!")

    # 4. Change Column Types
    elif choice == '4':
        print("\nCHANGE COLUMN TYPES")
        print("="*30)

        col_to_convert = input("Enter column name: ")

        if col_to_convert in df.columns:
            print(f"Current type of {col_to_convert}: {df[col_to_convert].dtype}")

            print("\nOptions:")
            print("1. Convert to numeric")
            print("2. Convert to string")
            print("3. Convert to integer")
            print("4. Convert to float")
            print("5. Convert to datetime")
            print("6. Convert to category")

            convert_choice = input("Enter your choice (1-6): ")

            try:
                if convert_choice == '1':
                    df[col_to_convert] = pd.to_numeric(df[col_to_convert], errors='coerce')
                    print(f"Converted {col_to_convert} to numeric")
                elif convert_choice == '2':
                    df[col_to_convert] = df[col_to_convert].astype(str)
                    print(f"Converted {col_to_convert} to string")
                elif convert_choice == '3':
                    df[col_to_convert] = pd.to_numeric(df[col_to_convert], errors='coerce').astype('Int64')
                    print(f"Converted {col_to_convert} to integer")
                elif convert_choice == '4':
                    df[col_to_convert] = df[col_to_convert].astype(float)
                    print(f"Converted {col_to_convert} to float")
                elif convert_choice == '5':
                    df[col_to_convert] = pd.to_datetime(df[col_to_convert], errors='coerce')
                    print(f"Converted {col_to_convert} to datetime")
                elif convert_choice == '6':
                    df[col_to_convert] = df[col_to_convert].astype('category')
                    print(f"Converted {col_to_convert} to category")
            except Exception as e:
                print(f"Error converting column: {e}")
        else:
            print(f"Column '{col_to_convert}' not found!")

    # 5. Clean String Columns
    elif choice == '5':
        print("\nCLEAN STRING COLUMNS")
        print("="*30)

        col_to_clean = input("Enter column name (or 'all' for all string columns): ")

        if col_to_clean.lower() == 'all':
            string_cols = df.select_dtypes(include=['object']).columns
            for col in string_cols:
                df[col] = df[col].str.strip()
                print(f"Stripped whitespace from {col}")
        elif col_to_clean in df.columns:
            if df[col_to_clean].dtype == 'object':
                print("\nString cleaning options:")
                print("1. Strip whitespace")
                print("2. Convert to lowercase")
                print("3. Convert to uppercase")
                print("4. Remove special characters")
                print("5. Custom character replacement")

                clean_choice = input("Enter your choice (1-5): ")

                if clean_choice == '1':
                    df[col_to_clean] = df[col_to_clean].str.strip()
                    print(f"Stripped whitespace from {col_to_clean}")
                elif clean_choice == '2':
                    df[col_to_clean] = df[col_to_clean].str.lower()
                    print(f"Converted {col_to_clean} to lowercase")
                elif clean_choice == '3':
                    df[col_to_clean] = df[col_to_clean].str.upper()
                    print(f"Converted {col_to_clean} to uppercase")
                elif clean_choice == '4':
                    df[col_to_clean] = df[col_to_clean].str.replace('[^a-zA-Z0-9 ]', '', regex=True)
                    print(f"Removed special characters from {col_to_clean}")
                elif clean_choice == '5':
                    chars_to_replace = input("Enter characters to replace: ")
                    replacement = input("Enter replacement: ")
                    df[col_to_clean] = df[col_to_clean].str.replace(chars_to_replace, replacement)
                    print(f"Replaced '{chars_to_replace}' with '{replacement}' in {col_to_clean}")
            else:
                print(f"Column '{col_to_clean}' is not a string column!")
        else:
            print(f"Column '{col_to_clean}' not found!")

    # 6. Remove Duplicates
    elif choice == '6':
        print("\nREMOVE DUPLICATES")
        print("="*30)

        print(f"Current duplicate rows: {df.duplicated().sum()}")

        if df.duplicated().sum() > 0:
            print("\nOptions:")
            print("1. Remove all duplicates")
            print("2. Remove duplicates based on specific columns")

            duplicate_choice = input("Enter your choice (1-2): ")

            if duplicate_choice == '1':
                df.drop_duplicates(inplace=True)
                print("Removed all duplicate rows")
            elif duplicate_choice == '2':
                columns = input("Enter column names (comma-separated): ").split(',')
                columns = [col.strip() for col in columns]

                # Validate columns
                invalid_cols = [col for col in columns if col not in df.columns]
                if invalid_cols:
                    print(f"Invalid columns: {invalid_cols}")
                else:
                    df.drop_duplicates(subset=columns, inplace=True)
                    print(f"Removed duplicates based on columns: {columns}")
        else:
            print("No duplicate rows found!")

    # 7. Filtering/Conditional Cleaning
    elif choice == '7':
        print("\nFILTERING/CONDITIONAL CLEANING")
        print("="*30)

        print("Options:")
        print("1. Filter rows based on condition")
        print("2. Remove rows based on condition")

        filter_choice = input("Enter your choice (1-2): ")

        if filter_choice == '1':
            column = input("Enter column name: ")
            if column in df.columns:
                print("Condition examples:")
                print("- values < 10")
                print("- values > 100")
                print("- values == 'text'")
                print("- values contains 'abc'")

                condition = input("Enter condition: ")

                try:
                    # Parse condition
                    if condition.startswith("values < "):
                        threshold = float(condition.split(" < ")[1])
                        filtered_df = df[df[column] < threshold]
                    elif condition.startswith("values > "):
                        threshold = float(condition.split(" > ")[1])
                        filtered_df = df[df[column] > threshold]
                    elif condition.startswith("values == "):
                        match_val = condition.split(" == ")[1].strip("'\"")
                        filtered_df = df[df[column] == match_val]
                    elif condition.startswith("values contains "):
                        substr = condition.split(" contains ")[1].strip("'\"")
                        filtered_df = df[df[column].str.contains(substr, na=False)]
                    else:
                        print("Unsupported condition format!")
                        continue

                    print(f"Filtered dataset shape: {filtered_df.shape}")
                    print("First 5 rows of filtered data:")
                    print(filtered_df.head())

                    replace_original = input("Replace original dataset with filtered data? (y/n): ")
                    if replace_original.lower() == 'y':
                        df = filtered_df
                        print("Dataset replaced with filtered data")
                except Exception as e:
                    print(f"Error applying filter: {e}")
            else:
                print(f"Column '{column}' not found!")

        elif filter_choice == '2':
            column = input("Enter column name: ")
            if column in df.columns:
                print("Condition examples:")
                print("- values < 10")
                print("- values > 100")
                print("- values == 'text'")
                print("- values contains 'abc'")

                condition = input("Enter condition: ")

                try:
                    # Parse condition
                    if condition.startswith("values < "):
                        threshold = float(condition.split(" < ")[1])
                        df = df[~(df[column] < threshold)]
                    elif condition.startswith("values > "):
                        threshold = float(condition.split(" > ")[1])
                        df = df[~(df[column] > threshold)]
                    elif condition.startswith("values == "):
                        match_val = condition.split(" == ")[1].strip("'\"")
                        df = df[~(df[column] == match_val)]
                    elif condition.startswith("values contains "):
                        substr = condition.split(" contains ")[1].strip("'\"")
                        df = df[~df[column].str.contains(substr, na=False)]
                    else:
                        print("Unsupported condition format!")
                        continue

                    print("Rows matching condition removed from dataset")
                except Exception as e:
                    print(f"Error applying filter: {e}")
            else:
                print(f"Column '{column}' not found!")

    # 8. Rename Columns
    elif choice == '8':
        print("\nRENAME COLUMNS")
        print("="*30)

        print("Current column names:")
        for i, col in enumerate(df.columns):
            print(f"{i+1}. {col}")

        print("\nOptions:")
        print("1. Rename specific column")
        print("2. Rename all columns")
        print("3. Strip whitespace from column names")

        rename_choice = input("Enter your choice (1-3): ")

        if rename_choice == '1':
            old_name = input("Enter current column name: ")
            if old_name in df.columns:
                new_name = input("Enter new column name: ")
                df.rename(columns={old_name: new_name}, inplace=True)
                print(f"Renamed '{old_name}' to '{new_name}'")
            else:
                print(f"Column '{old_name}' not found!")

        elif rename_choice == '2':
            new_names = input("Enter new column names (comma-separated): ").split(',')
            new_names = [name.strip() for name in new_names]

            if len(new_names) == len(df.columns):
                df.columns = new_names
                print("All columns renamed")
            else:
                print(f"Number of new names ({len(new_names)}) doesn't match number of columns ({len(df.columns)})")

        elif rename_choice == '3':
            df.columns = df.columns.str.strip()
            print("Stripped whitespace from all column names")

    # 9. Handle Outliers
    elif choice == '9':
        print("\nHANDLE OUTLIERS")
        print("="*30)

        numeric_cols = df.select_dtypes(include=[np.number]).columns
        if len(numeric_cols) == 0:
            print("No numeric columns found!")
            continue

        print("Numeric columns:")
        for i, col in enumerate(numeric_cols):
            print(f"{i+1}. {col}")

        col_to_process = input("Enter column name: ")

        if col_to_process in numeric_cols:
            print(f"Summary statistics for {col_to_process}:")
            print(df[col_to_process].describe())

            print("\nOutlier handling options:")
            print("1. Cap outliers using IQR method")
            print("2. Cap outliers using standard deviation method")
            print("3. Remove rows with outliers")

            outlier_choice = input("Enter your choice (1-3): ")

            if outlier_choice == '1':
                # IQR method
                Q1 = df[col_to_process].quantile(0.25)
                Q3 = df[col_to_process].quantile(0.75)
                IQR = Q3 - Q1
                lower_bound = Q1 - 1.5 * IQR
                upper_bound = Q3 + 1.5 * IQR

                print(f"IQR: {IQR}")
                print(f"Lower bound: {lower_bound}")
                print(f"Upper bound: {upper_bound}")

                outliers_count = ((df[col_to_process] < lower_bound) | (df[col_to_process] > upper_bound)).sum()
                print(f"Number of outliers: {outliers_count}")

                if outliers_count > 0:
                    df[col_to_process] = np.where(df[col_to_process] < lower_bound, lower_bound, df[col_to_process])
                    df[col_to_process] = np.where(df[col_to_process] > upper_bound, upper_bound, df[col_to_process])
                    print(f"Capped {outliers_count} outliers in {col_to_process}")
                else:
                    print("No outliers found using IQR method")

            elif outlier_choice == '2':
                # Standard deviation method
                mean = df[col_to_process].mean()
                std = df[col_to_process].std()
                lower_bound = mean - 3 * std
                upper_bound = mean + 3 * std

                print(f"Mean: {mean}")
                print(f"Standard deviation: {std}")
                print(f"Lower bound: {lower_bound}")
                print(f"Upper bound: {upper_bound}")

                outliers_count = ((df[col_to_process] < lower_bound) | (df[col_to_process] > upper_bound)).sum()
                print(f"Number of outliers: {outliers_count}")

                if outliers_count > 0:
                    df[col_to_process] = np.where(df[col_to_process] < lower_bound, lower_bound, df[col_to_process])
                    df[col_to_process] = np.where(df[col_to_process] > upper_bound, upper_bound, df[col_to_process])
                    print(f"Capped {outliers_count} outliers in {col_to_process}")
                else:
                    print("No outliers found using standard deviation method")

            elif outlier_choice == '3':
                # Remove outliers using IQR method
                Q1 = df[col_to_process].quantile(0.25)
                Q3 = df[col_to_process].quantile(0.75)
                IQR = Q3 - Q1
                lower_bound = Q1 - 1.5 * IQR
                upper_bound = Q3 + 1.5 * IQR

                original_size = len(df)
                df = df[(df[col_to_process] >= lower_bound) & (df[col_to_process] <= upper_bound)]
                new_size = len(df)

                print(f"Removed {original_size - new_size} rows with outliers from {col_to_process}")
        else:
            print(f"Column '{col_to_process}' is not numeric or doesn't exist!")

    # 10. Save Cleaned Dataset
    elif choice == '10':
        print("\nSAVE CLEANED DATASET")
        print("="*30)

        output_name = input("Enter output file name (without extension): ")
        if not output_name:
            output_name = "cleaned_data"

        folder_path = r"C:\Users\coccl\Desktop\ai-ml related stuff\dataset"

        print("Options:")
        print("1. CSV format")
        print("2. Excel format")

        format_choice = input("Enter your choice (1-2): ")

        if format_choice == '1':
            file_path = f"{folder_path}\\{output_name}.csv"
            df.to_csv(file_path, index=False)
            print(f"Dataset saved as {file_path}")
        elif format_choice == '2':
            file_path = f"{folder_path}\\{output_name}.xlsx"
            df.to_excel(file_path, index=False)
            print(f"Dataset saved as {file_path}")
        else:
            print("Invalid choice. Dataset not saved.")

    #11  hALF-Print
    elif choice == '11':
         print(df)

    # 12 Full-print
    elif choice == '12':
        chunk_size = 100
        for i in range(0, len(df), chunk_size):
            print(df.iloc[i:i+chunk_size])

    # 13. Exit
    elif choice == '13':
        print("Exiting data cleaning tool. Goodbye!")
        break

    else:
        print("Invalid choice! Please enter a number between 1 and 11.")