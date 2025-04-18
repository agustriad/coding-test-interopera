class HttpClient():

    def gemini():
        return {
            "headers":{
                "Content-Type": "application/json",
            },
            "model-control":{
                "text": "gemini-2.0-flash:generateContent",
                "image": "gemini-2.0-flash-exp-image-generation:generateContent"
            },

        }
    
