function addEmotion() {
    // Get the list and click-able item
    emotionsList = document.getElementById("emotions_list");
    addItem = document.getElementById("add_emotions");

    // add a new list item
    emotion = document.createElement("li");
    emotion.innerHTML = "another emotion";
    emotion.addEventListener("dblclick", removeEmotion);
    
    // append
    emotionsList.insertBefore(emotion, addItem);
}

function removeEmotion() {
    document.getElementById("emotions_list").removeChild(this);
}