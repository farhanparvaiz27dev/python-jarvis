eel.expose(DisplayMessage);
function DisplayMessage(message){
    console.log("JS RECEIVED:", message);
    $(".siri-message").text(message);
}