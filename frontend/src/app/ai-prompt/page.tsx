import ChatInput from "@/components/ChatInput";
import ChatList from "@/components/ChatList";
import { ChatProvider } from "@/contexts/ChatContext";

export default function AIPromptPage() {
  return (
    <ChatProvider>
      <div className="flex flex-col h-screen">
        <h1 className="p-4 text-2xl font-bold">AI Prompt</h1>
        <div className="flex-1 overflow-auto">
          <ChatList />
        </div>
        <ChatInput />
      </div>
    </ChatProvider>
  );
}
