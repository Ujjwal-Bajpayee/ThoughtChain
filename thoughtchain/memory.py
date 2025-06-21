import json
import os
import hashlib

MEMORY_FILE = "memory.json"

def load_memory():
    if os.path.exists(MEMORY_FILE):
        with open(MEMORY_FILE, "r") as f:
            return json.load(f)
    return {}

def save_memory(memory):
    with open(MEMORY_FILE, "w") as f:
        json.dump(memory, f, indent=2)

def hash_text(text):
    """
    Generate a SHA-256 hash of the input text to uniquely identify tasks.
    """
    return hashlib.sha256(text.encode()).hexdigest()

def memory_lookup(task_hash):
    """
    Look up a hashed task in memory and return the stored result if found.
    """
    memory = load_memory()
    return memory.get(task_hash, None)

def memory_store(task_hash, result):
    """
    Store the result of a task using its hash as the key.
    """
    memory = load_memory()
    memory[task_hash] = result
    save_memory(memory)

def memory_agent(task):
    """
    Check if the task has been processed before using its hash.
    Returns (result, hash) where result may be None if not found.
    """
    task_hash = hash_text(task)
    result = memory_lookup(task_hash)
    return result, task_hash
