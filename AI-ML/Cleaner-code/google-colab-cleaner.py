import pandas as pd
import numpy as np
import os

# =========================
# Load Dataset
# =========================
file_name = input("Enter full path to CSV file: ").strip()
while not os.path.exists(file_name):
    print("❌ File not found. Try again.")
    file_name = input("Enter full path to CSV file: ").strip()

df = pd.read_csv(file_name)
print("\n✅ Dataset loaded successfully!")
print(f"Shape: {df.shape}")

# =========================
# Main Menu Loop
# =========================
while True:
    print("\n" + "="*60)
    print("🧹 DATA CLEANING MENU")
    print("="*60)
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
    print("11. Print Half Dataset")
    print("12. Print Full Dataset")
    print("13. Exit")
    choice = input("\nEnter choice (1-13): ").strip()

    # 1️⃣ Overview
    if choice == '1':
        print("\nDATASET OVERVIEW")
        print("-"*40)
        print("\nFirst 5 rows:\n", df.head())
        print("\nLast 5 rows:\n", df.tail())
        print("\nInfo:")
        print(df.info())
        print("\nSummary Statistics:\n", df.describe(include='all'))
        print("\nShape:", df.shape)
        print("Columns:", list(df.columns))
        print("\nMissing values:\n", df.isnull().sum())
        print("Duplicate rows:", df.duplicated().sum())

    # 2️⃣ Handle Missing Values
    elif choice == '2':
        print("\nHANDLE MISSING VALUES")
        print("-"*40)
        print("Missing values per column:\n", df.isnull().sum())
        print("\nOptions:")
        print("1. Drop rows with missing values")
        print("2. Drop columns with missing values")
        print("3. Fill missing values")
        sub = input("Choice (1-3): ").strip()

        if sub == '1':
            df.dropna(inplace=True)
            print("✅ Dropped all rows with any missing values.")
        elif sub == '2':
            thresh = float(input("Drop columns with >X% missing (0-100): "))
            perc = (df.isnull().sum()/len(df))*100
            drop_cols = perc[perc > thresh].index
            df.drop(columns=drop_cols, inplace=True)
            print(f"✅ Dropped columns: {list(drop_cols)}")
        elif sub == '3':
            col = input("Column name (or 'all'): ").strip()
            method = input("Fill with mean/median/mode/value? ").lower()
            if col.lower() == 'all':
                for c in df.columns:
                    if df[c].isnull().sum() > 0:
                        if method == 'mean' and pd.api.types.is_numeric_dtype(df[c]):
                            df[c].fillna(df[c].mean(), inplace=True)
                        elif method == 'median' and pd.api.types.is_numeric_dtype(df[c]):
                            df[c].fillna(df[c].median(), inplace=True)
                        elif method == 'mode':
                            df[c].fillna(df[c].mode()[0], inplace=True)
                        else:
                            val = input(f"Value for {c}: ")
                            df[c].fillna(val, inplace=True)
                print("✅ Missing values filled.")
            else:
                if method == 'mean' and pd.api.types.is_numeric_dtype(df[col]):
                    df[col].fillna(df[col].mean(), inplace=True)
                elif method == 'median' and pd.api.types.is_numeric_dtype(df[col]):
                    df[col].fillna(df[col].median(), inplace=True)
                elif method == 'mode':
                    df[col].fillna(df[col].mode()[0], inplace=True)
                else:
                    val = input("Enter fill value: ")
                    df[col].fillna(val, inplace=True)
                print(f"✅ Filled missing in {col}.")

    # 3️⃣ Replace/Correct
    elif choice == '3':
        col = input("Column to replace in: ").strip()
        if col in df.columns:
            print("Unique values:", df[col].unique())
            old = input("Value to replace: ")
            new = input("New value: ")
            df[col].replace(old, new, inplace=True)
            print(f"✅ Replaced {old} → {new}")
        else:
            print("❌ Column not found.")

    # 4️⃣ Change Column Types
    elif choice == '4':
        col = input("Column name: ")
        if col in df.columns:
            print("Current type:", df[col].dtype)
            print("Options: numeric, int, float, string, datetime, category")
            t = input("Convert to: ").lower()
            try:
                if t == "numeric":
                    df[col] = pd.to_numeric(df[col], errors='coerce')
                elif t == "int":
                    df[col] = pd.to_numeric(df[col], errors='coerce').astype("Int64")
                elif t == "float":
                    df[col] = df[col].astype(float)
                elif t == "string":
                    df[col] = df[col].astype(str)
                elif t == "datetime":
                    df[col] = pd.to_datetime(df[col], errors='coerce')
                elif t == "category":
                    df[col] = df[col].astype("category")
                print("✅ Converted successfully.")
            except Exception as e:
                print("❌ Error:", e)

    # 5️⃣ Clean String Columns
    elif choice == '5':
        col = input("Column name (or 'all'): ").strip()
        def clean_str(c):
            df[c] = df[c].str.strip().str.replace(r'[^a-zA-Z0-9 ]', '', regex=True)
            print(f"✅ Cleaned {c}")
        if col.lower() == 'all':
            for c in df.select_dtypes(include='object').columns:
                clean_str(c)
        elif col in df.columns:
            clean_str(col)

    # 6️⃣ Remove Duplicates
    elif choice == '6':
        before = len(df)
        df.drop_duplicates(inplace=True)
        print(f"✅ Removed {before - len(df)} duplicate rows.")

    # 7️⃣ Filtering
    elif choice == '7':
        col = input("Column name: ")
        if col in df.columns:
            condition = input("Filter condition (e.g. >50, ==yes): ").strip()
            try:
                filtered = df.query(f"`{col}` {condition}")
                print(f"Filtered shape: {filtered.shape}")
                if input("Replace original? (y/n): ").lower() == 'y':
                    df = filtered
                    print("✅ Replaced dataset.")
            except Exception as e:
                print("❌ Error:", e)

    # 8️⃣ Rename Columns
    elif choice == '8':
        print("Current:", list(df.columns))
        old = input("Old column name: ")
        new = input("New column name: ")
        if old in df.columns:
            df.rename(columns={old:new}, inplace=True)
            print(f"✅ Renamed {old} → {new}")

    # 9️⃣ Handle Outliers (IQR cap)
    elif choice == '9':
        num_cols = df.select_dtypes(include=np.number).columns
        print("Numeric columns:", list(num_cols))
        col = input("Column to process: ")
        if col in num_cols:
            Q1, Q3 = df[col].quantile(0.25), df[col].quantile(0.75)
            IQR = Q3 - Q1
            low, high = Q1 - 1.5*IQR, Q3 + 1.5*IQR
            before = df[col].copy()
            df[col] = np.where(df[col] < low, low, np.where(df[col] > high, high, df[col]))
            print(f"✅ Capped outliers in {col}.")

    # 🔟 Save
    elif choice == '10':
        out = input("Output file name (without extension): ").strip() or "cleaned_data"
        fmt = input("Save as csv or xlsx? ").lower()
        if fmt == 'csv':
            df.to_csv(out + ".csv", index=False)
            print(f"✅ Saved as {out}.csv")
        else:
            df.to_excel(out + ".xlsx", index=False)
            print(f"✅ Saved as {out}.xlsx")

    # 1️⃣1 Half Print
    elif choice == '11':
        print(df.head(len(df)//2))

    # 1️⃣2 Full Print
    elif choice == '12':
        print(df)

    # 1️⃣3 Exit
    elif choice == '13':
        print("👋 Exiting. Goodbye!")
        break

    else:
        print("❌ Invalid choice.")
