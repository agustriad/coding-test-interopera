"use client";
import ReactMarkdown from 'react-markdown';
import remarkGfm from 'remark-gfm';

import { useChat } from "@/contexts/ChatContext";

export default function ChatList() {
  const { chats } = useChat();

  return (
    <div className="p-4 space-y-3 overflow-auto">
      {chats.map((chat) => (
        // eslint-disable-next-line react/jsx-key
        <div className={`p-5 rounded ${!chat.response ? "bg-blue-100 text-blue-900" : "bg-gray-200 text-gray-900"} w-90 h-auto `}>
            <ReactMarkdown  remarkPlugins={[remarkGfm]}>{!chat.response ? chat.content : chat.response}</ReactMarkdown>
        </div>
      ))}
    </div>
  );
}
