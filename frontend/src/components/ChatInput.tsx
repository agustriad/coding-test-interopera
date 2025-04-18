"use client";

import { useState, useOptimistic } from "react";
import { useChat } from "@/contexts/ChatContext";
import { sendPrompt } from "@/services/prompt";
import { Chat } from "@/types/chats";

export default function ChatInput() {
  const [input, setInput] = useState("");
  const { addChat } = useChat();
  const [optimisticChats, addOptimisticChat] = useOptimistic<Chat[]>([]);


  const handleSubmit = async () => {
    if (!input.trim()) return;
    console.log(optimisticChats.length,"optimisticChats.length222")
    const newChat: Chat = { id: Date.now().toString(), type:"text", content: input, response: null };
    addChat(newChat);
    addOptimisticChat([...optimisticChats, newChat]);
    setInput("");

    console.log(optimisticChats.length,"optimisticChats.length")
    try {
      const res = await sendPrompt(input);
      const aiChat: Chat = res;
      addChat(aiChat);
      addOptimisticChat([...optimisticChats, aiChat]);
    } catch (error) {
      console.error("Error:", error);
    }
  };

  return (
    <div className="flex gap-2 p-4 border-t">
      <input
        type="text"
        className="flex-1 p-2 border rounded"
        value={input}
        onChange={(e) => setInput(e.target.value)}
        placeholder="Prompt..."
      />
      <button onClick={handleSubmit} className="p-2 px-4 rounded bg-blue-500 text-white">
        {optimisticChats.length % 2 !== 0 ? "⏳" : "Send"}
      </button>
    </div>
  );
}
