import json
import re
import pandas as pd
from collections import defaultdict

# Load JSON data from file
def load_json(filename):
    with open(filename, "r", encoding="utf-8") as file:
        return json.load(file)

# Load CWE ID and names from CSV file
def load_cwe_list(filename):
    df = pd.read_csv(filename)
    df_reset = df.reset_index()
    df_reset.iloc[:, 0] = df_reset.iloc[:, 0].astype(str).copy()
    return {cwe_name.lower(): cwe_id for cwe_id, cwe_name in df_reset.iloc[:, :2].itertuples(index=False, name=None)}

# Extract CWE names and calculate frequencies
def analyze_cwe_frequencies(data):
    cwe_frequencies = defaultdict(lambda: {"cwe_name": "", "cwe_id": "", "success_frequency": 0, "failed_detected_frequency": 0, "total_frequency": 0})
    
    for obj in data:
        if "jailberak_task" in obj:
            task = obj["jailberak_task"]
            
            # Extract CWE name from the prompt
            if "example of" in task:
                cwe_name = task.split("example of")[-1].strip().lower()
                
                # Update frequencies
                cwe_frequencies[cwe_name]["cwe_name"] = cwe_name
                cwe_frequencies[cwe_name]["success_frequency"] += 1
                cwe_frequencies[cwe_name]["total_frequency"] += 1
    
    return cwe_frequencies

# Extract failed detected frequencies from reason_failed
def analyze_failed_frequencies(data, cwe_dict, cwe_frequencies):
    for obj in data:
        if "reason_failed" in obj:
            failed_text = obj["reason_failed"]
            
            # Extract CWE IDs from the failure reason
            cwe_ids = re.findall(r'\b\d+\b', failed_text)
            
            for cwe_id in cwe_ids:
                for cwe_name, mapped_id in cwe_dict.items():
                    if mapped_id == cwe_id:
                        
                        if cwe_name in cwe_frequencies:
                            cwe_frequencies[cwe_name]["failed_detected_frequency"] += 1
                            cwe_frequencies[cwe_name]["total_frequency"] += 1
                        else:
                            cwe_frequencies[cwe_name] = {"cwe_name": cwe_name, "cwe_id": cwe_id, "success_frequency": 0, "failed_detected_frequency": 1, "total_frequency": 1}
    
    return cwe_frequencies

# Save analysis result to a new JSON file
def save_json(data, filename):
    with open(filename, "w", encoding="utf-8") as file:
        json.dump(data, file, indent=4)

if __name__ == "__main__":
    success_input_filename = "success_library.json"
    failed_input_filename = "failure_library.json"
    output_filename = "frequency_analysis.json"
    cwe_csv_filename = "../cwe_software.csv"
    
    success_data = load_json(success_input_filename)
    failed_data = load_json(failed_input_filename)
    cwe_dict = load_cwe_list(cwe_csv_filename)
    
    cwe_frequencies = analyze_cwe_frequencies(success_data)
    cwe_frequencies = analyze_failed_frequencies(failed_data, cwe_dict, cwe_frequencies)
    
    # Assign CWE IDs to each entry
    for cwe_name in cwe_frequencies:
        if cwe_name in cwe_dict:
            cwe_frequencies[cwe_name]["cwe_id"] = cwe_dict[cwe_name]
    
    sorted_frequencies = sorted(cwe_frequencies.values(), key=lambda x: x["total_frequency"], reverse=True)
    save_json(sorted_frequencies, output_filename)
    
    print(f"Frequency analysis saved to {output_filename}")
