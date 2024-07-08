import os
import sys
import subprocess
import torch

sys.path.append('/home/shodh/eval')

def evaluate_models(model, tasks):
    model_type, model_args = model.split(":")
    device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
    output_path = f"results/eval_results_{model_type}-{model_args}.json"

    if os.path.exists(output_path):
        os.remove(output_path)

    command = [
        'lm_eval',
        '--model', model_type,
        '--model_args', f"pretrained={model_args}",
        '--tasks', tasks,
        '--device', f'{device}',
        '--log_samples',
        '--output_path', output_path,
        # '--batch_size', 'auto',
    ]
    print(f"Running command: {' '.join(command)}")
    process = subprocess.Popen(command, stdout=subprocess.PIPE, stderr=subprocess.STDOUT, text=True)
    for stdout_line in iter(process.stdout.readline, ""):
        sys.stdout.write(stdout_line)
        sys.stdout.flush()

    stdout, stderr = process.communicate()
    process.stdout.close()
    return_code = process.wait()
    if return_code:
        stderr = process.communicate()[1]
        print(stderr)
