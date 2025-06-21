from thoughtchain.agents import strategist, researcher, critic, writer
from thoughtchain.memory import memory_agent, memory_store

def run_thoughtchain(task):
    print("🧠 Task:", task)

    # 🔁 Check if this task was already solved
    cached_output, task_hash = memory_agent(task)
    if cached_output:
        print("\n🧠 Memory Found:")
        print(cached_output)
        return

    # 🧠 Step 1: Strategy
    plan = strategist(task)
    print("\n🔹 Strategist's Plan:\n", plan)

    subtasks = [line.strip("-• ") for line in plan.split("\n") if line.strip()]
    outputs = []

    for subtask in subtasks:
        print(f"\n🔍 Researching: {subtask}")
        research = researcher(subtask)
        print("📘 Research Output:", research)

        critique = critic(research)
        print("🔍 Critique:", critique)

        outputs.append(f"Subtask: {subtask}\n{research}\nCritique: {critique}\n")

    # 🧠 Step 2: Final Report
    final = writer("\n".join(outputs))
    print("\n✅ Final Output:\n", final)

    # 💾 Store to memory
    memory_store(task_hash, final)

if __name__ == "__main__":
    user_task = input("Enter a complex task for ThoughtChain: ")
    run_thoughtchain(user_task)
