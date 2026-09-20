# Financial Chatbot

def chatbot(query):
    query = query.lower()

    if "total revenue" in query:
        return "Microsoft 2025 Revenue: $281.7B, Apple 2025 Revenue: $416.2B, Tesla 2025 Revenue: $103B"

    elif "net income" in query:
        return "Apple had the highest net income in 2025 with approximately $112B."

    elif "assets" in query:
        return "Microsoft had the highest total assets among the analyzed companies."

    elif "cash flow" in query:
        return "All three companies generated positive operating cash flow."

    elif "best performing company" in query:
        return "Based on revenue and net income, Apple showed strong financial performance."

    else:
        return "Sorry, I can only answer predefined financial questions."

print("Financial Chatbot")
print("Type 'exit' to quit")

while True:
    user_input = input("You: ")

    if user_input.lower() == "exit":
        print("Chatbot: Goodbye!")
        break

    print("Chatbot:", chatbot(user_input))
