function make_pred() {

    let state= document.getElementById("state").value;
    let discovery_month= document.getElementById("discovery_month").value;
    let Temp_pre_7= document.getElementById("Temp_pre_7").value;
    let Wind_pre_7= document.getElementById("Wind_pre_7").value;
    let Hum_pre_7= document.getElementById("Hum_pre_7").value;



    console.log("state",state)  
    console.log("discovery_month",discovery_month)
    console.log("Temp_pre_7",Temp_pre_7)
    console.log("Wind_pre_7",Wind_pre_7)
    console.log("Hum_pre_7",Hum_pre_7)

    
    fetch("/predict", {
        method: "POST", 
        body: JSON.stringify({
            state: state,
            discovery_month: discovery_month,
            Temp_pre_7: Temp_pre_7,
            Wind_pre_7: Wind_pre_7,
            Hum_pre_7: Hum_pre_7,


        }),
        headers:{
            "Content-type":"application/json;charset=UTF-8"

        } 
    }).then(resp=>{
        return resp.json()
    }).then(resp=>{
        console.log(resp)
        document.getElementById("prediction").innerHTML=resp.Prediction
        console.log(resp.Prediction);
        if (resp.Prediction=="Not a Conspiracy Theorist"){
            document.getElementById("dummy").src= "/static/images/scully.gif" 
        }
        else if (resp.Prediction=="Government Malfeasance"){
            document.getElementById("dummy").src="/static/images/washington.gif"
        }
        else if (resp.Prediction=="Malevolent Global Conspiracy"){
            document.getElementById("dummy").src="/static/images/theyre_watching.gif"
        }
        else if (resp.Prediction=="Extraterrestrial Cover-up"){
            document.getElementById("dummy").src="/static/images/aliens.gif"
        }
        else if (resp.Prediction=="Personal Well-being"){
            document.getElementById("dummy").src="/static/images/mind_control.gif"
        }
        else if (resp.Prediction=="Control of Information"){
            document.getElementById("dummy").src="/static/images/simpsons.gif"
        }
        else if (resp.Prediction){
            document.getElementById("dummy").src="/static/images/jackets.gif"
        }
    })
}