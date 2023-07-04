setInterval(
    () => {
        try{
            let mess =  document.getElementById("messages")
            mess.remove()
        }catch(err){
        }
    }
, 2500);
