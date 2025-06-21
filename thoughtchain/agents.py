from thoughtchain.utils import call_llm

def strategist(task):
    """
    Strategist Agent: Breaks down the task into 3–5 sub-tasks.
    """
    prompt = f"You are a project strategist. Break down the following task into 3–5 clear, actionable sub-tasks:\n\nTask: {task}"
    return call_llm(prompt)

def researcher(subtask):
    """
    Researcher Agent: Provides insights, data, or background for the sub-task.
    """
    prompt = f"You are a researcher. Provide detailed insights, explanations, or relevant findings for the sub-task:\n\n{subtask}"
    return call_llm(prompt)

def critic(content):
    """
    Critic Agent: Reviews the content critically, pointing out assumptions, gaps, or improvements.
    """
    prompt = f"You are a critical reviewer. Provide a short critique of the following output:\n\n{content}"
    return call_llm(prompt)

def writer(collected_outputs):
    """
    Writer Agent: Synthesizes all subtask outputs into a polished final document.
    """
    prompt = f"Compile the following research and critiques into a coherent, well-structured final report:\n\n{collected_outputs}"
    return call_llm(prompt)
