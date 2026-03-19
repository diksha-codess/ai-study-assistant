function generate() {
    let topic = document.getElementById("topic").value;

    fetch("http://127.0.0.1:5000/generate", {
        method: "POST",
        headers: {
            "Content-Type": "application/json"
        },
        body: JSON.stringify({ topic: topic })
    })
    .then(res => res.json())
    .then(data => {
        let list = document.getElementById("tasks");
        list.innerHTML = "";

        data.tasks.forEach(t => {
            let li = document.createElement("li");
            li.innerText = t;
            list.appendChild(li);
        });
    });
}