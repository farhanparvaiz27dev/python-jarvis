$(document).ready(function () {

    eel.init()

    $(".text").textillate({
        loop: true,
        sync: true,
        in: {
            effect: "bounceIn"
        },
        out: {
            effect: "bounceOut"
        }
    })

    // siri configuration
    var siriWave = new SiriWave({
        container: document.getElementById("siri-container"),
        width: 800,
        height: 200,
        style: "ios9",
        amplitude: 1,
        speed: 0.3,
        autostart: true,
        frequency: 2,

    });


    $(".siri-message").textillate({
        loop: true,
        sync: true,
        in: {
            effect: "fadeInUp",
            delayScale: 1.0,
            delay: 30,
            sync: true,
        },
        out: {
            effect: "fadeOutUp",
            delayScale: 1.0,
            delay: 30,
            sync: true,
        }
    });

    //  mic click listener
    $("#MicBtn").click(function () {
        eel.playAssistantSound();
        $("#oval").attr("hidden", true);
        $("#siriwave").removeAttr("hidden");
        eel.allcommands()();
    });


    function doc_keyUp(e) {
        // Check if 'j' key is pressed along with the Meta key (e.g., Command on macOS)
        if (e.key === 'j' && e.metaKey) {
            eel.playAssistantSound();
            $("#oval").attr("hidden", true);
            $("#siriwave").attr("hidden", false);
            eel.allcommands()(); // Removed extra ()
        }
    }

    document.addEventListener("keyup", doc_keyUp, false);


    // to play assisatnt 
    function PlayAssistant(message) {

        if (message != "") {

            $("#oval").attr("hidden", true);
            $("#siriwave").attr("hidden", false);
            eel.allcommands(message);
            // $("#chatbox").val("")
            $("#Chatbot").val("");
            $("#MicBtn").attr('hidden', false);
            $("#SendBtn").attr('hidden', true);

        }

    }
    // toogle fucntion to hide and display mic and send button 
    function ShowHideButton(message) {
        if (message.length == 0) {
            $("#MicBtn").attr('hidden', false);
            $("#SendBtn").attr('hidden', true);
        }
        else {
            $("#MicBtn").attr('hidden', true);
            $("#SendBtn").attr('hidden', false);
        }
    }

    // key up event handler on text box
    $("#Chatbot").keyup(function () {

        let message = $("#Chatbot").val();
        ShowHideButton(message)

    });
    // send button event handler
    $("#SendBtn").click(function () {

        let message = $("#Chatbot").val()
        PlayAssistant(message)

    });
    // enter press event handler on chat box
    $("#Chatbot").keypress(function (e) {
        key = e.which;
        if (key == 13) {
            let message = $("#Chatbot").val()
            PlayAssistant(message)
        }
    });

    

});




