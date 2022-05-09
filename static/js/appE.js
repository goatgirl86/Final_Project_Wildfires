function make_pred(){
    let fire_id= document.getElementById("fire_id").value;
    let fire_size= document.getElementById("fire_size").value;
    let fire_cause= document.getElementById("fam_size").value;
    let latitude= document.getElementById("latitude").value;
    let longitude= document.getElementById("longitude").value;
    let state= document.getElementById("state").value;
    let discovery_month= document.getElementById("discovery_month").value;
    let Temp_pre_30= document.getElementById("Temp_pre_30").value;
    let Temp_pre_15= document.getElementById("Temp_pre_15").value;
    let Temp_pre_7= document.getElementById("Temp_pre_7").value;
    let Wind_pre_30= document.getElementById("Wind_pre_30").value;
    let Wind_pre_15= document.getElementById("Wind_pre_15").value;
    let Wind_pre_7= document.getElementById("Wind_pre_7").value;
    let Hum_pre_30= document.getElementById("Hum_pre_30").value;
    let Hum_pre_15= document.getElementById("Hum_pre_15").value;
    let Hum_pre_7= document.getElementById("Hum_pre_7").value;
    let year= document.getElementById("year").value;
    let putout_time= document.getElementById("putout_time").value;
    let fire_size_bin= document.getElementById("fire_size_bin").value;

    console.log("fire_id",fire_id) 
    console.log("fire_size",fire_size)
    console.log("fire_cause",fire_cause)
    console.log("latitude",latitude)
    console.log("longitude",longitude)
    console.log("state",state)  
    console.log("discovery_month",discovery_month)
    console.log("Temp_pre_30",Temp_pre_30)
    console.log("Temp_pre_15",Temp_pre_15)
    console.log("Temp_pre_7",Temp_pre_7)
    console.log("Wind_pre_30",Wind_pre_30)
    console.log("Wind_pre_15",Wind_pre_15)
    console.log("Wind_pre_7",Wind_pre_7)
    console.log("Hum_pre_30",Hum_pre_30)
    console.log("Hum_pre_15",Hum_pre_15)
    console.log("Hum_pre_7",Hum_pre_7)
    console.log("year",year)
    console.log("putout_time",putout_time)
    console.log("fire_size_bin",fire_size_bin)
    
    fetch("/predict", {
        method: "POST", 
        body: JSON.stringify({
            fire_id: fire_id,
            fire_size: fire_size,
            fire_cause: fire_cause,
            latitude: latitude,
            longitude: longitude,
            state: state,
            discovery_month: discovery_month,
            Temp_pre_30: Temp_pre_30,
            Temp_pre_15: Temp_pre_15, 
            Temp_pre_7: Temp_pre_7,
            Wind_pre_30: Wind_pre_30,
            Wind_pre_15: Wind_pre_15,
            Wind_pre_7: Wind_pre_7,
            Hum_pre_30: Hum_pre_30,
            Hum_pre_15: Hum_pre_15,
            Hum_pre_7: Hum_pre_7,
            year: year,
            putout_time: putout_time,
            fire_size_bin: fire_size_bin

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