document.addEventListener('DOMContentLoaded', () => {
    // Enter-Key event for text area
    document.querySelector('#emotionsInput').onkeyup = (event) => {
        if (event.keyCode == 13)
        {
            document.getElementById("emotionButton").click();
        }
    };
    // onclick for buttons
    document.querySelector('#emotionButton').onclick = addEmotion;
    document.querySelector('#pushEmotionsBtn').onclick = pushEmotions;
});

function pushEmotions() {
    
    // Gather up the emotions
    let emotions = document.getElementsByClassName("emotionItem");
    if (emotions.length == 0)
    {
        alert("No emotions specified! Please list at least one emotion.");
        return;
    }
    
    // Create JSON object for HTML elements
    let out = [];
    for (let i = 0; i < emotions.length; i++)
    {
        let emotionJSON = {
            "id": emotions[i].dataset.id,
            // "range": emotions[i].querySelector("#emotionSlider").value,
            "name": emotions[i].dataset.name
        };
        
        // Add emotion JSON to list
        console.log("ID: " + emotionJSON.id + ", EMOTION: " + emotionJSON.name);
        out.push(emotionJSON);
    }

    // Open up the AJAX cxn
    let xhttp = new XMLHttpRequest();

    // Open up POST request
    xhttp.open('POST', '/emotions/push', true);

    // Send the JSON
    xhttp.send(JSON.stringify(out));

}

function addEmotion() {
    
    // Get the input value
    let emotionText = document.getElementById("emotionsInput").value;
    if (emotionText == "")
    {
        alert("You must enter text for the emotion!");
        return;
    }
    // reset the input field string
    document.getElementById("emotionsInput").value = "";
    
    // Create the new emotion item
    let newEmotion = document.createElement("li");
    newEmotion.className = "emotionItem";
    // group the text in with the list item
    newEmotion.appendChild(document.createTextNode(emotionText));

    // Create the custom data
    newEmotion.dataset.id = -1;
    newEmotion.dataset.name = newEmotion.innerText || newEmotion.textContent;

    // Append the emotion to the list
    let emotionsList = document.getElementById("emotionsList");
    emotionsList.appendChild(newEmotion);

    // Create the Slider
    let slider = document.createElement("input");
    slider.type = "range";
    slider.min = 0;
    slider.max = 100;
    slider.value = 50;
    slider.step = 5;
    slider.className = "emotionSlider";
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