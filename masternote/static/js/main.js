//show markdown live



window.onload = function () {

    
    fix_code_problem();
    window.onresize = fix_code_problem;
    
    // Responsive code block
    function fix_code_problem() {
        let precode = document.querySelectorAll(".markdown-render .highlight")
        precode_arr = Array.from(precode)
      
        precode_arr.forEach(element => {
            const widthPercentage = 92;
            const parentWidth = element.parentElement.offsetWidth;
            const childWidth = (parentWidth * widthPercentage) / 100;
            element.style.width = childWidth + 'px';

        });
    }


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
