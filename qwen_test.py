import json
import urllib.request
import sqlite3

db=sqlite3.connect("chat_memory.db")

db.execute("""
   CREATE TABLE IF NOT EXISTS memories(
   id INTEGER PRIMARY KEY AUTOINCREMENT,
   fact TEXT NOT NULL)
   """)
db.commit()

url = "http://localhost:11434/api/chat"

messages= []

print(" Qwen Chatbot with presistent Memory")
print("Type 'remember: ...' to save a fact.")
print("Type 'exit' to stop.\n")

while True:
    prompt= input("You: ")

    if prompt.lower() == "exit":
        print("Goodbye!")
        break

    #for saving fact permanently
    if prompt.lower().startswith("remember:"):
        fact=prompt[len("remember:"):].strip()

        if fact:
            db.execute(
                "INSERT INTO memories (fact) VALUES (?)",
                (fact,)
            )
            db.commit()
            print("DEBUG: Saved fact:", fact)
            print("DEBUG: Database file:", db.execute("PRAGMA database_list").fetchone()[2])
            print("BOT:I'll save that in your database.\n")
        else:
            print("Bot: Please provide a fact to remeber.\n")

        continue
    rows =db.execute(
        "SELECT fact FROM memories ORDER BY id"
    ).fetchall()

    save_facts=[row[0] for row in rows]

    system_message = {
        "role": "system",
        "content": (
            "Answer the user using the conversation and saved facts "
            "when relevant. Do not invent personal facts. "
            "Saved facts:\n" + "\n".join(save_facts)
        )
    }


    messages.append({
        "role":"user",
        "content":prompt
    })

    data={
       "model":"qwen3:0.6b",
       "messages":[system_message]+messages,
       "stream":False
    }

    request = urllib.request.Request(
      url,
      data=json.dumps(data).encode("utf-8"),
      headers={"content-Type": "application/json"}


    )
    with urllib.request.urlopen(request) as response:
       result = json.loads(response.read().decode("utf_8"))

    answer=result["message"]["content"]

    messages.append({
        "role":"assistant",
        "content":answer
    }
    )


    print("Bot:", answer,"\n")
db.close()
print("Chatbot closed")