import requests, os, torch, numpy as np
from bs4 import BeautifulSoup

# Get all .md files (DOCS)
response = requests.get('https://huggingface.co/hexgrad/Kokoro-82M/tree/main')
soup = BeautifulSoup(response.text, 'html.parser')

for link in soup.find_all('a', href=True):
    if link['href'].endswith('.md?download=true'):
        file_url = f'https://huggingface.co{link["href"]}'
        file_name = file_url[:-14].split('/')[-1]
        print(f"Downloading {file_name} from {file_url}")
        file_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'voices', file_name)
        with open(f'{file_path}', 'wb') as f: f.write(requests.get(file_url).content)

# Get all .pt file (VOICES)
response = requests.get('https://huggingface.co/hexgrad/Kokoro-82M/tree/main/voices')
soup = BeautifulSoup(response.text, 'html.parser')

for link in soup.find_all('a', href=True):
    if link['href'].endswith('.pt?download=true'):
        file_url = f'https://huggingface.co{link["href"]}'
        file_name = file_url[:-14].split('/')[-1]
        print(f"Downloading {file_name} from {file_url}")
        file_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'voices', file_name)
        with open(f'{file_path}', 'wb') as f: f.write(requests.get(file_url).content)

path = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'voices')

# List all files
print("---- ST LISTING FILES ----- ")
for file in os.listdir(path): print("-", file)
print("---- ED LISTING FILES ----- ")

# Convert all voices
for file in os.listdir(path):
    if not file.endswith('.pt'): continue
    try:
        voice_style = torch.load(os.path.join(path, file), weights_only = False).numpy().astype(np.float32)
        np.save(os.path.join(path, file).replace('.pt', '.npy'), voice_style)
    except Exception as e:
        print(f"Error processing {file}: {e}")

# Delete old .pt files
for file in os.listdir(path):
    if file.endswith('.pt'): os.remove(os.path.join(path, file))

# List all files
print("---- ST LISTING FILES ----- ")
for file in os.listdir(path): print("-", file)
print("---- ED LISTING FILES ----- ")