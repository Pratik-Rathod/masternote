//show markdown live



window.onload = function () {
    
    // Editor Functions
    try {
        publish_button()
        markdown_preview()
        preview_buttons_switch()
    } catch (error) {
        console.error(error)
    }

    setInterval(
        () => {
            const mess = document.getElementById("messages")
            if (mess) {
                mess.remove()
            }
        }
        , 2500);

    form_input = document.querySelectorAll('.form input');
    // console.log(form_input)

    form_input.forEach(element => {
        let a = element.parentElement.querySelector(".helptext")

        if (document.activeElement === element) {
            if (!element.value) {
                if (a) {
                    a.style.cssText = "display:block"
                }
            }
        }
        element.addEventListener("input", (e) => {
            if (element.value) {
                if (a) {
                    a.style.cssText = "display:none"
                }

            } else {
                if (a) {
                    a.style.cssText = "display:block"
                }
            }
        })

        element.addEventListener("focus", (e) => {
            if (a) {
                a.style.cssText = "display:block"
            }
        })

        element.addEventListener("blur", () => {
            if (a) {
                a.style.cssText = "display:none"
            }
        })
    });


}
