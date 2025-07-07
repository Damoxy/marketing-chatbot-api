import { useState } from "react";
import { Input } from "@/components/ui/input";
import { Button } from "@/components/ui/button";

export default function App() {
  const [messages, setMessages] = useState([
    { role: "system", content: "You are a marketing chatbot. Ask only marketing-related questions." },
    { role: "assistant", content: "Hi! Let's talk marketing. What marketing goal are you currently focused on?" }
  ]);
  const [input, setInput] = useState("");
  const [loading, setLoading] = useState(false);

  const sendMessage = async () => {
    if (!input.trim()) return;
    const newMessages = [...messages, { role: "user", content: input }];
    setMessages(newMessages);
    setInput("");
    setLoading(true);

    const response = await fetch("http://localhost:8000/api/chat", {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({ messages: newMessages })
    });
    const data = await response.json();
    setMessages([...newMessages, data]);
    setLoading(false);
  };

  return (
    <div className="max-w-2xl mx-auto mt-10 p-4">
      <h1 className="text-2xl font-bold mb-4">Marketing Chatbot</h1>
      <div className="space-y-4 h-[60vh] overflow-y-auto border p-4 rounded-lg">
        {messages
          .filter((msg) => msg.role !== "system")
          .map((msg, idx) => (
            <div key={idx} className={`p-2 rounded ${msg.role === "user" ? "bg-blue-100 text-right" : "bg-gray-100 text-left"}`}>
              <p>{msg.content}</p>
            </div>
          ))}
        {loading && <p className="text-gray-500">Thinking...</p>}
      </div>
      <div className="flex mt-4">
        <Input value={input} onChange={(e) => setInput(e.target.value)} placeholder="Type your message..." />
        <Button onClick={sendMessage} className="ml-2">Send</Button>
      </div>
    </div>
  );
}
