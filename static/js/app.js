document.addEventListener("DOMContentLoaded", () => {
    const userInput = document.getElementById("user-input");
    const sendBtn = document.getElementById("send-btn");
    const chatMessages = document.getElementById("chat-messages");
  
    sendBtn.addEventListener("click", sendMessage);
  
    function sendMessage() {
      const query = userInput.value.trim();
  
      if (query) {
      
        const userMessageDiv = document.createElement("div");
        userMessageDiv.className = "user-message";
        userMessageDiv.textContent = query;
        chatMessages.appendChild(userMessageDiv);
  
    
        userInput.value = "";
  
        chatMessages.scrollTop = chatMessages.scrollHeight;
  
        
        fetch("/process_query", {
          method: "POST",
          headers: { "Content-Type": "application/json" },
          body: JSON.stringify({ query }),
        })
          .then((response) => response.json())
          .then((data) => {
            
            const botMessageDiv = document.createElement("div");
            botMessageDiv.className = "bot-message";
            botMessageDiv.textContent = data.response;
            chatMessages.appendChild(botMessageDiv);
  
            chatMessages.scrollTop = chatMessages.scrollHeight;
          })
          .catch((error) => {
            console.error("Error:", error);
          });
      }
    }
  });
  