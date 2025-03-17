import json

def get_json_list_length(file_path):
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            data = json.load(file)
            
            if isinstance(data, list):
                return len(data)
            else:
                print("Error: JSON data is not a list.")
                return None
    except (FileNotFoundError, json.JSONDecodeError) as e:
        return None

def get_attack_success_rate(library_path):
    success_cnt = get_json_list_length(f"{library_path}/success_library.json")
    failure_cnt = get_json_list_length(f"{library_path}/failure_library.json")
    
    if success_cnt is None or failure_cnt is None:
        return None
    
    acc = success_cnt / (success_cnt + failure_cnt) if (success_cnt + failure_cnt) > 0 else 0
    
    if success_cnt + failure_cnt != 96:
        print(library_path)
        return f"only {success_cnt + failure_cnt} total with acc of {acc}"
    
    return acc
    

# Example usage
if __name__ == "__main__":
    try:
        with open('stat_3.5.json', 'r') as f:
            results = json.load(f)
    except (FileNotFoundError, json.JSONDecodeError):
        results = {}
    
    for attacker in ['prompt', 'tuned']:
        if attacker not in results:
            results[attacker] = {}
        for victim in ['llama3_8b', 'codellama']:
            if victim not in results[attacker]:
                results[attacker][victim] = {}
            for method in ['comment', 'compare_rag', '1st_rag']:
                use_rag = False if method == "comment" else True

                library_name = f"{method}_{attacker}_{use_rag}_{victim}"
                
                acc = get_attack_success_rate(library_name)
                if acc is not None:
                    results[attacker][victim][method] = acc
                    with open('stat_3.5.json', 'w') as f:
                        json.dump(results, f, indent=4)
                        
                        
                        


# import json

# def get_json_list_length(file_path):
#     try:
#         with open(file_path, 'r', encoding='utf-8') as file:
#             data = json.load(file)
            
#             if isinstance(data, list):
#                 return len(data)
#             else:
#                 print("Error: JSON data is not a list.")
#                 return None
#     except (FileNotFoundError, json.JSONDecodeError) as e:
#         return None

# def get_attack_success_rate(library_path):
#     success_cnt = get_json_list_length(f"{library_path}/success_library.json")
#     failure_cnt = get_json_list_length(f"{library_path}/failure_library.json")
    
#     if success_cnt is None or failure_cnt is None:
#         return None
    
#     acc = success_cnt / (success_cnt + failure_cnt) if (success_cnt + failure_cnt) > 0 else 0
    
#     if success_cnt + failure_cnt != 32:
#         print(library_path)
    
#     return acc

# # Example usage
# if __name__ == "__main__":
#     try:
#         with open('stat_combined.json', 'r') as f:
#             results = json.load(f)
#     except (FileNotFoundError, json.JSONDecodeError):
#         results = {}
    
#     for attacker in ['fullfinetuned', 'fullfinetuned_rag', 'prompt', 'prompt_rag']:
#         if attacker not in results:
#             results[attacker] = {}
#         for victim in ['llama3_8b', 'codellama']:
#             total_success = 0
#             total_failure = 0
#             for method in ['general', 'history', 'repeate']:
#                 library_name = f"cwe_{method}_attacker_{attacker}_victim_{victim}"
#                 success_cnt = get_json_list_length(f"{library_name}/success_library.json")
#                 failure_cnt = get_json_list_length(f"{library_name}/failure_library.json")
                
#                 if success_cnt is not None:
#                     total_success += success_cnt
#                 if failure_cnt is not None:
#                     total_failure += failure_cnt
            
#             if total_success + total_failure > 0:
#                 results[attacker][victim] = total_success / (total_success + total_failure)
#                 with open('stat_combined.json', 'w') as f:
#                     json.dump(results, f, indent=4)
