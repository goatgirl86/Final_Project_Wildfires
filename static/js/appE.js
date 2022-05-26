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
        headers:{
            "Content-type":"application/json" 
            // charset=UTF-8
    
        }, 
        body: JSON.stringify({
            state: state,
            discovery_month: discovery_month,
            Temp_pre_7: Temp_pre_7,
            Wind_pre_7: Wind_pre_7,
            Hum_pre_7: Hum_pre_7,


        }),
    })
    .then(res => res.json())
    .then(data=>{
        console.log(data)
        document.getElementById("prediction").innerHTML=data.Prediction
        
        if (data.Prediction=="0"){
            document.getElementById("dummy").src="/static/images/little_fire_2.jpg" 
        }
        else if (data.Prediction=="1"){
            document.getElementById("dummy").src="/static/images/big_fire_2.jpg"
        }

    })
}