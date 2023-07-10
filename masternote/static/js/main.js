

window.onload = function () {

    setInterval(
        () => {
            const mess = document.getElementById("messages")
            if (mess) {
                mess.remove()
            }

            // let errorlistcollection = document.getElementsByClassName("errorlist")
            // let arrerrorlist = Array.from(errorlistcollection)
            // arrerrorlist.forEach(error => {
            //     error.remove()
            // });
        }
        , 2500);



    form_input = document.querySelectorAll('.form input')

    // console.log(form_input)

    form_input.forEach(element => {
        let a = element.parentElement.querySelector(".helptext")

        if (document.activeElement === element) {
            if (!element.value){
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
