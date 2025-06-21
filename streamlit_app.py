import streamlit as st
from thoughtchain.agents import strategist, researcher, critic, writer
from thoughtchain.memory import memory_agent, memory_store
from io import BytesIO
from fpdf import FPDF

st.set_page_config(page_title="ThoughtChain", layout="wide")
st.title("🧠 ThoughtChain – Multi-Agent AI Think Tank")

task = st.text_area("Enter a complex task you'd like AI agents to work on:", height=150)

from fpdf import FPDF
from io import BytesIO
import textwrap

def create_pdf(text):
    pdf = FPDF()
    pdf.add_page()
    pdf.set_auto_page_break(auto=True, margin=15)
    pdf.set_font("Arial", size=12)

    # Wrap very long lines to prevent breaking PDF
    for line in text.split("\n"):
        wrapped_lines = textwrap.wrap(line, width=100) or [""]
        for wrapped_line in wrapped_lines:
            pdf.cell(0, 10, wrapped_line, ln=True)

    buffer = BytesIO()
    pdf.output(buffer)
    buffer.seek(0)
    return buffer


if st.button("Run ThoughtChain"):
    if not task.strip():
        st.warning("Please enter a task first.")
    else:
        with st.spinner("Checking memory..."):
            cached_output, task_hash = memory_agent(task)

        if cached_output:
            st.success("✅ Retrieved from memory.")
            st.download_button("📄 Download PDF", create_pdf(cached_output), file_name="thoughtchain_output.pdf")
            st.text_area("🧠 Final Output", value=cached_output, height=300)
        else:
            st.subheader("🔹 Strategist Plan")
            plan = strategist(task)
            st.code(plan)

            subtasks = [line.strip("-• ") for line in plan.split("\n") if line.strip()]
            full_output = ""

            for i, subtask in enumerate(subtasks):
                with st.expander(f"🔍 Subtask {i+1}: {subtask}"):
                    research = researcher(subtask)
                    st.markdown("**📘 Research Output**")
                    st.text_area("Research", value=research, height=200, key=f"research_{i}")

                    critique = critic(research)
                    st.markdown("**🔍 Critique**")
                    st.text_area("Critique", value=critique, height=150, key=f"critique_{i}")

                    full_output += f"Subtask: {subtask}\n{research}\nCritique: {critique}\n\n"


            final = writer(full_output)
            st.success("✅ Final Output Generated")
            st.download_button("📄 Download PDF", create_pdf(final), file_name="thoughtchain_output.pdf")
            st.text_area("📝 Final Output", value=final, height=300)

            memory_store(task_hash, final)
