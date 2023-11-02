function getBotResponse(input) {
    

    // Simple responses
    if (input == "hello") {
        return "Hello there! I am Rythu";
    } else if (input == "goodbye") {
        return "Talk to you later!";
    } else if (input == "what you do ") {
        return "I can do Crop Suggetions   Disease Prediction   Fertilizer Recomamdation";
    } else if (input == "open crop suggetion") {
        return "url";
    } else {
        return "Try asking something else!";
    }
}