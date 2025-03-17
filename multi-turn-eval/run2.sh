export CUDA_VISIBLE_DEVICES=0,1,2,3,4,5,6,7

#!/bin/bash

# List of victim models and their short names
declare -A victims=(
    ["codegemma"]="google/codegemma-7b-it"
    ["qwen"]="Qwen/Qwen2.5-7B-Instruct"
    ["codeqwen"]="Qwen/Qwen2.5-Coder-7B-Instruct"
)



# Run experiments for each victim model
for victim_name in "${!victims[@]}"; do
    victim_model="${victims[$victim_name]}"
    echo "Running experiment for victim: $victim_name ($victim_model)"
    
    python autodan_eval_compare_rag.py --victim_name "$victim_name" --victim_model "$victim_model" 
    
    echo "Finished experiment for $victim_name"
    echo "----------------------------------"
done
