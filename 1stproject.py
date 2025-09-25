import google.generativeai as genai

# Configure your API Key
genai.configure(api_key="AIzaSyCnfagE_vM-CCDVdr2vQQ9iFeEJOE8skp8")

# Create model instance
model = genai.GenerativeModel("gemini-1.5-flash")

print("\n--- Text Summarization Console App ---")
print("Type 'exit' to quit.\n")

# Interactive loop
while True:
    user_input = input("Enter text to summarize:\n")

    if user_input.lower() in ["exit", "quit"]:
        print("Goodbye!")
        break

    # Generate summary
    try:
        response = model.generate_content(f"Summarize the following text:\n{user_input}")
        print("\n--- Summary ---")
        print(response.text.strip())
        print("----------------\n")
    except Exception as e:
        print(f"Error: {e}")
