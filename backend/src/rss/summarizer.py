import ollama  # Ensure this import is correct

def summarize_text(text, model="mistral"):
    """
    Summarizes input text using Ollama's AI model.
    """
    try:
        response = ollama.generate(model, text)
        return response
    except Exception as e:
        print(f"❌ Error summarizing text: {e}")
        return None

if __name__ == "__main__":
    sample_text = "Artificial intelligence is changing the world by automating tasks and improving decision-making processes."
    summary = summarize_text(sample_text)
    print(f"🔍 Summary: {summary}")
