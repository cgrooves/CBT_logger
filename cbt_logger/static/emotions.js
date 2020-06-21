
function addEmotion() {
    
    // Get the input value
    let emotionText = document.getElementById("emotionsInput").nodeValue;
    if (emotionText == "")
    {
        alert("You must enter text for the emotion!");
        return;
    }
    document.getElementById("emotionsInput").nodeValue = "";
    
    // Create the new emotion item
    let newEmotion = document.createElement("li");
    newEmotion.appendChild(document.createTextNode(emotionText));

    // Append the emotion
    let emotionsList = document.getElementById("emotionsList");
    emotionsList.appendChild(newEmotion);

    // Create the Slider
    let slider = document.createElement("input");
    slider.type = "range";
    slider.min = 0;
    slider.max = 100;
    slider.value = 50;
    slider.step = 5;
    newEmotion.appendChild(slider);

    // Create the "delete" button
    let close = document.createElement("span");
    let closeText = document.createTextNode("\u00D7");
    close.className = "listClose";
    close.onclick = removeEmotion;
    close.appendChild(closeText);
    newEmotion.appendChild(close);
}

function removeEmotion() {
    let listItem = this.parentElement;
    emotionsList.removeChild(listItem);
}